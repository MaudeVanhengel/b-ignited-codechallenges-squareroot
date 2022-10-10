from square import squareroot

given_number = int(input("Enter a number: "))

try: 
    result = squareroot(given_number)
    print("The square root of %d is %.5f" %(given_number, result))
except Exception as e:
    print(e)
