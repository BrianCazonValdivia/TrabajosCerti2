def verificar_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("VALOR INVALIDO: Los lados del triángulo deben ser mayores que 0")

    if a == b == c:
        return "EL TRIANGULO ES EQUILATERO"
    elif a == b or b == c or a == c:
        return "EL TRIANGULO ES ISOSCELES"
    else:
        return "EL TRIANGULO ES ESCALENO"


while True:
    try:
        lado_a = float(input("INGRESE EL LADO A DEL TRIANGULO: "))
        lado_b = float(input("INGRESE EL LADO B DEL TRIANGULO: "))
        lado_c = float(input("INGRESE EL LADO C DEL TRIANGULO: "))

        resultado = verificar_triangulo(lado_a, lado_b, lado_c)
        print(resultado)
        break
    except ValueError as e:
        print(e)
        print("Por favor, intente de nuevo.")