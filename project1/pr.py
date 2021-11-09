import random

_phrase = [['learn', 'from', 'yesterday'], ['be', 'the', 'change'], ['do', 'your', 'best'], ['follow', 'your', 'heart'],
           ['never', 'give', 'up']]

_random_phrase = random.randint(0, 4)
ans = _phrase[_random_phrase]
print(ans)
_under = [len(word) * '_' for word in ans]
_under2 = " ".join(_under)
print(_under2)

guess = 0
score = 0

guessed_letter = input('guess the letter: ')
if not guessed_letter.isalpha():
    print('guess only a letter')
elif (len(guessed_letter)>1):
    print('guess only one letter')

while _under2 != ans:
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i[j]] == guessed_letter:
                _under2[i[j]] = ans[i[j]]
            print(i[j])
        else:
            print('you guessed a wrong letter')
guess += 1

if guess != 0:
     score += 5
else:
    score -= 1
    print(_under2)
    print(score)


