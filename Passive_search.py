#Метод пассивного поиска
#f(x)=exp(0,87x)+exp(0,84x)-144sinx
import numpy as np
import math
import matplotlib.pyplot as plt

corsim=4                   #Кол-во верных цифр в 16 системе счисления
a=0                         #Интервал поиска минимайзера
b=3*np.pi/2
eps=0.5*1/(16**(corsim-1))                      #Погрешность
k=math.ceil((b-a)/eps)     #Кол-во узлов(кол-во вычислений функции)

callf=0
itern=0
minimayzer=1000
min_value=1000
def form(x):
    return str(float.hex(x))
def f(x):
    global  callf
    callf+=1
    return math.exp(0.87*x)+math.exp(0.84*x)-144*math.sin(x)

points=np.linspace(a,b,k)

for i in points:
    itern+=1
    f1=f(i)
    if f1<min_value:
        min_value=f1
        minimayzer=i
    else:
         print(itern, form(i), form(f1), sep='    ')
         break
    print(itern ,form(i) , form(f1), sep='    ')




#
# plt.text(0,10, eps, fontsize=15)
# plt.plot(points, values, color='blue', marker="*", )
# plt.legend(title=(minimayzer))
# plt.show()
# x=1.52693853
# print(f"Истинное значение = {x}")

print(f"Минимайзер = {float.hex(minimayzer)}   в 10-тичной")
s=str(float.hex(minimayzer))
hans=s[2:3+corsim:]

print(f"Погрешность = {float.hex(0.5*(b-a)/(k-1))}")
print(f"Функция была вызвана {callf} раз(а)")
print(f"Минимайзер = {hans}     16-ричная с {corsim-1} верными цифрами")