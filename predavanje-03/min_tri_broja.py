x=int(input('Unesi broj x '))

z=x%10
s=(x/10)%10
p=x/100
if z > s and z > p:
   print("korijen od z")
elif s > z and s > p:
   print("korijen od s")
else:
    print("korijen od p")