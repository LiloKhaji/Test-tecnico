def pertence_a_fibonacci(numero):
    a, b = 0, 1

    # Verifica se o número é 0 ou 1, que são os primeiros numeros da sequencia
    if numero == a or numero == b:
        return True

    # Gera a sequencia ate encontrar o número ou ultrapassa-lo
    while b < numero:
        a, b = b, a + b

    # Verifica se o número esta na sequencia
    return b == numero

try:
    numero = int(input('Digite um número para verificar se pertence à sequência de Fibonacci: '))

    if pertence_a_fibonacci(numero):
        print(f'O número {numero} pertence a sequência de Fibonacci.')
    else:
        print(f'O número {numero} não pertence a sequência de Fibonacci.')
except ValueError:
    print('Por favor, digite um número válido.')