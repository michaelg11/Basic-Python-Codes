fname=raw_input('Enter file name:')
if len(fname)<1:
	fname='mbox-short.txt'
fhand=open(fname)

counts=dict()
for line in fhand:
	words=line.split()
	if line.startswith('From') and not line.startswith('From:'):
		hours=words[5]
		req=hours.split(":")
		hour=req[0]		
		counts[hour]=counts.get(hour,0)+1
			
lst=counts.items()
lst.sort()

for k,v in lst:
	print k,v
		