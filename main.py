import experimentos.experimento_1 as exp1
import experimentos.experimento_2 as exp2
import experimentos.experimento_3 as exp3
import experimentos.experimento_4 as exp4


def main():
    print("Digite o número do experimento que deseja executar (0 para parar): ")
    print("1 - Experimento 1")
    print("2 - Experimento 2")
    print("3 - Experimento 3")
    print("4 - Experimento 4")

    while True:
        experimento = input()

        if experimento == "0":
            print("Encerrando o programa.")
            break
        elif experimento == "1":
            exp1.run_experimento()
            print(
                "Experimento 1 concluído. Digite o número do próximo experimento (0 para parar): "
            )
        elif experimento == "2":
            exp2.run_experimento()
            print(
                "Experimento 2 concluído. Digite o número do próximo experimento (0 para parar): "
            )
        elif experimento == "3":
            exp3.run_experimento()
            print(
                "Experimento 3 concluído. Digite o número do próximo experimento (0 para parar): "
            )
        elif experimento == "4":
            exp4.run_experimento()
            print(
                "Experimento 4 concluído. Digite o número do próximo experimento (0 para parar): "
            )
        else:
            print(
                "Experimento inválido. Digite o número do experimento que deseja executar (0 para parar): "
            )


if __name__ == "__main__":
    main()
