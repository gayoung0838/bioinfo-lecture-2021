#!/usr/bin/python

data = dict()

with open("covid19.fasta", "r") as handle:
	for line in handle:
		if line.startswith(">"):
			continue
	for base in line.strip():
		if base not in data:
			data[base] = 0
		data[base] += 1

print(f"A: {data['A']}")
print(f"C: {data['C']}")
print(f"G: {data['G']}")
print(f"T: {data['T']}")
print(data)
