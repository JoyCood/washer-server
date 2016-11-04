import hashlib

def md5(x):
    m = hashlib.md5()
    m.update(x.encode())
    return m.hexdigest()
