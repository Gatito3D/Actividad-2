
saldo = float(input("Digite su saldo disponible: "))
Retirado_hoy = float(input("Digite la cantidad retirada el dia de hoy:  "))
monto = int(input("Ingrese el monto que desea retirar "))

if monto % 50 !=0:
    print("monto no valido | saldo : ",saldo)
    
elif monto > saldo:
    print("Saldo insuficiente | saldo : ",saldo)

elif Retirado_hoy + monto > 6000:
    print("Limite diario excedido | saldo : ",saldo)
    
else:
    saldo = saldo - monto
    print("Entregado | saldo :",saldo)