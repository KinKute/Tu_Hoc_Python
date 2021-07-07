from random import randint
nguoiChoi = input('Người chơi chọn bao - búa - kéo: ')
mayTinh = randint(0, 2)
if mayTinh == 0:
    mayTinh = 'bao'
if mayTinh == 1:
    mayTinh = 'búa'
if mayTinh == 2:
    mayTinh = 'kéo'
print('Máy tính chọn: ', mayTinh)

# if nguoiChoi == mayTinh:
#     print('2 bạn hòa')

if nguoiChoi == 'bao':
    if mayTinh == 'bao':
        print('Bạn và máy hòa nhau')
    if mayTinh == 'búa':
        print('Bạn thắng')
    if mayTinh == 'kéo':
        print('Bạn thua rồi')

if nguoiChoi == 'bua':
    if mayTinh == 'bua':
        print('Bạn và máy hòa nhau')
    if mayTinh == 'kéo':
        print('Bạn thắng')
    if mayTinh == 'bao':
        print('Bạn thua rồi')

if nguoiChoi == 'kéo':
    if mayTinh == 'kéo':
        print('Bạn và máy hòa nhau')
    if mayTinh == 'bao':
        print('Bạn thắng')
    if mayTinh == 'búa': 
        print('Bạn thua rồi')
else:
    print('Nhập sai rồi, thử lại nha!')