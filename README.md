# LLM-GANs-Projects

A structured collection of notebooks and scripts covering deep learning, generative models, LLM applications, agent frameworks, and vector search.

## GANs (`GANs/`)

### Art-Portrate Generator
- Art portrait generation workflow from a Kaggle-sourced dataset (`Art_Portraits_Generator.ipynb`)
- Subject coverage: image preprocessing, training flow, generated portrait outputs

### Face Generation
- Progressive GAN face generation notebook (`(Progan)_Face_generation_with_GanAI_.ipynb`)
- Model/theme referenced: Google ProGAN (`google/progan-128`)

### MNIST generator
- Convolutional GAN for MNIST digits (`GAN_Convolution.ipynb`)
- Baseline dense GAN workflow (`generated_images/GANs_normal_network.ipynb`)
- Subject coverage: adversarial training loop, discriminator/generator dynamics, sample generation

### models
- Stable Diffusion XL image generation
  - Script + notebook: `stable-diffusion-xl-base-1.0`
  - Files: `models/Stable-Diffusion/main.py`, `stable_diffusion.ipynb`
- Z-Image-Turbo generation pipeline
  - Model: `Tongyi-MAI/Z-Image-Turbo`
  - Files: `models/Z-Image-Turbo/image-generator.py`
- FLUX image generation notebooks
  - Models: `black-forest-labs/flux-1.1-pro`, `black-forest-labs/flux-kontext-pro`
- Imagen notebook
  - Model reference: `google/imagen-4`

## LLMs (`LLMs/`)

### Code Generator
- Code synthesis notebook using Salesforce CodeGen
- Model: `Salesforce/codegen-2B-multi`

### Customer Service Chatbot
- Customer support QA chatbot notebook
- Model: `deepset/roberta-base-squad2`

### Excel Data Analyzer
- Spreadsheet question-answering and analysis notebook
- Model: `gemini-2.5-flash`

### Legal-Document-Analyzer
- Legal document summarization and analysis notebooks
- Models used/referenced:
  - `facebook/bart-large-cnn`
  - `nlpaueb/legal-bert-base-uncased`

### Short Story Generator
- Creative text generation notebook
- Model: Google Flan-T5 (`flan-t5` family)

## Lang-Graph (`Lang-Graph/`)

### codebasics_tutorial
- Chatbot graph basics (`chatbot.ipynb`)
- Conditional graph routing (`conditional_graph.ipynb`)
- Financial analysis graph (`financial_graph.ipynb`)
- Memory in graph workflows (`memory_in_langgraph.ipynb`)
- Tool-calling stock price flow (`tool_call_stock_price.ipynb`)
- Models used in notebooks:
  - `google_genai:gemini-2.0-flash`
  - `gpt-3.5-turbo`

## LangChain (`LangChain/`)

### Travel Scheduler
- Travel planning/scheduling notebook (`Travel_Scheduler_LLM.ipynb`)
- Model theme referenced in notebook: IBM Granite 3.2

### udemy_course / hello_world
- Prompt + context pipeline with LangChain chains
- Models used:
  - OpenAI `gpt-5`
  - Ollama `gemma3:270m`

### udemy_course / ReAct
- LangChain tool-calling ReAct loop (`tool_calling/1_agent_loop_langchain_tool_calling.py`)
- Raw SDK tool calling with manual tool schema (`raw_tool_calling/raw_tool_calling.py`)
- Raw prompt-only ReAct notebook (`raw_react_prompt/3_raw_react_prompt.ipynb`)
- Models used:
  - `gpt-3.5-turbo` (LangChain tool-calling config)
  - Ollama `qwen3:1.7b` (raw tool-calling and raw prompt ReAct)
- Implemented lessons:
  - Tool schema design
  - Multi-turn agent loops
  - Tool execution and observation handling
  - ReAct prompt structuring and parsing

### udemy_course / search-agent
- Search agent scaffold using external search tool integration
- Stack/models:
  - OpenAI `gpt-5`
  - Tavily search tool

## MCP (`MCP/`)

### Authentiation
- FastMCP-based HTTP server scaffold for authenticated tool access
- Implemented tools:
  - `retrieve_users_notes`
  - `add_note`
- Implemented subjects:
  - MCP server structure
  - Bearer-auth/OAuth-style scaffolding imports
  - CORS middleware setup

## Neural Networks (`Neural Networks/`)

### Tensorflow
- Neural network fundamentals notebook (`NeuralNetwork.ipynb`)
- From-scratch workflow (`from_scratch.ipynb`)
- Keras CNN notebook (`keras_CNN.ipynb`)

### PyTorch
- Differential Privacy in PyTorch (`DP_in_PyTorch.ipynb`)

### HPC-IPM
- CNN notebooks (`CNN.ipynb`, `CNNcode.ipynb`)
- Subject coverage: CNN architecture/training exercises

## SymanticSearch (`SymanticSearch/`)

- Semantic search with OpenAI embeddings + Pinecone (`Simantic_Search_OpenAI(ada3)_and_Pinecone.ipynb`)
- Text embedding pipeline with pretrained models + Pinecone (`Text_Embedding_with_Pretrained_model.ipynb`)
- Implemented subjects:
  - Embedding creation
  - Vector upsert/retrieval flow
  - Similarity-based semantic querying

## vector_database (`vector_database/`)

### chromadb
- ChromaDB crash-course notebook (`chroma_db.ipynb`)
- Implemented subjects:
  - Collection creation and management
  - Document embedding storage
  - Similarity query workflow (cosine/distance concepts)

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for full text.
