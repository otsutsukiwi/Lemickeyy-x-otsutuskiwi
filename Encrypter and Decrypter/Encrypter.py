import sys

key = "3wy3T6eU6W0m1L"
key_list = [ord(i) for i in key]
true_key = sum(key_list)

text = "cool!"
text_list = [ord(i) for i in text]

gen_l = []
for i in text_list:
    gen_l.append(str(i * true_key))
msg = ', '.join(gen_l)

f = open("message", "w")
f.write(msg)
f.close()

# ---- Example keys! ---- #
keys = ["4td0ATxY7XAk8F", "2ul2TGpb0BTv33", "7eZ4ANuu7A3m8V", "05c8BNgj5ECg4J", "3wy3T6eU6W0m1L"]
