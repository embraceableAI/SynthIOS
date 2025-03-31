from collections import Counter
from prompt_templates import *

#Functions
def rank_by_majority_domain(search_result, top_k: int = 5):
    """
    1) Majority on general domain => Subset #1.
    2) Among that subset, majority on specific domain => Subset #2.
    3) If Subset #2 < 5, fill from Subset #1 (in original order) until 5.
    4) If Subset #1 is still < 5, (rare case) fill from full search_result.
    """

    # Helper to get "general domain" (lowercased) from a payload
    def get_general(payload):
        top1 = payload.get("general domain (top 1 percent)")
        top01 = payload.get("general domain (top 0.1 percent)")
        val = top1 if top1 and top1.lower() != "none" else top01
        return val.strip().lower() if val and val.lower() != "none" else None

    # Helper to get "specific domain" (lowercased) from a payload
    def get_specific(payload):
        top1 = payload.get("specific domain (top 1 percent)")
        top01 = payload.get("specific domain (top 0.1 percent)")
        val = top1 if top1 and top1.lower() != "none" else top01
        return val.strip().lower() if val and val.lower() != "none" else None

    # --- Step 1: Majority vote for "general domain" ---
    general_list = []
    general_map = {}  # map: result.id -> normalized general domain

    for r in search_result:
        g = get_general(r.payload)
        if g:
            general_list.append(g)
            general_map[r.id] = g

    # If no valid general domains, just return top_k from the original
    if not general_list:
        return search_result[:top_k]

    counter_general = Counter(general_list)
    max_g_count = max(counter_general.values())
    # All domains that tie for top frequency
    majority_generals = {d for d, c in counter_general.items() if c == max_g_count}

    # Build Subset #1 in original order
    subset1 = [r for r in search_result if general_map.get(r.id) in majority_generals]

    # --- Step 2: Majority vote for "specific domain" among Subset #1 ---
    specific_list = []
    specific_map = {}  # map: result.id -> normalized specific domain

    for r in subset1:
        s = get_specific(r.payload)
        if s:
            specific_list.append(s)
            specific_map[r.id] = s

    # If none have a specific domain, we skip Step 2 majority
    if not specific_list:
        # Then Subset #2 is just Subset #1
        subset2 = subset1
    else:
        counter_specific = Counter(specific_list)
        max_s_count = max(counter_specific.values())
        majority_specifics = {d for d, c in counter_specific.items() if c == max_s_count}

        # Build Subset #2 in the original order
        subset2 = [r for r in subset1 if specific_map.get(r.id) in majority_specifics]

    # --- Step 3: Ensure we have 5 results ---
    # We always keep them in the order of search_result (original ranking).
    # subset2 is already in the original order (because we iterated in order).

    if len(subset2) >= top_k:
        # Just take the first top_k from Subset #2
        return subset2[:top_k]
    else:
        # If we have fewer than top_k from Subset #2, let's fill from Subset #1
        # (excluding any already in Subset #2), in original order.
        needed = top_k - len(subset2)
        subset2_ids = {r.id for r in subset2}
        extended = list(subset2)  # copy

        # fill from Subset #1
        for r in subset1:
            if r.id not in subset2_ids:
                extended.append(r)
                subset2_ids.add(r.id)
            if len(extended) == top_k:
                break

        # If we still don't reach top_k (very unlikely unless Subset #1 is also small),
        # fill from the full search_result
        if len(extended) < top_k:
            for r in search_result:
                if r.id not in subset2_ids:
                    extended.append(r)
                    subset2_ids.add(r.id)
                if len(extended) == top_k:
                    break

        return extended
    


def get_semantic_result(client, query, qdrant_client, num_candidate, collection_name="personas", embedding_model="BAAI/bge-m3"):
    embedding_response = client.embeddings.create(
        model=embedding_model,
            input=query)
    vector = embedding_response.data[0].embedding
    search_result = qdrant_client.search(
        collection_name=collection_name,
        query_vector=vector,
        limit=num_candidate
    )

    filtered_result=rank_by_majority_domain(search_result, num_candidate)
    list_personas=[result.payload['persona'] for result in filtered_result]

    return list_personas



def get_adjusted_persona(client, persona, model, langugae):

    if langugae=='de':
        content= "Ändere die Bezeichnung und Beschreibung der gegebenen Persona ab, bleibe allerdings im selben Themengebiet. Verändere den Fokus der Persona oder füge bestimmte Aspekte in kurzer Form hinzu. Schreibe die neue aber in der Struktur ähnliche Personabeschreibung in Deutsch."
    else:
        content="Change the name and description of the given persona, but stay within the same subject area. Change the focus of the persona or add certain aspects in short form."
    
    completion = client.chat.completions.create(
        model=model,
        temperature=0.7,
        messages=[
            {"role": "system", "content":content},
            {"role": "user", "content": f"{persona}"}
        ]
    )
    return completion.choices[0].message.content


def get_problem_hard_reasoning(client, model_name, user_prompt):
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": f"{user_prompt}"}
        ]
    )
    response = completion.choices[0].message.content
    return response


def get_response_hard_reasoning(client, model_name, problem_sample, language):
    if language=="de":
        system = system_de
    else:
        system = system_en

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": problem_sample}
        ]
    )
    response = completion.choices[0].message.content
    return response



def get_wrong_response_hard_reasoning(client, model_name, problem_sample, language):

    if language=='de':
        content=f"Löse das folgende Problem so schnell und kurz wie möglich aber falsch:\n{problem_sample}"
    else:
        content=f"Provide a solution to this problem as quick and short as possible, but wrong:\n{problem_sample}"
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": content}
        ]
    )
    response = completion.choices[0].message.content
    return response
