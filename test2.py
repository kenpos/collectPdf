# coding:UTF-8
import sys
import os

if __name__ == "__main__":
    all_lines=sys.stdin.readlines()
for line in all_lines:
    if line.find(".pdf") >= 0:
        print line[:-1]
