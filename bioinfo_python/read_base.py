#!/usr/bin/python

A = 0
C = 0
G = 0
T = 0

with open("covid19.fasta", "r") as handle:
	for line in handle:
		if line.startswith(">"):
			continue
		for base in line.strip():
			if base == "A":
				A += 1
			elif base == "C":
				C += 1
			elif base == "G":
				G += 1
			elif base == "T":
				T += 1

print(f"A: {A}")
print(f"C: {C}")
print(f"G: {G}")
print(f"T: {T}")		
