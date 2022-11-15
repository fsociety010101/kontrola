class Fibo:
    def __init__(self, n):
        self.fib_num = self.fibo_rec(n)

    # fibonacci recursive   
    def fibo_rec(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibo_rec(n-1) + self.fibo_rec(n-2)

    def get_fib(self):
        return self.fib_num

a = Fibo(10)
print(a.get_fib())

