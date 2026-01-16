# Citim datele de la utilizator
pret = float(input("Introdu pretul unui obiect (in lei): "))
bucati = int(input("Introdu cate bucati vrei sa cumperi: "))
bani = float(input("Introdu cati bani ai (in lei): "))

# Calculam costul total
cost_total = pret * bucati

# Verificam daca sunt suficienti bani
if bani >= cost_total:
    print("Poti cumpara obiectele!")
    print(f"Iti vor ramane {bani - cost_total:.2f} lei.")
else:
    print("Nu ai suficienti bani pentru aceste obiecte.")
    print(f"Iti mai lipsesc {cost_total - bani:.2f} lei.")
