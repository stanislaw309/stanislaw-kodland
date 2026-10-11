import random
pass_length = int(input("podaj długosc hasla"))
password = ""
letters = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,s,t,u,w,x,y,z,1,2,3,4,5,6,7,8,9,0,!,@,#,$,%,^,&,*,."]
for i in range(pass_length):
    password += random.choice(letters)
print(password)