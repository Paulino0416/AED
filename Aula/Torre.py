def moverD(discos, ori, aux, dest):
    if discos > 0:
        moverD(discos - 1, ori, dest, aux)
        print(f"Mover disco {discos} para torre {dest}")
        moverD(discos - 1, aux, ori, dest)


discos = int(input("Quantos discos tem a torre? "))
if discos < 1:
    print("Número de discos inválido.")
else:
    moverD(discos, 'A', 'B', 'C')

