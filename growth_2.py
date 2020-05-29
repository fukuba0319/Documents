prev = float(input('前期売上を入力:'))
this = float(input('今期売上を入力:'))
growth = this / prev * 100    #前期比を計算
print(growth)               #前期比を表示

#目標の達成/未達成を判定して表示する
if growth < 120:
    print('目標未達成')
else:
    print('目標達成')
