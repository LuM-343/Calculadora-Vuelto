#Calcular el cambio más optimo que se le debe dar a un comprador, siendo lo mejor la menor cantidad de villetes a utilziar
switch = 1
while switch == 1:
    gastado = 0
    pago = 0
    vuelto = 0
    bi_200 = 0
    bi_100 = 0
    bi_50 = 0
    bi_20 = 0
    bi_10 = 0
    bi_5 = 0
    mon_1 = 0
    cent_50 = 0
    cent_25 = 0
    cent_10 = 0
    cent_5 = 0

    print("-------------------------------")
    print("Bienvenido a la calculadora de Vueltos L&M")
    print("Por favor ingrese el monto a pagar:")
    gastado = float(input())
    print()
    print("Por favor ingrese la denominación del billete con la que se pagó")
    pago = float(input())

    vuelto = pago - gastado

    if vuelto == 0:
        print ("El pago fue exacto, no se debe dar vuelto")
    elif vuelto > 0:
        print ("Se debe dar un vuelto de: Q",vuelto)
        print("Dividido de esta forma:")
        
        if vuelto > 0:
            if vuelto>=200:
                bi_200 = int(vuelto/200)
                vuelto = vuelto % 200
                print(bi_200, "billetes de Q200.00")
            if vuelto>=100:
                bi_100 = int(vuelto/100)
                vuelto = vuelto % 100
                print(bi_100, "billetes de Q100.00")
            if vuelto>=50:
                bi_50 = int(vuelto/50)
                vuelto = vuelto % 50
                print(bi_50, "billetes de Q50.00")
            if vuelto>=20:
                bi_20 = int(vuelto/20)
                vuelto = vuelto % 20
                print(bi_20, "billetes de Q20.00")
            if vuelto>=10:
                bi_10 = int((vuelto/10))
                vuelto = vuelto % 10  
                print(bi_10, "billetes de Q10.00")
            if vuelto>=5:
                bi_5 = int(vuelto/5)
                vuelto = vuelto % 5
                print(bi_5, "billetes de Q5.00")
            if vuelto>=1:
                mon_1 = int(vuelto/1)
                vuelto = vuelto % 1
                print(mon_1, "monedas de Q1.00")
            if vuelto>=0.5:
                cent_50 = int(vuelto/0.5)
                vuelto = vuelto % 0.5
                print(cent_50, "monedas de Q0.50")
            if vuelto>=0.25:
                cent_25 = int(vuelto/0.25)
                vuelto = vuelto % 0.25
                print(cent_25, "monedas de Q0.25")
            if vuelto>=0.10:
                cent_10 = (int(vuelto/0.10))
                vuelto = vuelto % 0.10
                print(cent_10, "monedas de Q0.10")
            if vuelto>=0.05:
                cent_5 = int(vuelto/0.05)
                vuelto = vuelto % 0.05
                print(cent_5, "monedas de Q0.05")
            if vuelto <0.5:
                vuelto = round(vuelto)

    else:
        print("¡¡¡Falta dinero para completar el pago!!!")
    print()
    print("---------------------------------------------")
    print("Desea realizar otra operación")
    print("Si = 1       No = 0")
    switch = int(input())

print("Gracias por su atención")
