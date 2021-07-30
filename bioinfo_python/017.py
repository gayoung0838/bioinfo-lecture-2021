#!/usr/bin/python3

fw = open("write_sample.txt", "w")
fw.write("MEN1\n")
fw.close()


# with open으로 파일 열어서 쓰기
with open("write_sample2.txt", "w") as write_handle:
    write_handle.write("BRCA1\n")


# with open을 파일 열어서 추가하기
with open("write_sample2.txt", "a") as write_handle:
    write_handle.write("BRCA2\n")
