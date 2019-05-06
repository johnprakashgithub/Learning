letters ="abcdefghijklmnopqrstuvwxyz"
number = 0

for letter in letters:
    number = number+1
    print("{}.  {}   {}".format(number,letter.capitalize(),letter))
type(letters[9])
daughter = letters[9]+letters[20]+letters[0]+letters[13]+letters[0]
son = letters[9]+letters[14]+letters[7]+letters[13]
wife = letters[11]+letters[8]+letters[13]+letters[3]+letters[0]
myself =letters[15]+letters[17]+letters[0]+letters[10]+letters[0]+letters[18]+letters[7]
print("\n\nMy daughter {}.".format(daughter.capitalize()))
print("\nMy son {}.".format(son.capitalize()))
print("\nMy wife {}.".format(wife.capitalize()))
print("\nMyself {}.".format(myself.capitalize()))

vowels = 0
consonant = 0
for letter in letters:
    if letter in "aeiou":
        vowels += 1
    else:
        consonant += 1
print("\n\nVowels: {}".format(vowels))
print("Consonants: {}".format(consonant))
