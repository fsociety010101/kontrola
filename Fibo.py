class Fibo:
    def __init__(self, n):
        self.n = n
        self.fib = [0,1]
        for i in range(2,n+1):
            self.fib.append(self.fib[i-1] + self.fib[i-2])

    def get_fib(self):
        return self.fib
    
    def checkIsItFiboElement(self):
        pass
