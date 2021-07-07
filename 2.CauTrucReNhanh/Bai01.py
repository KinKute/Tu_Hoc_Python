import math
a = input('Nhập hệ số a: ')
b = input('Nhập hệ số b: ')
c = input('Nhập hệ số c: ')
denta = pow(int(b),2) - (4 * int(a) * int(c))

if denta < 0:
    print('Phương trình vô nghiệm')
if denta == 0:
    print('Phương trình có nghiệm kép')
    kq = (-(int(b))/2(int(a)))
    print('x1 = x2 = ', kq)
if denta > 0:
    print('Phương trình có 2 nghiệm phân biệt')
    kq1 = (-(int(b) + math.sqrt(int(denta)))/ (2 * int(a)))
    kq2 = (-(int(b) - math.sqrt(int(denta)))/ (2 * int(a)))
    print("x1 = ", float(kq1))
    print('x2 = ', float(kq2))
