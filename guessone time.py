import random
num=random.randint(1,10)
while True:
    try:
        ans=int(input('num'))
    except:
        print('again')
        continue
        
    if num==ans:
        print ('good')
    else:
        print('no no ')