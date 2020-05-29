weight = float(input('体重(kg)を入力:'))
height = float(input('身長(cm)を入力:')) / 100
bmi = weight / (height**2)
print(bmi)
if bmi < 18.5:
    print('低体重')
elif bmi < 25.0:
    print('普通体重')
elif bmi < 30.0:
    print('前肥満')
else:
    print('肥満')            
