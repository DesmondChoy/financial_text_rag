# %%
import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
from langchain.document_loaders import PyMuPDFLoader

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
# os.environ["OPENAI_API_KEY"] = your_key_here

# %%
loader = PyMuPDFLoader("../data/sg_credit_outlook_1H2023.pdf")
pages = loader.load()


# %%
pages[2]
# %%
folder_path = "../data"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "rb") as file:
            loader = PyPDFLoader(file)
            pages = loader.load()
