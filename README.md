# Financial Text RAG

To facilitate accurate Q&A with financial documents (OCBC credit reports), we can leverage Retrieval-Augmented Generation (RAG) together with a LLM.   
This is the basic workflow: Financial text -> Split into chunks + OpenAI embeddings -> Load Vectorstore  
Ask questions -> Look up Vectorstore -> Get most relevant embeddings -> Expose to LLM -> Get relevant answer

It's split into the following parts:
* Loading libraries and initializing LLM (OpenAI's GPT-4)
* Selecting an appropriate text splitter
* Loading all PDFs then splitting them into chunks
* Using OpenAI word embeddings
* Initializing Vectorstore (Chroma)
* Comparing different retrieval methods
* Asking questions and using different chain methods to retrieve answers 

Inspired by: https://learn.deeplearning.ai/langchain-chat-with-your-data/
