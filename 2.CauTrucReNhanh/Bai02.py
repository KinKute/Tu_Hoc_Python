from random import randint

print('Trò chơi đoán số')
nguoiChoi = input('Mời bạn chọn cấp độ (dễ, trung bình, khó): ')

if nguoiChoi == 'dễ':
    mayTinh = int(randint(1, 2))
    nguoiChoi = input('Nhập số mà bạn đoán (1 - 2): ')

    if int(mayTinh) == int(nguoiChoi):
        print('Hai bạn hòa')

    if int(mayTinh) < int(nguoiChoi):
        print('Bạn thắng')

    if int(mayTinh) > int(nguoiChoi):
        print('Máy thắng')

if nguoiChoi == 'thường':
    mayTinh = int(randint(1, 10))
    nguoiChoi = input('Nhập số mà bạn đoán (1 - 10): ')

    if int(mayTinh) == int(nguoiChoi):
        print('Hai bạn hòa')

    if int(mayTinh) < int(nguoiChoi):
        print('Bạn thắng')

    if int(mayTinh) > int(nguoiChoi):
        print('Máy thắng')

if nguoiChoi == 'khó':
    mayTinh = int(randint(1, 100))
    nguoiChoi = input('Nhập số mà bạn đoán (1 - 100): ')

    if int(mayTinh) == int(nguoiChoi):
        print('Hai bạn hòa')

    if int(mayTinh) < int(nguoiChoi):
        print('Bạn thắng')

    if int(mayTinh) > int(nguoiChoi):
        print('Máy thắng')

print('Máy tính chọn: ', int(mayTinh))