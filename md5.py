import hashlib as hl

s = input()
hash_obj = hl.md5(s.encode())
output = hash_obj.hexdigest()    # to display the code in hexadecimal format
print(output)