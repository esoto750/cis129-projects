print('number of coffee')
A = input('')
print('number of muffins')
B = input('')
print('number of biscuts')
F = input('')
print('number of pastrys')
E = input('') 
C = int(A)*5
D = int(B)*4
Bis = int(F)*2
Pas = int(E)*3
T = 0.06*(C+D+Bis+Pas)
L = C+D+Bis+Pas+T
print('**********')
print('Muffins and stuff')
print(A,'Coffee at 5$ each:$', C)
print(B,'Muffins at $4 each:$', D)
print(F,'biscuts at $2 each:$',Bis)
print(E,'pastrys at $3 each:$',Pas)
print('6% tax:$', T)
print('-------')
print('Total $',L)
print('**********')
print('Thank you for your purchase please come again')
