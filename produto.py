from colorama import init, Fore, Back, Style
init(autoreset=True)

def produto ():
    print(Fore.LIGHTBLUE_EX + "\n===CADASTRO PRODUTO===")
    Nome_produto = input("\nInforme o nome do produto: ").strip()
    while True:
        try:
            Preco_produto = float(input("Informe o preço do produto: "))
        except ValueError:
            print(Fore.RED + "\nINSIRA UM '.' OU NUMERO VÁLIDO!")
            continue
            
        while True:
            try:
                Quantidade_produto = int(input("Informe a quantidade do produto :"))
            except ValueError:
                print(Fore.RED +"\nINSIRA UMA QUANTIDADE VÁLIDA!")
                continue
            
            print(Fore.LIGHTGREEN_EX + "\nPRODUTO CADASTRADO COM SUCESSO! ")
            print (f"Produto: {Nome_produto}")
            print(f"Preço: {Preco_produto}")
            print(f"Quantidade: {Quantidade_produto}")
            break
        break

produto()