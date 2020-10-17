class Node():
    def __init__(self):
        self.data=None
        self.link=None


node1=Node()
node1.data='다현'

node2=Node()
node2.data='정현'
node1.link=node2

node3=Node()
node3.data='쯔위'
node2.link=node3

newNode=Node()
newNode.data='재남'
newNode.link=node2.link #정연의 손을 재남에 인계
node2.link=newNode

current=node1
print(current.data, end='-->')

while True:
    if current.link==None:
        break
    current=current.link
    print(current.data, end='-->')