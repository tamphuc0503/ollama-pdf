import hashlib

def md5(filePath:str):
    ret = hashlib.md5(open(filePath,'rb').read()).hexdigest()
    return ret