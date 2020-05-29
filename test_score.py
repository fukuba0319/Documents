r = float(input('リーディングの得点を入力:'))
l = float(input('リスニングの得点を入力:'))
w = float(input('ライティングの得点を入力:'))
ave = (r + l + w) / 3
if ave >= 40:
    print('A')
elif ave >= 30:
    print('B')
elif ave >= 20:
    print('C')
else:
    print('D')
