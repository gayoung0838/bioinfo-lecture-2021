#!/usr/bin/python3

f = open("read_sample.txt", "r")
res = f.readlines()
print(res)
f.close()

print("-" * 10)

with open("read_sample.txt", "r") as handle:
	res = handle.readlines()
	print(res)

print("-----")

with open("read_sample.txt", "r") as f:
	for line in f:
		print(line.strip())
