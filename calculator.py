def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))


def square(n):
    #return n * n
    return pow(n, 2)

main()


##x = float(input("What is x? "))
##y = float(input("What is y? "))
##z = x / y
##print(f"{z:.2f}")

#z = round(x / y, 2)
#print(z)
#z = round(x + y)
#print(f"{z:,}")
#print(int(input("What is x? ")) + int(input("What is y? ")))


#def square(n):
    #return n * n
# for i in range(10):
#    print(f"The square of {i} is {square(i)}")