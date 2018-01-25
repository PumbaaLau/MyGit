# line_count.py
import sys

count = 0
for line in sys.stdin:
	count += 1
	
# 输出去向 sys.stdout
print(count)