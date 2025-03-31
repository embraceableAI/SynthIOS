import argparse
import json
from openai import OpenAI
from prompt_templates import *
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import *
from qdrant_client import QdrantClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
model_name = os.getenv("MODEL_NAME")
ionos_api_key = os.getenv("IONOS_API_KEY")
ionos_api_base = os.getenv("IONOS_API_BASE")
qdrant_host = os.getenv("QDRANT_HOST")

# Initialize Qdrant client
qdrant_client = QdrantClient(qdrant_host)

try:
    client = OpenAI(api_key=ionos_api_key, base_url=ionos_api_base)
    
    # Test the connection with a simple API call
    print("Testing IONOS connection...")
    test_response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": "Hello, are you working?"}],
        max_tokens=10
    )
    print(f"IONOS connection successful! Response: {test_response.choices[0].message.content}")
except Exception as e:
    print(f"Error connecting to IONOS: {str(e)}")
    raise  # Re-raise the exception to stop the script if connection fails



def process_persona(persona, template, args):
    try:
        updated_persona = get_adjusted_persona(client, persona, model_name, args.language)
        user_prompt = template.format(persona=updated_persona)
        print(f"User Prompt: {user_prompt}")  # Add this line to print the user prompt
    except KeyError as e:
        print(f"KeyError: {e} in persona: {persona}")
        return None

    problem_sample = get_problem_hard_reasoning(client, model_name, user_prompt)
    problem_sample = problem_sample.replace("**", "")
    print(f"HARD PROBLEM: {problem_sample}")
    print("==================================================================")
    correct_solution = get_response_hard_reasoning(client, model_name, problem_sample, args.language)
    correct_solution = correct_solution.replace("**", "")
    print(f"HARD REASONING: {correct_solution}")
    print("==================================================================")
    wrong_solution = get_wrong_response_hard_reasoning(client, model_name, problem_sample, args.language)
    wrong_solution = wrong_solution.replace("**", "")
    wrong_solution = wrong_solution.replace("### ", "")
    print(f"WRONG SOLUTION: {wrong_solution}")
    print("==================================================================")
    # Only continue to add Sample if problem and correct_solution and wrong_solution:
    if problem_sample and correct_solution and wrong_solution:
        return {"input_persona": updated_persona, "persona_prompt": user_prompt, "problem": problem_sample, "correct_solution": correct_solution,"wrong_solution": wrong_solution}
    else:
        print(f"Failed to generate problem and solution for persona: {persona}")
        return None
        

def main(args):

    # --- Validate topic ---
    if not args.topic or not isinstance(args.topic, str) or not args.topic.strip():
        raise ValueError("Invalid or missing topic. Please provide a non-empty topic string with --topic.")
    
    # Load the appropriate template
    if args.language == "de":
        template = hard_reasoning_template_de
    elif args.language == "en":
        template = hard_reasoning_template_en
    else:
        raise ValueError("Language is required, please choose between 'en' and 'de'.")

    # generate candidates
    initial_query=args.topic
    num_candidates=args.sample_size
    list_personas=get_semantic_result(client, initial_query ,qdrant_client,num_candidates)

    with open(args.output_path, "w", encoding="utf-8") as out:
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(process_persona, persona, template, args) for persona in list_personas]
            for future in tqdm(as_completed(futures), total=len(futures)):
                result = future.result()
                if result:
                    out.write(json.dumps(result, ensure_ascii=False) + '\n')

    print(f"Outputted the results to: {args.output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synthesize text using a specified model and template.")
    parser.add_argument(
    '--topic',
    type=str,
    required=True,
    help='The topic to generate text about.'
)
    parser.add_argument(
    '--language',
    type=str,
    required=True,
    choices=['en', 'de'],
    help='Language for text generation. Choose from "en" (English) or "de" (German).'
)
    parser.add_argument(
    '--sample_size',
    type=int,
    default=5,
    help='Number of samples to process from the dataset. Default is 5'
)
    
    parser.add_argument(
    '--output_path',
    type=str,
    default="./output.jsonl",
    help='The output filename to save the output'
)

    args = parser.parse_args()
    main(args)

