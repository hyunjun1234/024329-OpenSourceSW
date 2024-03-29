a=int(input('a: '))
b=int(input('b: '))
X=int(input('Max: '))
def func(a,b,X):
    for n in range(0, X+1, 1):
        Y=a*a*n+b
        print(f"{a}x{a}x{n} + {b} = {Y}")

func(a,b,X)