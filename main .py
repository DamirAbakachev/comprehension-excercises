#regular code
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)
 
#comprehension code
   
f = [("FizzBuzz" if (i % 3 == 0 and i % 5 == 0) else "Fizz" if (i % 3 == 0) else "Buzz" if (i % 5 == 0) else i) for i in range(1,101)]

print(f)