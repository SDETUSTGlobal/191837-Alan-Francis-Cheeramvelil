def main():
    x, y = 2, 8
    if (x < y):
        st = "x is less than y"
    print(st)


if __name__ == "__main__":
    main()

#--------------------------------------------------------------

# Example file for working with conditional statement with else
def main():
    x, y = 8, 4
    if (x < y):
        st = "x is less than y"

    else:
        st = "x is greater than y"
    print(st)
if __name__ == "__main__":
    main()
#--------------------------------------------------------------------------


# Example file for working with conditional statement with elseif
def main():
    x, y = 8, 8
    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is same as y"
    else:
        st = "x is greater than y"
    print(st)
if __name__ == "__main__":
    main()
#-------------------------------------------------------------------------------


# minium code execution
def main():
    x=10
    y=8

    if (x < y):
        st = "x is less than y"
        print(st)
    else:
        print( "x is greater than or equal to y")
if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------
# nested if
total = 100
# country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
    print("Shipping Costs $5")
else:
    print("FREE")
if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
else:
    print("FREE")
#----------------------------------------------------------------------------------------
# Switch Case Statement in Python
#function(argument)
#{
 #   switch(argument)
#{
 #   case 0:
   #         return ("This is Case Zero");

#case 1:
#return (" This is Case One")
#case 2:
#return " This is Case Two ";
#default:
#return "nothing";
#};
#};


#-----------------------------------------------------------------------------------------


def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print(SwitchExample(argument))
#---------------------------------------------------------------------------------------------
# while loop
# Example file for working with loops
x = 0
# define a while loop
while (x < 4):
    print(x)
    x = x + 1
#-----------------------------------------------------------------------------------------------
#
# Example file for working with loops
#
x = 0
# define a while loop
while(x <4):
		print (x)
		x = x+1

# Define a for loop
for x in range(2, 7):
    print(x)
#-------------------------------------------------------------------------------------------------
# For Loop
# use a for loop over a collection
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for m in Months:
    print(m)
#--------------------------------------------------------------------------------------------------
for x in range(10, 20):
    if (x == 15): break
    if (x % 2 == 0) : continue
    print(x)
#------------------------------------------------------------------------------------------------
# How to use “continue statement” in For Loop
# use a for loop over a collection
# Months = ["Jan","Feb","Mar","April","May","June"]
# for m in Months:
# print m

# use the break and continue statements
for x in range(10, 20):
    if (x == 15): break
    if (x % 5 == 0): continue
    print(x)
#-----------------------------------------------------------------
# Enumerate
# use a for loop over a collection
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months):
    print(i, m)

# use the break and continue statements

for x in range (10,20):
        if (x == 15):break
        if (x % 5 == 0) :continue
print (x)
#------------------------------------------------------------------------
#Python loop Working Code for all exercises: ::

#Code for while loop
x = 0
while (x < 4):
    print(x)
    x = x + 1

#For Loop Simple Example
x = 0
for x in range(2, 7):
    print(x)

#Use of for loop in string
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for m in (Months):
    print(m)

#Use break -statement in for loop
    for x in range(10, 20):
        if (x == 15): break
        print(x)

#Use of Continue statement in for loop
    for x in range(10, 20):
        if (x % 5 == 0): continue
        print(x)

#Code for “enumerate function” with “ for loop”
Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months): #provides a list implmentation
    print(i, m)
