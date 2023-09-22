katok=['1','2','3','4']

def inser_data(postion,friend):
    # position이 선형리스트의 범위에 있나?
    katok.append(None)
    klen=len(katok)
    # 칸 이동
    for i in range(klen-1,postion,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None

    katok[postion]=friend

inser_data(2,'우히히')
print(katok)