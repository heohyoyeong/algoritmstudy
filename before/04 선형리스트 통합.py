## 함수 및 클래서 선언부

def add_data(friend):
    katok.append(None)  # 빈칸추가
    kLEN = len(katok)  # 배열크기
    katok[kLEN - 1] = friend  # 친구를 선형리스트에 추가


def inser_data(postion, friend):
    # position이 선형리스트의 범위에 있나?
    katok.append(None)
    klen = len(katok)
    # 칸 이동
    for i in range(klen - 1, postion, -1):
        katok[i] = katok[i - 1]
        katok[i - 1] = None
    katok[postion] = friend


def dele(postion):
    katok[postion] = None
    klen = len(katok) - 1
    for z in range(postion, klen):
        katok[z] = katok[z + 1]
        katok[z + 1] = None
    del (katok[klen])

## 전역 변수부


katok=[]

## 메인 코드부


if __name__ == '__main__':
    add_data('다현')
    add_data('정현')
    add_data('쯔위')
    print(katok)
    inser_data(2, '화사')
    print(katok)
    dele(2)
    print(katok)


