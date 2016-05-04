#!/bin/sh
python test1.py | python test2.py | while read line
do
pdf=$(pdftotext "${line}" -f 1 -l 1 -raw - |head -n 10 )
echo  "${line}:\n${pdf}\n"
done
