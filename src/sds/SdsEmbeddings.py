from langchain_community.embeddings.ollama import OllamaEmbeddings
# from langchain_community.embeddings.bedrock import BedrockEmbeddings

def getOllamaEmbeddings():
    embeddings = OllamaEmbeddings(model="nomic-embed-text",
                                  base_url="http://ollama:11434")
    return embeddings
