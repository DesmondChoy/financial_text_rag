# Financial Text RAG

To facilitate accurate Q&A with financial documents (OCBC credit reports), a Retrieval-Augmented Generation (RAG) approach can be used together with a LLM.  
Different retrieval methods were compared and the Maximum Marginal Relevance method was found to work best in retrieving diverse and unique results from vectorstore.  
Running a few questions to test showed encouraging answers - the LLM was pulling correct answers from relevant documents and summarizing them in a succinct manner.

Inspired by: https://learn.deeplearning.ai/langchain-chat-with-your-data/
It's split into the following parts:
* Loading libraries and initializing LLM (OpenAI's GPT-4)
* Selecting an appropriate text splitter
* Loading all PDFs then splitting them into chunks
* Using OpenAI word embeddings
* Initializing Vectorstore (Chroma)
* Comparing different retrieval methods
* Asking questions and using different chain methods to retrieve answers 

Some possible follow-up that extends beyond the scope of this project:
* Can this workflow scale? Three documents were used but how about a hundred?
* Chatbot functionality with memory and a clean interface can be built for non-technical stakeholders
* How can model performance drift be tracked for LLMs? What if quality of embeddings/results deteriorate over time?
* Can tabular data be created by specifically specifying the output? This could serve as input to ML/DL predictive models.


Inspired by: https://learn.deeplearning.ai/langchain-chat-with-your-data/
