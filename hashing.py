import hashlib as hl

s1 = input()

hash_obj1 = hl.md5(s1.encode())
hash_obj2 = hl.sha1(s1.encode())
hash_obj3 = hl.sha256(s1.encode())

print(hash_obj1.hexdigest())
print(hash_obj2.hexdigest())
print(hash_obj3.hexdigest())