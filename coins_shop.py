coins = int(input("Coins: "))
item = input("Item (skin/battlepass/boost): ")
rank = input("Rank (noob/pro/legend): ")

pret = 0
reducere_proc = 0

# Pret baza
if item == "skin":
    pret = 1200
elif item == "battlepass":
    pret = 2500
elif item == "boost":
    pret = 700
else:
    print("Item invalid!")
    pret = 0

# Reducere
if rank == "noob":
    reducere_proc = 0
elif rank == "pro":
    reducere_proc = 10
elif rank == "legend":
    reducere_proc = 20
else:
    print("Rank invalid!")
    reducere_proc = 0

reducere = pret * reducere_proc // 100
total = pret - reducere

print("Pret baza:", pret)
print("Reducere:", reducere)
print("Total:", total)

if pret == 0:
    print("Cumpararea nu poate fi realizata (item invalid).")
elif coins >= total:
    print("Cumparare reusita! Iti raman", coins - total, "coins.")
    if rank == "legend":
        print("GG! Legendary discount!")
else:
    print("Nu ai destui coins. Mai ai nevoie de", total - coins, "coins.")
