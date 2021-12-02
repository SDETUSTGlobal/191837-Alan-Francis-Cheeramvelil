

for i in range(10):
    print(i, end=" ")

#------------------------------

for i in range(3, 10):
    print(i, end=" ")

#-----------------------------------

for i in range(3, 10, 2):
    print(i, end=" ")

#---------------------------------------

for i in range(1, 30, 5):
    print(i, end=" ")

#-----------------------------------------

for i in range(15, 5, -1):
    print(i, end=" ")

#---------------------------------------------

#for i in range(10.5):
  #  print(i, end=" ")

#---------------------------------------------------

arr_list = ['Mysql', 'Mongodb', 'PostgreSQL', 'Firebase']

for i in range(len(arr_list)):
    print(arr_list[i], end=" ")

#----------------------------------------------------------

print(list(range(10)))

#------------------------------------------------------

#for c in range('z'):
  #  print(c, end=" ")


#--------------------------------------------------------------


def get_alphabets(startletter, stopletter, step):
    for c in range(ord(startletter.lower()), ord(stopletter.lower()), step):
        yield chr(c)


print(list(get_alphabets("a", "h", 1)))
#---------------------------------------------------------------

for i in range(6):
        print(i)

#----------------------------------------------------------------------

startvalue = range(5)[0]
print("The first element in range is = ", startvalue)

secondvalue = range(5)[1]
print("The second element in range is = ", secondvalue)

lastvalue = range(5)[-1]
print("The first element in range is = ", lastvalue)

#---------------------------------------------------------------

print(list(range(10)))
#--------------------------


for i in range(2, 20, 2):
    print(i, end=" ")

#----------------------------------------------------

from itertools import chain

print("Merging two range into one")
frange = chain(range(10), range(10, 20, 1))
for i in frange:
    print(i, end=" ")

#-------------------------------------------------------




import numpy as np

for i in np.arange(10):
    print(i, end=" ")

#---------------------------------------------------------------------------

import numpy as np

for i in np.arange(0.5, 1.5, 0.2):
    print(i, end=" ")
