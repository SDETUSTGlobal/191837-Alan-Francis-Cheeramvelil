from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))

from collections import Counter
my_str = "Welcome to Guru99 Tutorials!"
print(Counter(my_str))

from collections import Counter
list1 = ['x','y','z','x','x','x','y','z']
print(Counter(list1))

from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(dict1))

from collections import Counter
tuple1 = ('x','y','z','x','x','x','y','z')
print(Counter(tuple1))

from collections import Counter
print(Counter("Welcome to Python"))   #using string
print(Counter(['x','y','z','x','x','x','y', 'z'])) #using list
print(Counter({'x': 4, 'y': 2, 'z': 2})) #using dictionary
print(Counter(('x','y','z','x','x','x','y', 'z'))) #using tuple

from collections import Counter
_count = Counter()
_count.update('Welcome to Python')
print(_count)

from collections import Counter
_count = Counter()
_count.update('Welcome to Guru99 Tutorials!')
print('%s : %d' % ('u', _count['u']))
print('\n')
for char in 'Guru':
    print('%s : %d' % (char, _count[char]))

from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2}
del dict1["x"]
print(Counter(dict1))

from collections import Counter
counter1 =  Counter({'x': 4, 'y': 2, 'z': -2})
counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })
#Addition
counter3 = counter1 + counter2 # only the values that are positive will be returned.
print(counter3)
#Subtraction
counter4 = counter1 - counter2 # all -ve numbers are excluded.For example z will be z = -2-4=-6, since it is -ve value it is not shown in the output
print(counter4)
#Intersection
counter5 = counter1 & counter2 # it will give all common positive minimum values from counter1 and counter2
print(counter5)
#Union
counter6 = counter1 | counter2 # it will give positive max values from counter1 and counter2
print(counter6)

