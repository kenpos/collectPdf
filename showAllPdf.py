import os
import sys

print os.system('pdftotext -layout -f 1 -l 1  - | head -n 4 |tail -n 2)
