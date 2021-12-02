
try:
    except IndexError as error:
        print("Caught first " + error.getMessage())
except IOError as error2:
print("Caught second " + error2.getMessage())

try:
    raise KeyboardInterrupt
finally:
        print ('welcome, world!')