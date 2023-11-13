# cart = []
# while True:
#     a = input('what do you need?')
#     if a in ['end', 'exit', 'payan', 'tamam', '0']:
#         break
#     cart.append(a)
# print(f"your items are: {cart}")

n = int(input("Enter n:"))
for i in range(n):
    cart = []
    a = ''
    while a not in ['end', 'exit', 'payan', 'tamam', '0']:
        cart.append(a)
        a = input('what do you need?')
    cart.pop(0)
    print(f"your items are: {cart}")