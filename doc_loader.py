import os
import tempfile
from langchain_community.document_loaders import TextLoader
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def load_text_file():
    # 1.create text file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(
            b"Hello, this is a sample text file.\nThis file is used to demonstrate the TextLoader."
        )
        temp_file_path = temp_file.name

    # 2. Load the text file using TextLoader

    try:
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        print(f"Loaded {len(documents)} document(s) \n")
        print(f"Content preview: {documents[0].page_content[:100]}... \n")
        print(f"Metadata: {documents[0].metadata} \n")

        # Print the loaded documents
        for doc in documents:
            print("Document Content:")
            print(doc)
            print(doc.page_content)
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)



def main():
    load_text_file()
    
if __name__ == "__main__":
    main()
    