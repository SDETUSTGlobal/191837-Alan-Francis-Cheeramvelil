class p1():
    def method(self):
        print("This is the 1st method of p1")

    def method(self):
        print("This is the 2nd method of p1")

class p2(p1):
    pass
    #def method(self):
        #print("This is the 1st method of p2")
    #def method(self):
        #                       print("This is the 2nd method of p2")

class p3(p2,p1):
    pass

obj=p3()
obj.method()
obj1=p2()
obj1.method()
