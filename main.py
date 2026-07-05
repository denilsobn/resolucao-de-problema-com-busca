import experimentos.experimento_1 as exp1
import experimentos.experimento_2 as exp2
import experimentos.experimento_3 as exp3
import experimentos.experimento_4 as exp4

def main():
    print("Hello from busca-ia!")
    print("Digite o número do experimento que deseja executar (0 para parar): ")

    while True:
        experimento = input()

        if experimento == '0':
            print("Encerrando o programa.")
            break
        elif experimento == '1':
            exp1.run_experimento()
        elif experimento == '2':
            exp2.run_experimento()
        elif experimento == '3':
            exp3.run_experimento()
        elif experimento == '4':
            exp4.run_experimento()


if __name__ == "__main__":
    main()
