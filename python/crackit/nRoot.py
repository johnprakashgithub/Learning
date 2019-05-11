class nRoot:
    def __init__(self,n):
        self.nthbase = float(1)/n

    def nRoot(self,number):
        print("The number {} and base {}".format(number,self.nthbase))
        return(int(float(number) ** self.nthbase))


if __name__ == "__main__":
    sqrRt = nRoot(2) # for square root
    number=input("Enter the number to find square root : ")
    print("The squareroot of {} : {}".format(number,sqrRt.nRoot(number)))

    cubeRt = nRoot(3) # for cube root
    number=input("Enter the number to find cube root : ")
    print("The cuberoot of {} : {}".format(number,cubeRt.nRoot(number)))

    fourthRt = nRoot(4) # for fourth root
    number=input("Enter the number to find fourth root : ")
    print("The fourthroot of {} : {}".format(number,fourthRt.nRoot(number)))    