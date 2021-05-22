from abc import ABC,abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

class B(A):

    def fun1(self):
        print("function 1 called")
o = B()
o.fun1()

# Output  =  Error  TypeError: Can't instantiate abstract class A with abstract methods fun1, fun2