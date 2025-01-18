def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Itera sobre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona o caractere à nova string
        
    return string_invertida

# Entrada do usuário
entrada_usuario = input("Digite uma string para inverter: ")

# Inverte a string
resultado = inverter_string(entrada_usuario)

# Exibe o resultado
print(f"String invertida: {resultado}")
