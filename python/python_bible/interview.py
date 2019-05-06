class Summarizer(object):

    def __init__(self):
        self.sum = 0
        self.counter = 0

    def add(self, a):
        self.counter = self.counter + 1
        self.sum = self.sum + a
        return (self.sum)

    def getMean(self):
        return (self.sum/self.counter)



if __name__ == "__main__":
    # Test implementation

    s = Summarizer()

    s.add(5)
    s.add(7)
    s.add(9)
    print(s.getMean())