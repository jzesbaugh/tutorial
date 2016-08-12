n = 10
while n > 0:
    print n
# if the condition does not change in a way the ends the loop it will never end, in this case a plus would create an infinite look 
    n = n - 1
    if n == 1:
# break essentially renders the condition false    
        break
print "1"
print "blast off!"


# while is a conditional statement true or false, it continues until a fales or break occurs.
while True:
    line = raw_input('> ')
# the look would be infinite if not for the break condition.
    if line == 'done':
        break
    if len(line) < 1:    # enter exits the program
            break
    print line
print "done"   
 
while True:
    line = raw_input('> ')
    if len(line) < 1:    # enter exits the program
        break
# remember that the [0] indicates a place on the list or string.    
    if line[0] == '#' :
# continue is like skip, continue is skip, so we are asking python to ignore # in the zero position of any text.    
        continue
    if line == 'done':
# remember again break renders any loop false if the condition is met
        break

    print line
print "done!"       

friends = ['Joseph', 'Glenn', 'Van', 'Sally']
#for is a set number of items to go through such as a list, the variable is defined in the fore statment, for item in
#list perform X task, once its done it moves on, its a definite list
for friend in friends:
    print 'Happy New Year: ', friend
print 'done'


count = 0
# we are counting the definite list using a plus one counter
for lala in [3, 41, 21, 9, 74, 15, 199]:
    count = count + 1
    print count
print "count: ", count

# Min max Loop

# were using none since it will be defined later in the loop
largest = None
smallest = None
print "before ", largest, smallest
for lulu in [3, 41, 21, 9, 74, 15, 199]:
# since we have used none we have to account for it
    if largest is None or lulu > largest:
        largest = lulu
    if smallest is None or lulu < smallest:
        smallest = lulu
    print "loop: ", lulu, largest, smallest
print "Largest: ", largest, "Smallest", smallest




# 5.1
total = 0
count = 0
while True:
    try:
        linex = raw_input("Enter Number: ")
        
# Handle Cases
        if linex == "done":
            break
        if len(linex) < 1:    # enter exits the program
            break
        elif linex[0] == "#" :   # allows for ghost input for whatever reason, easter egg
            continue
        
            
# do the work

        num = float(linex)
        count = count + 1
        total = total + num
    except:
        print "bad input"
print total, count, total/count


# 5.2
largestx = None
smallestx = None
while True:
    try:
        liney = raw_input("Enter Number: ")
            
        if liney == 'done':
            break
        if len(liney) < 1:
            break
        if liney[0] == "#" :
            continue
                
        num = int(liney)
        if smallestx is None or num < smallestx:
            smallestx = num
        if largestx is None or num > largestx:
            largestx = num
        
    except:
        print "bad input"
print largestx, smallestx
