# from langchain.document_loaders.pdf import UnstructuredPDFLoader
from langchain.document_loaders import PyPDFDirectoryLoader

# def readFile(filePath: str):
#     loader = UnstructuredPDFLoader(filePath, mode="elements", strategy="fast")
#     ret = loader.loads()
#     print(ret)
#     return ret

def loadDocumentsInDir(dirPath: str):
    loader = PyPDFDirectoryLoader(dirPath)
    documents = loader.load()
    return documents