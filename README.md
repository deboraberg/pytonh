"""criar um pograma que lia peso e altura
e calcule o IMC"""

peso = float(input("Digite o peso"))
altura = float(input("Digite a altura"))
imc = peso / (altura ** 2)
print("O valor do IMC é {:.2F}".format(imc))

"""criar um programa que leia a base e a altura"""
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = (base* altura)/2
print("Area do triângulo", area)
