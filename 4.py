
# here we are defining a function with the def feature, the function must include (), and end in : which reminds us to indent
def computepay():
# here we are using try, which is our insurance if the float conversion does not work, the data is wrong.
	try:
		hrs = raw_input("Enter Hours:")
		h = float(hrs)
		pay = raw_input("Enter Pay:")
		p = float(pay)
# except shows us what happens if try creates and error		
	except:
		print "Input Error, please enter numeric value"
		quit()
# if is a conditional statment, if a variable meets the if condition, the code below plays out if has a :		
	if h >= 40:
		pay1 = 40 * p + (h - 40) * (p * 1.5)
		return pay1
# should the if feature not active the else feature handles the data.		
	else:
		pay2 = h * p
#return is used instead of print as it ends the conditional statment		
		return pay2

# here we are asking to print the function, which will ask for input
print computepay()

# the grader is also now a function
def grader():
	grade = 0.5
# we see our insurance again with the try statement.
	try:
		gpa = raw_input("Enter GPA beten 0.0 and 1.0: ")
		grade = float(gpa)
# we are only working in a limited range so we have some conditions the input needs to meet.		
		if grade < 0.0:
			return "bad score"
			quit()
		if grade > 1.0:
			return "bad score"
			quit()
# we also have accounted if it cannot be converted to a float		
	except:
		print "Bad Input"
		quit()
# here are the if variables again using the return rather then print functions.	
	if grade >= 0.9:
		return "A"
	elif grade >= 0.8:
		return "B"
	elif grade >= 0.7:
		return "C"
	elif grade >= 0.6:
		return "D"
	else:
		return "F"	
# we are running it a few times to debug it.	
print grader()
print grader()
print grader()




# This does not work
# python ./first py to run this in terminal
# use CD and Ls commands to navigate

