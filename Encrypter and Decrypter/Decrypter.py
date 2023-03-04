import sys

key = "3wy3T6eU6W0m1L"
true_key = sum([ord(i) for i in key])


f = open("message", "r")
file = f.read()
msg = [int(n) for n in file.split(',')]


decrypt = []
for j in msg:
    decrypt.append(chr(int(j / true_key)))

print(''.join(decrypt))
