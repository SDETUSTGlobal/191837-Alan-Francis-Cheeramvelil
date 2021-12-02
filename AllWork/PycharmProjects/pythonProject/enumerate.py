mylist = ['A', 'B', 'C', 'D']
e_list = enumerate(mylist)
print(list(e_list))

#UsingEnumerate()onalistwith startIndex
mylist = ['A', 'B', 'C', 'D']
e_list = enumerate(mylist, 2)
print(list(e_list))

#LoopingOveranEnumerateobject
mylist = ['A', 'B', 'C', 'D']
for i in enumerate(mylist):
    print(i)
    print("\n")
print("Using startIndex as 10")
for i in enumerate(mylist, 10):
    print(i)
    print("\n")

#EnumeratingaTuple
my_tuple = ("A", "B", "C", "D", "E")
for i in enumerate(my_tuple):
    print(i)

#EnumeratingaString
my_str = "Guru99 "
for i in enumerate(my_str):
    print(i)

#Enumerateadictionary
my_dict = {"a": "PHP", "b": "JAVA", "c": "PYTHON", "d": "NODEJS"}
for i in enumerate(my_dict):
    print(i)