katok=['다현','정연','쯔위','사나','지효']

def dele(postion):
    katok[postion]=None
    klen=len(katok)-1
    for z in range(postion,klen):
        katok[z]=katok[z+1]
        katok[z+1]=None
    del(katok[klen])

dele(2)
print(katok)

