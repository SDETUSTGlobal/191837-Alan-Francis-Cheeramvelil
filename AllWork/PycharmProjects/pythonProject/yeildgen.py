def testyield():
  yield "Welcome to Python "
output = testyield()
print(output)

#UsingGeneratorfunction


def generator():
  yield "H"
  yield "E"
  yield "L"
  yield "L"
  yield "O"


test = generator()
for i in test:
  print(i)

#--------------------------------------------------------------------------
#DifferencebetweenNormalfunctionv / sGeneratorfunction.


# Normal function
def normal_test():
  return "Hello World"


# Generator function
def generator_test():
  yield "Hello World"


print(normal_test())  # call to normal function
print(generator_test())  # call to generator function

#-------------------------------------------------------------------------------------

#How to read the values from the generator?

#Using: list()


def even_numbers(n):
  for x in range(n):
    if (x % 2 == 0):
      yield x


num = even_numbers(10)
print(list(num))

#--------------------------------------------------------------
#Using:for - in
def even_numbers(n):
    for x in range(n):
      if (x % 2 == 0):
        yield x
num = even_numbers(10)
for i in num:
  print(i)

#-----------------------------------------------------

#Using next()


def even_numbers(n):
  for x in range(n):
    if (x % 2 == 0):
      yield x


num = even_numbers(10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

#-------------------------------------------------------------



def even_numbers(n):
  for x in range(n):
    if (x % 2 == 0):
      yield x


num = even_numbers(10)
for i in num:
  print(i)

print("\n")
print("Calling the generator again: ", list(num))

#-------------------------------------------------------------------

#Example: Generatorsandyieldfor Fibonacci Series


def getFibonnaciSeries(num):
  c1, c2 = 0, 1
  count = 0
  while count < num:
    yield c1
    c3 = c1 + c2
    c1 = c2
    c2 = c3
    count += 1


fin = getFibonnaciSeries(7)
print(fin)
for i in fin:
  print(i)

#-------------------------------------------------------------------------

#Example: CallingFunctionwith Yield


def test(n):
  return n * n


def getSquare(n):
  for i in range(n):
    yield test(i)


sq = getSquare(10)
for i in sq:
  print(i)


