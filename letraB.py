numero = int(input("Digite um número: "))
a, b = 0, 1

# Loop para gerar a sequência
while a <= numero:
    if a == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
        break  # Interrompe o loop se o número for encontrado
    a, b = b, a + b

if a > numero:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")