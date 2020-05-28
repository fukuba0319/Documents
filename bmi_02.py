weight = input('体重(kg)を入力:')
height = input('身長(cm)を入力:')
weight = float(weight)
height = float(height) / 100
bmi = weight / (height**2)
print(bmi)
