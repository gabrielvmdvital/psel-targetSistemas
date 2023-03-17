def fibonacci(n: int) -> list:
    fib_list = [0, 1]
    while fib_list[-1] < n+1: #loop usado para construir a sequencia e armazenala na lista fib_list
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list[:-1]

if __name__ == "__main__":
    num = int(input("Digite um número: "))

    fib_sequence = fibonacci(num)

    # Verifica se o número fornecido pelo usuário está na sequência de Fibonacci
    if num in fib_sequence:
        print(num, "pertence à sequência de Fibonacci:", fib_sequence)
    else:
        print(num, "não pertence à sequência de Fibonacci:", fib_sequence)