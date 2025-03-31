# SynthIOS: Intelligent Synthetic Data Pipelines

## 📝 Project Description
SynthIOS is an open-source pipeline for generating synthetic data for topic specific reasoning using powerful LLMs. It works with open-source models from the IONOS AI Model Hub, including Llama 3.1-70B, 3.3-70B, and 3.1-405B, or any other OpenAI SDK compatible Endpoint.

This repository was developed for a sprint at the PyConDE & PyData Darmstadt 2025 event. During this development sprint, participants will work on a project focused on synthetic data generation for training open-source models. The IONOS AI Model Hub is sponsoring language models for use in the sprint, providing participants with hands-on experience while equipping them with tools for synthetic data generation. 

Additionally, this project makes use of `.env` files for configuration and provides an upfront collection in Qdrant for quick access to datasets. The dataset used is a subset of "elite_personas" from [PersonaHub](https://huggingface.co/datasets/proj-persona/PersonaHub/viewer/elite_persona/), pre-uploaded to facilitate experimentation.

## 🎯 Objectives
- Develop modular function blocks for synthetic data generation.
- Provide a Jupyter Notebook as an interactive guide for pipeline customization.
- Enable free use and customization of the pipeline for different research projects.
- Offer an easy way to share generated datasets with the community (e.g., via Hugging Face).
- Foster the open-source community in the field of synthetic data generation for AI models.

## 🔎 Functional Components
![Synthetic Data Generation Pipeline](https://embraceable.ai/wp-content/uploads/2025/03/Synthetic-Data-Generation-Pipeline-en.png)
The SynthIOS pipeline consists of multiple functional blocks:
1. **Topic and Model Selection**: The user selects a specific topic and a model for generating synthetic data.
2. **Retrieving Persona Descriptions**: The pipeline fetches relevant persona descriptions and processes them.
3. **Persona Optimization**: Personas are refined and optimized.
4. **Problem Generation**: A specific problem is formulated based on the personas.
5. **Solution and Reasoning Generation**: The pipeline generates suitable solutions along with detailed reasoning.
6. **Solution Evaluation**: The generated solutions are evaluated.
7. **Storage and Export**: The final dataset is filtered, saved, and made available for use.
8. **Uploading and Sharing**: Optionally, the generated data can be shared with the community.

## 📂 Project Structure
```
.
├── SynthIOS_Notebook-Guide.ipynb      # Jupyter Notebooks for using, understanding and customizing the pipeline
├── SynthIOS.py                        # Python script for automating data generation
├── utils.py                           # utility Functions for Data-Handling & Generation
├── prompt_templates.py                # The Prompt-Templates used for generation of Reasoning Samples & Solutions
├── requirements.txt                   # Requirements to run the script and notebook
├── .env                               # Configuration file for API keys and settings
├── README.md                          # This documentation
```

## 🎓 Usage
### Requirements
- Python 3.8+
- Jupyter Notebook
- API credentials for the IONOS Model Hub
- Qdrant installed and configured
- OpenAI SDK installed

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/embraceableAI/SynthIOS.git
   cd SynthIOS
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with the necessary API credentials and configuration.
4. Start the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## 📊 Community Contribution
The generated data can be published via Hugging Face to support the development of new AI models. In the long term, we aim to collaborate further with HessianAI to train high-quality European AI models.

## 📈 Future Outlook
In addition to the continuous development of the pipeline, the following enhancements are planned:
- Support for additional model providers
- Expansion into multimodal data generation (text, images, audio)
- Integration with existing RAG frameworks for improved generation

## 🌟 Get Involved
We invite all interested developers and researchers to contribute to the optimization of SynthIOS. Submit a pull request or reach out to us for further collaboration!

## 👤 Contact
- **Project Lead**: embraceableAI
- **Community & Support**: [hf.co/embraceableAI](https://huggingface.co/embraceableAI)
- **License**: MIT License
