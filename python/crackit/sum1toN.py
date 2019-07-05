class sumof1toN:
    def __init__(self):
        self.initial = 1

    def addto(self,number):
        sum=(number*(number+1))/2
        return(int(sum))

if __name__ == "__main__":
    sum1toN = sumof1toN()
    number=int(input("Enter the number to find the sum of this number from 1 : "))
    print("The sum from 1 to the number {} is {}".format(number,sum1toN.addto(number)))