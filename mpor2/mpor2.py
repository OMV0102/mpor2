from cvxopt.modeling import op
from cvxopt.modeling import variable
import numpy as np
import matplotlib.pyplot as plt

#################################
# Начальные условия и ограничения
#################################
# вектор решения
x = variable(20, 'x')
# ограничения по заводам
limit1 = (x[0] + x[1] +x[2] + x[3] + x[4] <= 4)
limit2 = (x[5] + x[6] +x[7] + x[8] + x[9] <= 6)
limit3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 10)
limit4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 10)
# ограничения по хранилищам
limit5 = (x[0] + x[5] + x[10] + x[15] == 7)
limit6 = (x[1] + x[6] + x[11] + x[16] == 7)
limit7 = (x[2] + x[7] + x[12] + x[17] == 7)
limit8 = (x[3] + x[8] + x[13] + x[18] == 7)
limit9 = (x[4] + x[9] + x[14] + x[19] == 2)
# ограничения на неотрицательность
x_positive = (x >= 0)

####################################################
# Решение задачи по стоимости перевозки (Критерий 1)
####################################################

c1 = [160,300,170,100,160,
    300,270,260,90,230,
    130,40,220,30,100,
    30, 100,50,40,240]

z1 = (c1[0]*x[0] + c1[1]*x[1] +c1[2]* x[2] +c1[3]*x[3] + c1[4]*x[4] + 
    c1[5]* x[5] + c1[6]*x[6] +c1[7]*x[7] +c1[8]*x[8] + c1[9]*x[9] +
    c1[10]*x[10] + c1[11]*x[11] + c1[12]*x[12] + c1[13]*x[13] + c1[14]*x[14] + 
    c1[15]*x[15] + c1[16]*x[16] + c1[17]*x[17] + c1[18]*x[18] + c1[19]*x[19])


problem1 = op(z1,[limit1, limit2, limit3, limit4, limit5, limit6, limit7, limit8, limit9, x_positive])
problem1.solve(solver = 'glpk')
problem1.status
print("Результат:")
print(x.value)
print("Стоимость доставки:")
s1 = problem1.objective.value()[0]
print(s1, "\n")

##################################################
# Решение задачи по времени перевозки (Критерий 2)
##################################################

c2 = [3,5,1,8,2,
    4,5,3,7,2,
    4,9,3,6,4,
    1,2,1,5,7]

z2 = (c2[0]*x[0] + c2[1]*x[1] +c2[2]* x[2] +c2[3]*x[3] + c2[4]*x[4] + 
    c2[5]* x[5] + c2[6]*x[6] +c2[7]*x[7] +c2[8]*x[8] + c2[9]*x[9] +
    c2[10]*x[10] + c2[11]*x[11] + c2[12]*x[12] + c2[13]*x[13] + c2[14]*x[14] + 
    c2[15]*x[15] + c2[16]*x[16] + c2[17]*x[17] + c2[18]*x[18] + c2[19]*x[19])

problem2 = op(z2,[limit1, limit2, limit3, limit4, limit5, limit6, limit7, limit8, limit9, x_positive])
problem2.solve(solver = 'glpk')
problem2.status
print("Результат:")
print(x.value)
print("Время доставки:")
s2 = problem2.objective.value()[0]
print(s2, '\n')

#######################################################
# Решение задачи по стоимости и времени (оба критерия)
#######################################################

w = [0.0,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
w_ = w[5]

z3 = ( (w_*(s1+z1)/s1) + ((1.0-w_)*(s2+z2)/s2) )

problem3 = op(z3,[limit1, limit2, limit3, limit4, limit5, limit6, limit7, limit8, limit9, x_positive])
problem3.solve(solver = 'glpk')
problem3.status
print("Результат:")
print(x.value)
print("ИТОГ:")
s3 = problem3.objective.value()[0]
print(s3, "\n")


##########################################################
# Подстановка вектора X, найденного при совместном решении
##########################################################
#считаются F1 и F2 каждая от общего вектора X
z1_x = 0.0
z2_x = 0.0
for i in range(0,20):
    z1_x += (c1[i] * x.value[i])
    z2_x += (c2[i] * x.value[i])

#print('z1(x) = ', z1_x)
#print('z2(x) = ', z2_x)


##########################################
# Генерация случайного X
# График с точка
# Нахождение парето-оптимального множества
##########################################

N = 20
Count = 0


#r = [0.0, 0.0, 4.0, 0.0, 0.0,
#     0.0, 0.0, 0.0, 6.0, 0.0,
#     0.0, 7.0, 0.0, 1.0, 2.0,
#     7.0, 0.0, 3.0, 0.0, 0.0]

r = [0.0, 0.0, 4.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 6.0, 0.0,
     0.0, 7.0, 0.0, 1.0, 2.0,
     7.0, 0.0, 3.0, 0.0, 0.0]

rand = 0
flag = True
# генерируем 20 значений (вектор X)

print('\nВектор X =\n', r, '\n')

check1 = False
check2 = False
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False
check8 = False
check9 = False
check10 = True

#Проверка вектора на ограничение
if ((r[0] + r[1] + r[2] + r[3] + r[4]) <= 4):
    check1 = True
if ((r[5] + r[6] +r[7] + r[8] + r[9]) <= 6):
    check2 = True
if ((r[10] + r[11] + r[12] + r[13] + r[14]) <= 10):
    check3 = True
if ((r[15] + r[16] + r[17] + r[18] + r[19]) <= 10):
    check4 = True
if ((r[0] + r[5] + r[10] + r[15]) == 7):
    check5 = True
if ((r[1] + r[6] + r[11] + r[16]) == 7):
    check6 = True
if ((r[2] + r[7] + r[12] + r[17]) == 7):
    check7 = True
if ((r[3] + r[8] + r[13] + r[18]) == 7):
    check8 = True
if ((r[4] + r[9] + r[14] + r[19]) == 2):
    check9 = True
for i in range(0,20):
    if(r[i] < 0):
        check10 = False

if (check1 and check2 and check3 and check4 and check5 
    and check6 and check7 and check8 and check9 and check10):
    print('Проверка вектора на ограничение = ПРОВЕРКА ПРОШЛА")
else:
    print('lim_check =', lim_check)



#######################################



matr = [[],[],[],[],[]]
ij = 0
for i in range(4):
    for j in range(5):
        matr[i].append(r[ij])
        ij += 1

#print(matr[0][3])
#########################################

#####################################################################################
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import numpy as np
x = np.linspace(0, 10, 11)
y1 = 4*x

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("График", fontsize=16)
ax.set_xlabel("F1(x)", fontsize=14)        
ax.set_ylabel("F2(x)", fontsize=14)
ax.grid(which="major", color="black", linewidth=1.0)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

#ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)
ax.scatter(x, y1, c="red", label="y1 = 4*x")
#plt.show()
