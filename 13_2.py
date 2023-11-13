from random import choice

def gol_ya_pooch():
    entekhab = ['left', 'right']
    answer = choice(entekhab)
    # print(answer)
    guess = input("Which hand?")
    n=0
    while guess not in entekhab:
        n += 1
        if n<3:
            guess = input("Which hand?(only choose left or right)")
        else:
            guess = input("Allaho Akbar. Only choose left or right.")
    if guess==answer:
        print(f"You win. it was in {answer} hand.")
    else:
        print(f"You lose. it was in {answer} hand.")

k = int(input("Chand dor mikhay bazi koni?"))
for i in range(k):
    gol_ya_pooch()


# اول ایمپورت ها را انجام میدهیم.
# بعد توابع خودمان را مینویسیم.
# بعد کدهای اصلی صفحه