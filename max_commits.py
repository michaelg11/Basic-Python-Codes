fname=raw_input("Enter file name:")
if len(fname) <1:
	fname='mbox-short.txt'
handle=open(fname)

commit=dict()
for line in handle:
	if line.startswith('From') and not line.startswith('From:'):
		words=line.split()
		email=words[1]
		commit[email]=commit.get(email,0)+1

bigword=None
bigcount=None
for word,count in commit.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count
		
print bigword,bigcount
	