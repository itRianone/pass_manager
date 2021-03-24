# import os; #print(os.urandom(16))
# key = b'8\xf3i^\xd5\x04\xcd^!289\x07s\xe6\xd7'
# #print(key.decode("latin-1"))
# import random
# import string
# import secrets

# def buildblock(size):
#     return ''.join(random.choice(string.ascii_letters) for _ in range(size))

# sh = secrets.token_hex(100000)
# sb = secrets.token_bytes(100000)
# su = secrets.token_urlsafe(100000)
# #print(sh)
# #print(sb)
# #print(su)
# #print(buildblock(1))    
def circle(radius):
    return '\n'.join(
        ''.join('#' if x**2 + y**2 < radius**2 else ' ' for x in range(1-radius, radius))
        for y in range(1-radius, radius)
    ) + '\n' * (radius >= 0)

print(circle(10))
print((5, 5)>(5, 5, 4))