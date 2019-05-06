class MyString(object):
    def __init__(self, s):
        self.string = s

    def anyalnum(self):
        if self.anyalpha() and self.anydigit():
            return True
        return False

    def anyalpha(self):
        for c in self.string:
            if c.isalpha():
                return True
        return False

    def anydigit(self):
        for c in self.string:
            if c.isdigit():
                return True
        return False

    def anylower(self):
        for c in self.string:
            if c.islower():
                return True
        return False

    def anyupper(self):
        for c in self.string:
            if c.isupper():
                return True
        return False

    def len(self):
        return len(self.string)


if __name__ == '__main__':
    s = MyString(input())
    if 0 < s.len() < 100:
        # String contains alpha numeric
        if s.anyalnum():
            print(True)
        else:
            print(False)
        # String contains alphabets
        if s.anyalpha():
            print(True)
        else:
            print(False)
        # String contains digits
        if s.anydigit():
            print(True)
        else:
            print(False)
        # String contains lower case
        if s.anylower():
            print(True)
        else:
            print(False)
        # String contains upper case
        if s.anyupper():
            print(True)
        else:
            print(False)
