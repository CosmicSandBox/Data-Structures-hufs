#최대 공약수
a=int(input('a입력'))
b=int(input('b입력'))
while a!=0 and b!=0 :
    if a>b :
        a=a-b
    else :
        b=b-a
print('최대공약수%d' %(a+b))