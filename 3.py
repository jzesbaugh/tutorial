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
		return pay1
	else:
		pay2 = h * p
		return pay2


print computepay()

grade = 0.5

try:
	gpa = raw_input("Enter GPA beten 0.0 and 1.0: ")
	grade = float(gpa)
	if grade < 0.0:
		print "bad score"
		quit()
	if grade > 1.0:
		print "bad score"
		quit()
			
except:
	print "Bad Input"
	quit()
	
if grade >= 0.9:
	print "Grade is A"
elif grade >= 0.8:
	print "Grade is B"
elif grade >= 0.7:
	print "Grade is C"
elif grade >= 0.6:
	print "Grade is D"
else:
	print "Fail"	
	






# This does not work
# python ./first py to run this in terminal
# use CD and Ls commands to navigate

