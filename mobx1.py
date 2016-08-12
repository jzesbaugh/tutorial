fname = raw_input("Enter file name: ")
try:
    fh = open(fname)     
except:
    print 'file cannot be opened', fname
    quit()
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    elif line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        dice = line.find('0')
        tot = line[dice - 1:26]
        tot = float(tot)
        total = total + tot
	
gtotal = total / count
print 'Average Spam Confidence', gtotal