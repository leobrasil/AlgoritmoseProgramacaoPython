max = 100

def func1(count):
    if count < max:
        print("contador menor que o valor de max")

def func2(count):
    max =10
    if count < max:
        print("contador menor que o valor de max local")

func1(90)
func2(90)
func1(90)