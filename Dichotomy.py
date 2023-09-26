#Метод дихотомии
#f(x)=exp(0,87x)+exp(0,84x)-144sinx
import numpy as np
import math

corsim=4                       #Кол-во верных цифр в 16 системе счисления
a=0.                         #Интервал поиска минимайзера
b=3*np.pi/2
eps=0.5*1/(16**(corsim-1))                      #Погрешность
delta=eps/8
callf=0
itern=0
def form(x):
    return str(float.hex(x))[2:10]
def f(x):
    global  callf
    callf+=1
    return math.exp(0.87*x)+math.exp(0.84*x)-144*math.sin(x)

print(f"№   ЛУ         ПУ     -дельта   +дельта     ЗЛ        ЗП       Погрешность")
def dichotomy(a,b):
    global itern
    itern+=1
    #print(f"Итерация номер {callf//2+1},  значение: {str(float.hex((b+a)/2))[2:3+corsim:]}, с погрешностью {float.hex((b-a)/2)}")
    print(itern,end='  ')
    #print(form(a),form(b),end='    ',sep='    ')
    if b-a<=2*eps:
        return (b+a)/2
    else:
        c=(b+a)/2-delta
        d=(b+a)/2+delta
        f1,f2=f(c),f(d)
        print(form(a),form(c),float.hex(f1),float.hex(f2),form(d),form(b),float.hex((b-a)/2),callf,sep='    ')
        if f1<=f2:
            return dichotomy(a,d)
        else: return dichotomy(c,b)

minimayzer=dichotomy(a,b)

print('')
print(f"Минимайзер = {float.hex(minimayzer)}   в 10-тичной")
s=str(float.hex(minimayzer))
hans=s[2:3+corsim:]


print(f"Функция была вызвана {callf} раз(а)")
print(f"Минимайзер = {hans}     16-ричная с {corsim-1} верными цифрами")