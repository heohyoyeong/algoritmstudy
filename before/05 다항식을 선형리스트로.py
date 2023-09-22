 ## 함수 선언부
def printPoly(p_x):
    term=len(p_x)-1 #최고차항
    polyStr="P(x) ="
    for i in range(len(p_x)):
        coef=p_x[i]#계수
        if (coef >=0):
            polyStr +="+"
        polyStr+=str(coef)+'x^'+str(term)+ ''
        term-=1
    return polyStr

def calcPoly(xVal,p_x):
    retVal=0
    term = len(p_x) - 1
    for i in range(len(p_x)):
        coef = p_x[i]  # 계수
        retVal += coef*xVal**term
        term-=1
    return retVal

 ## 전역 변수부
px=[7,-4,0,5]



 ## 메인 코드부

pStr=printPoly(px)
print(pStr)

xValue=int(input('X값 =>'))
pxValue=calcPoly(xValue,px)
print(pxValue)