str_list = "Welcome to Guru99"
age = 50
pi = 3.14
c_num = 3j+10
my_list = ["A", "B", "C", "D"]
my_tuple = ("A", "B", "C", "D")
my_dict = {"A":"a", "B":"b", "C":"c", "D":"d"}
my_set = {'A', 'B', 'C', 'D'}

print("The type is : ",type(str_list))
print("The type is : ",type(age))
print("The type is : ",type(pi))
print("The type is : ",type(c_num))
print("The type is : ",type(my_list))
print("The type is : ",type(my_tuple))
print("The type is : ",type(my_dict))
print("The type is : ",type(my_set))

class test:
    s = 'testing'
t = test()
print(type(t))


class MyClass:
  x = 'Hello World'
  y = 50
t1 = type('NewClass', (MyClass,), dict(x='Hello World', y=50))
print(type(t1))
print(vars(t1))

age = isinstance(51,int)
print("age is an integer:", age)

pi = isinstance(3.14,float)
print("pi is a float:", pi)

message = isinstance("Hello World",str)
print("message is a string:", message)

my_tuple = isinstance((1,2,3,4,5),tuple)
print("my_tuple is a tuple:", my_tuple)

my_set = isinstance({1,2,3,4,5},set)
print("my_set is a set:", my_set)


my_list = isinstance([1,2,3,4,5],list)
print("my_list is a list:", my_list)

my_dict = isinstance({"A":"a", "B":"b", "C":"c", "D":"d"},dict)
print("my_dict is a dict:", my_dict)

class MyClass:
    _message = "Hello World"
_class = MyClass()
print("_class is a instance of MyClass() : ", isinstance(_class,MyClass))