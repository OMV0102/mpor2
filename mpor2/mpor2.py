
from cvxopt.modeling import op
from cvxopt.modeling import variable
x = variable(20, 'x')
c = [160,300,170,100,160,
    300,270,260,90,230,
    130,40,220,30,100,
    30, 100,50,40,240]

z1 = (c[0]*x[0] + c[1]*x[1] +c[2]* x[2] +c[3]*x[3] + c[4]*x[4] + 
    c[5]* x[5] + c[6]*x[6] +c[7]*x[7] +c[8]*x[8] + c[9]*x[9] +
    c[10]*x[10] + c[11]*x[11] + c[12]*x[12] + c[13]*x[13] + c[14]*x[14] + 
    c[15]*x[15] + c[16]*x[16] + c[17]*x[17] + c[18]*x[18] + c[19]*x[19])

mass1 = (x[0] + x[1] +x[2] + x[3] + x[4] <= 4)
mass2 = (x[5] + x[6] +x[7] +x[8] +x[9] <= 6)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 10)
mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 10)

mass5 = (x[0] + x[5] + x[10] + x[15] == 7)
mass6 = (x[1] +x[6] + x[11] + x[16] == 7)
mass7 = (x[2] + x[7] + x[12] + x[17] == 7)
mass8 = (x[3] + x[8] + x[13] + x[18] == 7)
mass9 = (x[4] + x[9] + x[14] + x[19] == 2)

x_non_negative = (x >= 0)
problem =op(z1,[mass1,mass2,mass3,mass4 ,mass5,mass6, mass7, mass8, mass9, x_non_negative])
problem.solve(solver='glpk')
problem.status
print("Результат:")
print(x.value)
print("Стоимость доставки:")
print(problem.objective.value()[0])