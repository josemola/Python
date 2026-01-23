num_decimal=int(input("Dime un numero: "))
num_binario=int(input("Dime otro numero en binario: "))

def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

def binario_a_decimal(binario):
    decimal = 0
    binario_str = str(binario)[::-1]
    for i in range(len(binario_str)):
        if binario_str[i] == "1":
            decimal += 2 ** i
    return decimal


resultado_binario = decimal_a_binario(num_decimal)
print(f"El decimal {num_decimal} en binario es: {resultado_binario}")
resultado_decimal = binario_a_decimal(num_binario)
print(f"El binario {num_binario} en decimal es: {resultado_decimal}") 