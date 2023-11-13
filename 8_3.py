jame_kol = 0

for i in range(20):
    gheymat = float(input(f"Gheymatesh item e {i+1} om cheghadr shod?"))
    if gheymat==0:
        break
    jame_kol = jame_kol + gheymat

print(f"Kolle factor shoma: {jame_kol} tooman")

# همین برنامه رو با while بنویسید.