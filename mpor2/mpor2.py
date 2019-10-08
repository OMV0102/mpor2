
from cvxopt.modeling import op
from cvxopt.modeling import variable
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
# ограничение на объем перевозок
'''limit10 = (x[0] + x[1] +x[2] + x[3] + x[4] +
          x[5] + x[6] + x[7] + x[8] + x[9] +
          x[10] + x[11] + x[12] + x[13] + x[14] + 
          x[15] + x[16] + x[17] + x[18] + x[19] <= 30)'''

#######################################################
# Решение задачи по стоимости перевозки (Критерий 1)
#######################################################

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

#######################################################
# Решение задачи по времени перевозки (Критерий 2)
#######################################################

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

z1_x = 0.0
z2_x = 0.0

for i in range(0,20):
    z1_x += (c1[i] * x.value[i])
    z2_x += (c2[i] * x.value[i])

print('z1(x) = ', z1_x)
print('z2(x) = ', z2_x)


#z = 0.0
#print('z :')
#for i in range(0,20):
#    z = (w_*(s1-x1.value[i])/s1) + ((1.0-w_)*(s2-x2.value[i])/s2)
#    print(z)

