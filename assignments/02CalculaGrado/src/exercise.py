def calcula_grado(x):
    if 0.90 <= x < 0.99:
        return 'A'
    elif 0.80 <= x < 0.90:
        return 'C'
    elif 0.70 <= x < 0.80:
        return 'B'
    elif 0.60 <= x < 0.70:
        return 'D'
    else:
        return "score incorrecto"
def main():
    x = float(input('Ingresa Un valor entre 0.0 y 1.0: '))
    print(calcula_grado(x))
if __name__=='__main__':
    main()

