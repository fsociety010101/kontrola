import Punkt
import Fibo


print("Pierwszy feature")

print("Drugi feature")
punkt1 = Punkt.Punkt(0, 0, 0)
punkt2 = Punkt.Punkt(1, 2, 3)
print("Distance: ", punkt1.distance(punkt2))

fibo = Fibo.Fibo(13)
print(fibo.get_fib())

fibo_feature = Fibo.Fibo(10)
print(fibo_feature.get_fib())