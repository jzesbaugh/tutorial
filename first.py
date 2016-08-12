def computepay():
	try:
		hrs = raw_input("Enter Hours:")
		h = float(hrs)
		pay = raw_input("Enter Pay:")
		p = float(pay)
	except:
		print "Input Error, please enter numeric value"
		quit()
	if h >= 40:
		pay1 = 40 * p + (h - 40) * (p * 1.5)
		print pay1
	else:
		pay2 = h * p
		print pay2


computepay()




# This does not work
# pyton ./first py to run this in terminal
# use CD and Ls commands to navigate

