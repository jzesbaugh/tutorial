largest = None
smallest = None
while True:
        num = raw_input("Enter a number: ")
       
        if num == "done" : 
            break
        try:
            num = int(num) 
        except:  
            print "Invalid input"
            continue             
        if smallest is None:
			smallest = num
			largest = num
        elif num > largest:
			largest = num
        elif num < smallest:
           smallest = num          	

     

    

print "Maximum is", largest
print "Minimum is", smallest



# This does not work
# python ./final.py to run this in terminal
# use CD and Ls commands to navigate
