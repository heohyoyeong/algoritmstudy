katok=[]

def add_data(friend):
    katok.append(None) # 빈칸추가
    kLEN=len(katok) # 배열크기
    katok[kLEN-1]=friend # 친구를 선형리스트에 추가

add_data('1')
add_data('2')
add_data('3')
add_data('4')
add_data('5')
add_data('6')
add_data('7')

print(katok)
