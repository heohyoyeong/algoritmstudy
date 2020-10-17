## 함수 선언부
def isQueueFull():
    if (rear+1) % size==front:
        return True
    else:
        return False

def isQueueEmpty():
    if rear==front:
        return True
    else:
        return False

def enQueue(data):
    global size, queue, front,rear
    if isQueueFull():
        print("꽉참")
        return

    rear = (rear +1 ) % size
    queue[rear]=data



def deQueue():
    global size, queue, front, rear
    if isQueueEmpty():
        print("없음")
        return
    front+=1
    data=queue[front]
    queue[front]=None
    return data


## 전역 변수부
size= 5
queue= [None for _ in range(size)]
front= rear= 0



## 메인 코드부

enQueue('A')
print(queue)
enQueue('B')
print(queue)
enQueue('C')
print(queue)
enQueue('D')
print(queue)
enQueue('E') # 실패
print(deQueue())
enQueue('E') # 성공
print(queue)