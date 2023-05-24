import hashlib

hashed_md5 = hashlib.md5()
hashed_sha256 = hashlib.sha256()
path = input("Di quale file devo generare l'hash? [incolla il percorso assoluto del file]: ")

with open(path, "rb") as f:
    c = f.read()
    hashed_md5.update(c)
    hashed_sha256.update(c)

print("Ecco qui i diversi hash:")
print(hashed_md5.name+": "+hashed_md5.hexdigest())
print(hashed_sha256.name+": "+hashed_sha256.hexdigest())
