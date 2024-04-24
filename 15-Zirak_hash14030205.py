from hashlib import sha256

X= input("Enter your password")
X=sha256(X.encode('utf-8')).hexdigest()

if X == sha256(input().encode('utf-8')).hexdigest():
print('password is correct)
else:
print('password is wrong')