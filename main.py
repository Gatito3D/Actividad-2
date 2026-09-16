
saldo = float(input())
retirado_hoy = float(input())
monto = int(input())

if monto % 50 != 0:
    print(f"MONTO NO VÁLIDO | saldo: {int(saldo) if saldo == int(saldo) else saldo}")
elif monto > saldo:
    print(f"SALDO INSUFICIENTE | saldo: {int(saldo) if saldo == int(saldo) else saldo}")
elif retirado_hoy + monto > 6000:
    print(f"LÍMITE DIARIO EXCEDIDO | saldo: {int(saldo) if saldo == int(saldo) else saldo}")
else:
    saldo -= monto
    print(f"ENTREGADO | saldo: {int(saldo) if saldo == int(saldo) else saldo}")