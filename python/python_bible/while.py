number = 1
while(number <= 10):
    print(number)
    number += 1

L = []
while len(L) <= 3:
    name = input("Enter a name into list :")
    L.append(name)
print("\n\nThe list is full !!! \n\nNames are {}".format(L))