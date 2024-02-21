def funcao(x):
    return x**3 - 5*x + 1

def bisseccao(a, b, epsilon):
    iteracoes = 0
    if funcao(a) * funcao(b) < 0:
        x = (a + b) / 2
        while abs(funcao(x)) > epsilon:
            print(f'Iteração {iteracoes}: x = {x}, f(x) = {funcao(x)}')
            if funcao(a) * funcao(x) < 0:
                b = x
            else:
                a = x
            x = (a + b) / 2
            iteracoes += 1
        print(f'## A raiz do intervalo dado é: {x} obtida na iteração: {iteracoes}')
    else:
        print('## Não há raízes no intervalo dado.')
        

# Intervalo inicial
a = 2.0
b = 3.0

# Precisão desejada
epsilon = 1e-1

print("## Método da Bisseção para a função f(x) = x^3 - 5x + 1:")
bisseccao(a, b, epsilon)