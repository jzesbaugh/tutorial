x = "X-DSPAM-Confidence:    0.8475"
pos = x.find(':')
num = float(x[pos+1:])
final = num
print final