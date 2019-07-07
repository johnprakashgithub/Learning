# import string

# def get_samples(sub, string):
#     samples=[]
#     length = len(string) + 1
#     for i in sub:
#         pos = string.find(i)
#         samples += [string[pos:i] for i in range(pos, length) if string[pos:i]]
#         for sample in samples:
#             sample = sample[1:]
#             if sample is i or not sample:
#                 continue
#             pos = sample.find(i)
#             length = len(sample) + 1
#             samples += [sample[pos:j] for j in range(pos, length) if sample[pos:j].startswith(i) and sample[pos:j] not in samples]
#     return samples

# def occurrences(string, sub):
#     count = start = 0
#     while True:
#         start = string.find(sub, start) + 1
#         if start > 0:
#             count+=1
#         else:
#             return count

# def get_player_points(sub, string, points=0):
#     samples = get_samples(sub, string)
#     for sample in samples:
#         points += occurrences(string, sample) 
#     return points


# def get_consonents_vowels(s):
#     vowels = 'AEIOU'
#     consonent = list(set(string.ascii_uppercase)-set(vowels))
#     vowels_str = [i for i in vowels if i in s]
#     consonents_str = [i for i in consonent if i in s]
#     return consonents_str, vowels_str

# def minion_game(string):
#     # your code goes here
#     player1 = 'Kevin'
#     player2 = 'Stuart'
#     consonents, vowels = get_consonents_vowels(string)
#     player1_pts = get_player_points(vowels, string)
#     player2_pts = get_player_points(consonents, string)
#     if player1_pts > player2_pts:
#         print("{} {}".format(player1, player1_pts))
#     elif player1 == player2_pts:
#         print("Draw")
#     else:
#         print("{} {}".format(player2, player2_pts))
def minion_game(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    a = 0
    b = 0
    for i, c in enumerate(s):
        if c in vowels:
            b += len(s) - i
        else:
            a += len(s) - i
            
    if a == b:
        print ("Draw")
    elif a > b:
        print('Stuart {}'.format(a))
    else:
        print('Kevin {}'.format(b))


if __name__ == '__main__':
    s = input()
    minion_game(s)