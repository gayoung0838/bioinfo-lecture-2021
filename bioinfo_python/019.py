#!/usr/bin/python3

import sys


try:
	with open("noname.txt", "r") as handle:
		read = handle.readlines()
		print(3/0)
except FileNotFoundError:
	print("파일이 없습니다")
	sys.exit()
except ZeroDivisionError:
	print("0으로 나누었습니다")
	sys.exit()

print(read)
