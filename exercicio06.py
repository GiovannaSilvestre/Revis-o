resp = "S"
while resp == "S":

    peso = float (input ("Digite o seu peso: "))
    altura = float (input ("Digite a sua altura: "))
    imc = peso / altura**2

    if imc <18.6:
        print ("Abaixo do peso")
    elif 18.6 <= peso <= 24.9:
        print ("Peso ideal (parabens)")
    elif 25.0 <= imc <=29.9:
        print ("Levemente acima do peso")
    elif 30.0 <=imc <=34.9:
        print (" Obesidade grau I")
    elif 35.0<= 39.9:
        print ("Obesidade grau II (severa)")
    else:
        print ("Obesidade grau III (morbida)")

resp = input ("Você deseja calcular outro icm [S ou N]: ")