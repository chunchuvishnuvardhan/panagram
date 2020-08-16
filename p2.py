import string
str=input("enter your string")
st=str.upper()
a=string.ascii_uppercase
answer=1
for i in a:
    for j in st:
       if i in st:
           break
       else:
          answer=answer+1
          break
    if answer==2:
        print("its not a pangram")
        break
else:
    print("its a pangram")