while True:
    height = input('enter height in metre: ')
    
    if  height.replace(".", "").isdigit():
        height = float(height)
        break
    else:
        height = input('invalid, enter height in metre: ')
    
while True:
    weight = input('enter weight in KG: ')
    
    if  weight.replace(".", "").isdigit():
        weight = float(weight)
        break
    else:
        weight = input('invalid, enter weight in KG: ')

print(f'your bmi is {(weight/(height ** 2))}')