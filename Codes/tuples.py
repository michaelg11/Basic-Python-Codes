fhand=raw_input('Enter file name:')
if(len(fhand))<1:
	fhand='words.txt'
fname=open(fhand)
counts=dict()
for line in fname:
	words=line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1

lst=list()
for key, val in counts.items():
	lst.append( (val,key) )
	
lst.sort(reverse=True)

for val,key in lst[:10]:
	print key,val
