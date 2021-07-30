#!/usr/bin/python3

Seq1 = "ATGTTATAG"
Seq2 = ""

for i in Seq1:
	if i == 'A':
		Seq2 += 'T'
	elif i == 'C':
		Seq2 += 'G'
	elif i == 'G':
		Seq2 += 'C'
	elif i == 'T':
		Seq2 += 'A'

print(Seq1)
print(Seq2)
