""" 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

def fibonacci(n):

    #valores iniciais
    fib = [0,1]

    #Loop da sequência de valores
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    #Verificar se o numero pertence à sequência
    if n in fib:
        print(f"O número {n} pertence à sequencia de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequencia de Fibonacci.")

fibonacci(8)