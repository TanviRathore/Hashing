import hashlib as hl
import uuid as ud

password = input()
salt = ud.uuid4().hex
hash_pswd = hl.md5((password+salt).encode()).hexdigest()
print("The password after Salting and Hashing is: ",hash_pswd)

N = int(input("Enter the number for Iterartion: "))

for i in range(N):
    hash_pswd = hl.md5((hash_pswd).encode()).hexdigest()

print("The password after {0} Iteration is: {1}".format(N,hash_pswd) )