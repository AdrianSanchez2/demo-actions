def dividir(a,b):
    cociente = a//b
    resto = a%b
    return cociente, resto

if __name__ == "__main__":
    print(dividir(5,3))