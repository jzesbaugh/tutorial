# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
countx = 0
total = 0.750718518519 * 27
fptotal = float(total)

# Counter

for line in fh:
    count = count + 1
    if not line.startswith("X-DSPAM-Confidence:") :
		countx = countx + 1
		continue
		
# Extractor		
		
for linex in fh:
    if not linex.startswith("X-DSPAM-Confidence:") : continue
    print linex
    
# Calculation   
        
fcount = count - countx   
final = fptotal / fcount
# counter works fine
print fcount
print "Average spam confidence:", final