## 함수 선언부
def isStackFull():
    global size, stack,top
    if top>=size-1:
        return True
    else:
        return False

def isStackEmpty():
    global size, stack,top
    if top<=-1:
        return True
    else:
        return False



def push(data):
    global size, stack,top
    if isStackFull():
        print("스택 꽉참")
        return
    top += 1
    stack[top]=data

def pop():
    global size, stack,top
    if isStackEmpty():
        print("스택없다")
        return
    data=stack[top]
    stack[top]=None
    top-=1
    return data


## 전역 선언부
size=5
stack = [ None for _ in range(5)]
top = -1



## 메인 코드부

if __name__=='__main__':
    push('A')
    push('B')
    push('C')
    print(pop())
    print(pop())
    print(pop())
