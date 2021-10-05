myfile=open("people exercise.txt","r")

for i in myfile:
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
    elif "shimla" in i:
        m=open("shimla.txt","a")
        m.write(i)
    else:
        k=open("other.txt","a")
        k.write(i)
        
myfile()