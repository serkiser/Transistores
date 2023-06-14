import math
opcion = 0
while True:
    print("""
    ¿Que esquema quieres calcular?
    
    1) Calcular Circuito Polarización Directa
    2) Calcular Circuito Realimentación de Emisor
    3) Calcular Circuito Polarización Universal
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        Vce = 0.2
        Vbe = 0.7
        Vcc = float(input("Introduce los Voltios del circuito: ") )
        Rb = float(input("Introduce el valor de Rb: "))
        Rc = float(input("Introduce el valor de Rc: "))
        b = float(input("Introduce el valor de beta: "))
        """Calculos"""
        Isat = (Vcc-Vce)/Rc
        Vrb = Vcc-Vbe
        Ib = Vrb/Rb
        Ic = b*Ib
        Vce2 = Vcc-(Rc-Ic)
        print("Isat = ", Isat, "mA")
        print("Vrb = ", Vrb, "V")
        print("Ib = ", Ib, "uA")
        print("Ic = ", Ic, "mA")
        print("Vce = ", Vce2, "V")
        print("Vcorte =", Vcc, "V")
    elif opcion == 2:
        Vce = 0.2
        Vbe = 0.7
        Vcc = float(input("Introduce los Voltios del circuito: ") )
        Rb = float(input("Introduce el valor de Rb: ") )
        Rc = float(input("Introduce el valor de Rc: ") )
        Re = float(input("Introduce el valor de Rb: ") )
        b = float(input("Introduce el valor de beta: ") )
        """Calculos2"""
        Isat = (Vcc-Vce)/(Rc+Re)
        Ib = (Vcc-Vbe)/(Rb+(Re*b))
        Ic = b*Ib
        Vce2 = Vcc-(Rc*Ic)-(Re*Ic)
        print("Isat = ", Isat, "mA")
        print("Ib = ", Ib, "uA")
        print("Ic = ", Ic, "mA")
        print("Vce = ", Vce2, "V")
        print("Vcorte =", Vcc, "V")
    elif opcion == 3:
        Vce = 0.2
        Vbe = 0.7
        Vcc = float(input("Introduce los Voltios del circuito: ") )
        R1 = float(input("Introduce el valor de R1: ") )
        R2 = float(input("Introduce el valor de R2: ") )
        Rc = float(input("Introduce el valor de Rc: ") )
        Re = float(input("Introduce el valor de Rb: ") )
        b = float(input("Introduce el valor de beta: ") )
        """Calculos3"""
        Rth = (R1*R2)/(R1+R2)
        Vth = (Vcc*R2)/(R1+R2)
        Isat = (Vcc-Vce)/(Rc+Re)
        Ib = (Vth-Vbe)/(Rth+(Re*b))
        Ic = b*Ib
        Vce2 = Vcc-(Rc*Ic)-(Re*Ic)
        print("Rth = ", Rth, "Ohm")
        print("Vth = ", Vth, "V")
        print("Isat = ", Isat, "mA")
        print("Ib = ", Ib, "uA")
        print("Ic = ", Ic, "mA")
        print("Vce = ", Vce2, "V")
        print("Vcorte =", Vcc, "V")
    elif opcion == 4:
        break
    else:
        print("Opción incorrecta")