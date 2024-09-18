import math


class Operacao:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)  # utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "Impossível Dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f' \n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio1(self):
        msg = ""
        for i in range(1, 11,1):
            msg += F'\n{i}'
        return msg

    def exercicio2(self): #2
        pares = ""
        for i in range(1, 21,1):
            if i % 2 == 0:
                pares+= f'\n{i}'
        return pares

    def exercicio3(self): #3
            for i in range(1, 101,1):
                soma += i

    def exercicio4(self): #4
        multiplos = ""
        for i in range(1, 51,1):
            if i % 5 == 0:
                multiplos+=f'\n{i}'
        return multiplos

    def exercicio5(self, num):
        if num % 2 == 0:
            return "Par"
        else:
            return "ìmpar"

    def exercicio6(self, num):
        if num < 0:
            return ("O número é negativo.")
        else:

            return("O número é positivo.")

    def exercicio7(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f' \n{num1} * {i} = {num1 * i}'

    def exercicio8(self, num):
        if num < 0:
            return "O número é negativo."
        else:
            for i in range(1, num + 1):
                print(i)
        return "O número é positivo."

    def exercicio9(self, num):
        soma = 0
        for i in range(1, num, 1):
            soma += i
        return soma

    def exercicio10(self, num):
        primo = "1\n2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
            return primo


    def exercicio11(self, num):
        if num == 2 or num == 3 or num == 5:
           return f'0 {num} é primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'0 {num} Não é primo!'


    def exercicio12(self, num):
            res = 1
            for num in range(1, num , 1):
                res += res * num
            return res

    def exercicio13(self, num):
        fib1 = 0
        fib2 = 1
        for i in range(1, num):
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
            print(fib3)
        return fib3

    #14 Não fiz

    def exercicio15(self, num):
        num = input("Digite um número: ")
        num_str = str(num)
        soma = 0
        for digito in num_str:
            soma += int(digito)
        return soma

    def exercicio16(self, num):
        numero = int(input("Digite um número: "))

        if numero <= 0:
            print("Digite um número maior que 0.")
        else:
            print("Números pares de 1 até", numero, ":")
            for i in range(1, numero + 1):
                if i % 2 == 0:
                    print(i, end=' ')

            print()

            print("Números ímpares de 1 até", numero, ":")
            for i in range(1, numero + 1):
                if i % 2 != 0:
                    print(i, end=' ')

            print()

    def exercicio17(self, num):
        numero = int(input("Digite um número"))

        if numero <= 0:
            print("digite um número maior do que 0.")
        else:
            print("Os Números primos são", numero, ":")
            for i in range(2, numero + 1):
                if i % 2 != 0:
                    print(i, end=' ')

            print()

    def exercicio18(self, num):
        for i in range(1, num):
            if 0 == 2:
                return 0
            elif i % 2 == 0:
                print(1 + i // 2)
            else:
                print(1 + (3 * i + 1))

    def exercicio19(self, num):
        somapar = 0
        somaimpar = 0
        for i in range(1, num + 1, 1):
            if i % 2 == 0:
                somapar += i
            else:
                somaimpar += i
        return f'a soma dos pares é {somapar} e a dos ímpares é {somaimpar}.'


    def exercicio20(num):
    soma_divisores = 0
    
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    
    if soma_divisores == num:
        print(f"{num} é um número perfeito!")
    else:
        print(f"{num} não é um número perfeito.")


    def exercicio21
    A = 10
    B = 20

    temp = A
    A = B
    B = temp

    print(f"O valor de A agora é: {A}")
    print(f"O valor de B agora é: {B}")













