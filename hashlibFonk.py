import hashlib


obje1=hashlib.md5('ersin'.encode()).hexdigest()
obje2=hashlib.md5('ersin'.encode()).digest()

print(obje1)
print(obje2)
print()

obje3=hashlib.sha256('ersin'.encode()).hexdigest()
obje4=hashlib.sha256('ersin'.encode()).digest()

print(obje3)
print(obje4)