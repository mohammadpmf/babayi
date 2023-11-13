jame_kol = 0

i = 0
while True:
    gheymat = float(input(f"Gheymate item e {i+1} om cheghadr shod?"))
    i = i+1
    if gheymat==0:
        break
    jame_kol = jame_kol + gheymat

print(f"Kolle factor shoma: {jame_kol} tooman")