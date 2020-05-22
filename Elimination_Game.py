a=['Dannial','Rose','Nancy','Trisha','John','Chris']
print(a)
n=1
b=[]
while n<=6:
    v=input('enter the 1st compititor name :')
    if v in a:
        b.append(v)
    else:
        print('invalid enter again')
        continue
    while True:
        v1=input('enter the 2nd compititor name :')
        if v1 in a:
            b.append(v1)
            break
        else:
            print('invalid enter again')
            continue
    n=n+1
print(b)
x=b.count('Dannial')
y=b.count('Rose')
z=b.count('Nancy')
p=b.count('Trisha')
q=b.count('John')
r=b.count('Chris')
if x>y and x>z and x>p and x>q and x>r:
    print('eliminated: Dannial')
if y>x and y>z and y>p and y>q and y>r:
    print('eliminated: Rose')
if z>x and z>y and z>p and z>q and z>r:
    print('eliminated:Nancy ')    
if p>x and p>y and p>z and p>q and p>r:
    print('eliminated:Trisha')  
if q>x and q>y and q>z and q>p and q>r:
    print('eliminated: John') 
if r>x and r>y and r>z and r>p and r>q:
    print('eliminated: Chris')    
    
