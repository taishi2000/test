dict={}
w1=[]
w2=[]

with open("input.txt","r") as file:
    for i in file.read().splitlines():
        w=i.split(':')
        w1.append(w[0])
        if len(w)==2:
            w2.append(w[1])
        else:
            w3=w[0]

dict.update(zip(w1, w2))
dict2 = sorted(dict.items())
f=True
for i in range(len(dict2)):
    if int(w3)%int(dict2[0][0])==0:
        print(dict2[i][1])
        f=False

if f :
    print(w3)
