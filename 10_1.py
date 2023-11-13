foods = {
    'pizza': 210000,
    'hamberger': 140000,
    'pasta': 220000,
    'soosis': 110000,
}
# print(foods)
a = input('what do you need?')
print(foods.get(a, f'dont have {a}'))
b = input('do you want it?')
if b == 'yes':
    foods.pop(a)
print(foods)
# print(foods['pasta2'])
# for item in foods.keys():
# for item in foods.values():
# for item in foods.items():
#     print(item)
