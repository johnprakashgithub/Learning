class summerize:
    def __init__(self):
        self.sum = 0
        self.counter = 0
        print("Init: Sum : {}, Number of Additions : {}".format(self.sum,self.counter))

    def add(self, number):
        self.counter += 1
        self.sum = self.sum + number
        print(self.sum)
        return(self.sum)
    
    def mean(self):
        print("mean - Sum : {}, Number of Additions : {}".format(self.sum,self.counter))
        return(self.sum/self.counter)

if __name__ == "__main__":
    s = summerize()
    s.add(5)
    s.add(7)
    s.add(2)
    s.add(12)
    s.add(3)

    print(s.mean())