from re import A


#최대 공약수
while a!=0 and b!=0:
    if a>b : a=a-b
    else : b=b-a
return a+b