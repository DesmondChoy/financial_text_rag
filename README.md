# Financial Text RAG

The Jupyter notebook in /scripts showcases a project where Retrieval Augmented Generation (RAG) is used to query financial text documents (OCBC credit reports).

It's split into the following parts:
* Loading libraries and initializing LLM (OpenAI's GPT-4)
* Selecting an appropriate text splitter
* Loading all PDFs then splitting them into chunks
* Using OpenAI word embeddings
* Initializing Vectorstore (Chroma)
* Comparing different retrieval methods
* Asking questions and using different chain methods to retrieve answers 
