pret = float(input("Prețul unui obiect (lei): "))
bucati = int(input("Câte bucăți vrei să cumperi: "))
bani = float(input("Câți bani ai (lei): "))

cost_total = pret * bucati
rest = bani - cost_total

print("Costul total este:", cost_total, "lei")
print("Bani rămași după cumpărături:", rest, "lei")
