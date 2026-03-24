# BLOCO 2: Nível Iniciante (Estruturas Condicionais)

# 1. Classificador de Números
""" 
def classificador():
    n = int(input("Digite um numero qualquer: "))
    if n % 2 == 0:
        print(f"O Numero {n} é PAR")
    else:
        print(f"O Numero {n} é IMPAR")
    print("Zero" if n == 0 else "Positivo" if n > 0 else "Negativo")

classificador()
"""

# 2. Cálculo de Média Acadêmica
""" 
def media_aritimetica():
    n = float(input("Digite dua nota 1: "))
    n2 = float(input("Digite dua nota 2: "))
    n3 = float(input("Digite dua nota 3: "))
    n4 = float(input("Digite dua nota 4: "))
    
    media = (n + n2 + n3 + n4) / 4
    print(f'Sua média foi: {media:.2f}')
    
    print("Aprovado" if media >= 7 else "Recuperação" if 5 <= media <= 6.9 else "Reprovado")


media_aritimetica()
"""

























