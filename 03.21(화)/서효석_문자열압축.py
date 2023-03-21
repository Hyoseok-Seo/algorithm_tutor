def abrv(n,data):
    index=[-1]
    char=[]
    for i,alph in enumerate(data):
        index.append(i)
        char.append(alph)
        if (i<len(data)-n*2) and (data[i:i+n]==data[i+n:i+n*2]):
        
        

def main():
    s=input()
    for i in range(2,len(s)//2):
