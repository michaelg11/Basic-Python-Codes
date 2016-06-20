import re
fname=open('actual_data.txt')
sum=0
for line in fname:
	line.rstrip()
	num=re.findall('[0-9]+',line)
	if len(num)>0:
		for item in num:
			sum+=int(item)

print sum