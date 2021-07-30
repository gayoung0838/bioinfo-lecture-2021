
l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
d = {}

for k in l:
	if k not in d:
		d[k] = 0
	d[k] += 1

print(d)
