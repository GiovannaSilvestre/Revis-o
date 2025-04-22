resp = "S"
while resp == "S"

    num= float (input ("Digite um número: "))

    if num%2 ==0 and num>0:
     print ("O número é par e positivo")
    elif num%2 ==0 and num<0:
        print("O número é par e negativo")
    elif num%2 !=0 and num>0:
        print ("O número é impar e positivo")
    else:
     print("O número é impar e negativo")

    resp = input ("Deseja verificar outro número? [S or N]: ")




