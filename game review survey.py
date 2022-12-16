name = input('''Type the name of the game
''')


finalscore = 1

a = input('''Graphics
(S) Real life
(A) Excellent
(B) Good
(C) Decent
(D) ms paint
''')

b = input('''Gameplay
(S) Better than real life
(A) Excellent
(B) Good
(C) Decent
(D) watch paint dry
''')

c = input('''Difficulty
(S) Perfectly balanced
(A) Balanced
(B) Hard/Easy
(C) Cuphead
(D) press w
''')

d = input('''Length
(S) Perfect
(A) A bit long
(B) A bit short
(C) TOO LONG
(D) downloading time was longer than the game
''')

e = input('''System requirement
(S) potato
(A) toaster
(B) school laptop
(C) decent gaming pc
(D) give your pc back to nasa
''')

f= input('''Bugs and glitches
(S) None
(A) None that i can find
(B) Pretty rare
(C) Kind of common
(D) too buggy, needs to be returned
''')

if a.lower() == 's':
  finalscore += 2

elif a.lower() == 'a':
  finalscore += 1.5

elif a.lower() == 'b':
  finalscore += 1

elif a.lower() == 'c':
  finalscore -= 0.5

elif a.lower() == 'd':
  finalscore -= 1



if b.lower() == 's':
  finalscore += 2

elif b.lower() == 'a':
  finalscore += 1.5

elif b.lower() == 'b':
  finalscore += 1

elif b.lower() == 'c':
  finalscore -= 0.5

elif b.lower() == 'd':
  finalscore  -= 1



if c.lower() == 's':
  finalscore += 2

elif c.lower() == 'a':
  finalscore += 1.5

elif c.lower() == 'b':
  finalscore += 1

elif c.lower() == 'c':
  finalscore -= 0.5

elif c.lower() == 'd':
  finalscore  -= 1



if d.lower() == 's':
  finalscore += 2

elif d.lower() == 'a':
  finalscore += 1.5

elif d.lower() == 'b':
  finalscore += 1

elif d.lower() == 'c':
  finalscore -= 0.5

elif d.lower() == 'd':
  finalscore -= 1



if e.lower() == 's':
  finalscore += 2

elif e.lower() == 'a':
  finalscore += 1.5

elif e.lower() == 'b':
  finalscore += 1

elif e.lower() == 'c':
  finalscore -= 0.5

elif e.lower() == 'd':
  finalscore -= 1



if f.lower() == 's':
  finalscore += 2

elif f.lower() == 'a':
  finalscore += 1.5

elif f.lower() == 'b':
  finalscore += 1

elif f.lower() == 'c':
  finalscore -= 0.5

elif f.lower() == 'd':
  finalscore -= 1


print(f'{finalscore}/10')

if finalscore >= 10:
  print('This game was made for you!')
elif finalscore <= 2:
  print('Why did you download this?')
elif finalscore == 7 or 8 or 9:
  print('It seems like you enjoy it alot!')
elif finalscore == 4 or 3:
  print('Its going to stay unplayed for a while')
else:
  print('You would rather play something else.')

print('The final score calculation may not be 100% accurate to your opinions.')
score = input('Type your own custom score!')
print(f'{score}/10 :D')

note = input('''
Add a note!
''')

input(f'''
  {name} review!
Graphics: {a.upper()} tier
Gamplay: {b.upper()} tier
Difficulty: {c.upper()} tier
Length: {d.upper()} tier
System requirements: {e.upper()} tier
Bugs and glitches: {f.upper()} tier

Calculated final score: {finalscore} ({finalscore}/10)
Their own score: {score} ({score}/10)

Special notes: '{note}'
''')

input()