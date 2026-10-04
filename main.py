from importlib.metadata import version
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

print("LangChain Core:", version("langchain-core"))
print("LangGraph:", version("langgraph"))
print("LangChain OpenAI:", version("langchain-openai"))
# print("LangChain Anthropic:", version("langchain-anthropic"))
print("LangChain Google GenAI:", version("langchain-google-genai"))



def main():
    llmGPT = ChatOpenAI(model="gpt-4o-mini",temperature=0)
    res = llmGPT.invoke("Say, setup completed in One go")
    print(f"OpenAI: {res.content}")


    llmGemini = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite",temperature=0)
    res = llmGemini.invoke("Say, setup completed in One go")
    print(f"Gemini: {res}")


    print("setup complete!")

if __name__ == "__main__":
    main()
