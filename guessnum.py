import random
num=random.randint(1,10)
i=0
while i<5:
    ans=int(input('num'))
    if num==ans:
        print ('good')
        print('you guessed', i+1, 'times')
        break
    else:
        print('no no ')
        if num >ans:
            print ('bigger')
        else:
            print ('smaller')
    i=i+1
  