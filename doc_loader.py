import os
import tempfile
from collections.abc import Iterator
import httpx
from bs4 import BeautifulSoup
from pathlib import Path
from langchain_core.documents import Document
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

def load_text_file(temp_file_path):

    # create text file
    # with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
    #     temp_file.write(
    #         b"Hello, this is a sample text file.\nThis file is used to demonstrate the TextLoader."
    #     )
    #     temp_file_path = temp_file.name
   

    # 2. Load the text file using TextLoader

    try:
        # loader = TextLoader(file_path)
        # documents = loader.load()

        documents = [
            Document(
                page_content=Path(temp_file_path).read_text(encoding="utf-8"),
                metadata={"source": temp_file_path},
            )
        ]

        print(f"Loaded {len(documents)} document(s) \n")
        print(f"Content preview: {documents[0].page_content[:100]}... \n")
        print(f"Metadata: {documents[0].metadata} \n")

        # Print the loaded documents
        # for doc in documents:
        #     print("Document Content:")
        #     print(doc)
        #     print(doc.page_content)
    # finally:
         # Clean up the temporary file
         # os.remove(temp_file_path)

    except Exception as e:
        print(e)

def load_pdf_file(file_path:str):
    
    try:
        reader = PdfReader(file_path)

        documents = [
            
            Document(
                page_content=page.extract_text() or "",
                metadata={"source": file_path, "page": index},
            )
            for index, page in enumerate(reader.pages)
            
        ]
        
        print(f"Loaded {len(documents)} Document")
        for i, doc in enumerate(documents):
            print("-"*50)
            print(f"Document {i+1} and content:{doc.page_content[:100]}")
            print(doc.metadata)
            print("-"*50)
    except Exception as e:
        print(e)

def load_web_page(URL: str):
    try: 
        res = httpx.get(URL,follow_redirects=True,timeout=30)
        res.raise_for_status()
        print(res.status_code)
        soup = BeautifulSoup(res.text,"html.parser")

        for tag in soup(["script","style","noscript","footer","header"]):
            tag.decompose()
        
        documents = [
            Document(
                page_content=soup.get_text(separator="\n", strip=True),
                metadata={"source": URL},
            )
        ]

        print(f"Loaded {len(documents)} document(s) from web")
        print(f"Source: {documents[0].metadata.get('source', 'N/A')}")
        print(f"Content length: {len(documents[0].page_content)} characters")
        print(f"Preview: {documents[0].page_content[:200]}...")

    except httpx.RequestException as e:
        print(f"HTTP Request Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def load_text_directory(directory: str):
    try:
        suffex = "**/*.txt"
        for path in Path(directory).glob(suffex):
            if path.is_file():
                doc = Document(
                    page_content=path.read_text(encoding="utf-8"),
                    metadata={"source": str(path)},
                )

        for i, doc in enumerate(doc):
            print("-"*50)
            print(f"Document and content:{doc.page_content[:100]}")
            print(doc.metadata)
            print("-"*50)

    except Exception as e:
        print(e)

    try:
        suffex = "**/*.txt"
        for path in Path(directory).glob(suffex):
            if path.is_file():
                doc = Document(
                    page_content=path.read_text(encoding="utf-8"),
                    metadata={"source": str(path)},
                )

        for i, doc in enumerate(doc):
            print("-"*50)
            print(f"Document and content:{doc.page_content[:100]}")
            print(doc.metadata)
            print("-"*50)

    except Exception as e:
        print(e)

def main():
    # load_text_file()
    # load_pdf_file("./docs/Hanisha_SDE.pdf")
    load_web_page("https://openrouter.ai/docs/quickstart")
    print("loaded pdf file")
    
if __name__ == "__main__":
    main()    
