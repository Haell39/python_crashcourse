# 1.
""" 
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(a + b)

 """
# 2.

""" 
time = int(input("Enter time in DAYS: "))

hours = time * 24
print(f'{time} days in hours is {hours}h1')
 """


# 3.
""" 
a = int(input("Enter your note 1: "))
b = int(input("Enter your note 2: "))
c = int(input("Enter your note 3: "))

media = a + b + c / 3
media = (a + b + c) / 3
print(f"{media:.2f}")

 """
# 4.

while True:
    s = input("Quantidade disponível (ou 'sair' para encerrar): ")
    if s.lower() == 'sair':
        print("Encerrado.")
        break
    try:
        q = int(s)
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue
    if q >= 10:
        print("Estoque suficiente.")
        break
    print("Estoque baixo. Informe novamente.")

""" 
while True:
    s = input("Quantidade ou sair pra sair")
    if s.lower() == 'sair':
        print("FIM")
        break
    q = int(input("Enter your product quantity: "))
    if q >= 10:
        print('Suficiente')
        break
    print('esoque baixo tente dnv!')
 """










