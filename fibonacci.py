def is_fibonacci(n):
    # Função auxiliar para verificar se um número é um número de Fibonacci
    if n < 0:
        return False
    
    # Função para calcular o n-ésimo número de Fibonacci
    def fibonacci(num):
        a, b = 0, 1
        while b <= num:
            if b == num:
                return True
            a, b = b, a + b
        return False

    return fibonacci(n)

# Solicitar a entrada do usuário
try:
    number = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
