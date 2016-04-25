

fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
mail = list()
counts = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if not line.startswith('From '): continue
    email = words[1]
    counts[email] = counts.get(mail,0)+1

bigcount = None
bigname = None
for words,emails in counts.items():
    if bigcount is None or count>bigcount:
        bigname=email
        bigcount=count
print bigname, bigcount
