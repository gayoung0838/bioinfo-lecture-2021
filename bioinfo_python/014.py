#!/usr/bin/python3

s = input("입력: ")
print(type(s))

if s.isalpha():
	print(f"{s}는 문자")
else:
	print(f"{s}는 숫자")
