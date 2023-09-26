#Метод золотого сечения
#f(x)=exp(0,87x)+exp(0,84x)-144sinx
import numpy as np
import math

corsim=4                   #Кол-во верных цифр в 16 системе счисления
a=0.                         #Интервал поиска минимайзера
b=3*np.pi/2
eps=0.5*1/(16**(corsim-1))                      #Погрешность
root5=math.sqrt(5)
callf=0
itern=0

def form(x):
    return str(float.hex(x))[2:10]
def f(x):
    global  callf
    callf+=1
    return math.exp(0.87*x)+math.exp(0.84*x)-144*math.sin(x)

flag=True
d=((root5-1)/2)*(b-a)+a
f1=f(d)
f2=-1

print(f"№   a        b          c       d      f1        f2       Погрешность")
def golden(a,b,c,d,flag):
    global f1,f2,itern
    itern+=1
    #print(f"Итерация номер {callf},  значение: {str(float.hex((b + a) / 2))[2:3 + corsim:]}, с погрешностью {float.hex((b - a) / 2)}")
    print(itern, end='  ')
    #print(form(a), form(b), sep='    ',end='  ')
    if b-a<=2*eps:
        print(form(a), form(b), sep='    ')
        return (b+a)/2
    else:
        if flag:
            c=((3-root5)/2)*(b-a)+a
            f2=f1
            f1=f(c)
        else:
            d=((root5-1)/2)*(b-a)+a
            f1=f2
            f2=f(d)
        print(form(a),form(c),float.hex(f1),float.hex(f2),form(d),form(b),float.hex((b-a)/2),callf,sep='    ')
        if f1<=f2:
            return golden(a,d,-1,c,True)
        else:
            return golden(c,b,d,-1,False)

minimayzer=golden(a,b,-1,d,flag)

print('')
print(f"Минимайзер = {float.hex(minimayzer)}   в 10-тичной")
s=str(float.hex(minimayzer))
hans=s[2:3+corsim:]


print(f"Функция была вызвана {callf} раз(а)")
print(f"Минимайзер = {hans}     16-ричная с {corsim-1} верными цифрами")