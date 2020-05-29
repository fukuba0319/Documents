weight = float(input('体重(kg)を入力:'))
height = float(input('身長(cm)を入力:')) / 100
bmi = weight / (height**2)
if bmi < 18.5:
    print('低体重')
print(bmi)    
