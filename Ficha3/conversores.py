def converter_moeda(valor,taxa):
    return valor*taxa

def apresentar_menu(insira):
    while True:
        print("\n--- CONVERSOR DE MOEDAS ---")
        print("1. Converter para dolar(taxa 1.12)")
        print("2. Converter para libra(taxa 0.85)")
        print("3. Definir nova moeda")
        print("4. Sair")
        insira=int(input("Insira uma opção(1-4)"))
        match insira:
            case 1:
                taxa=1.12
                valor=float(input("Insira o valor que quer converter:"))
                print(f"{converter_moeda(valor,taxa):.2f}")
                
            case 2:
                taxa=0.85
                valor=float(input("Insira o valor que quer converter:"))
                print(f"{converter_moeda(valor,taxa):.2f}")
            case 3:
                nome_moeda=input("Insira o nome da moeda:")
                taxa=float(input("Insira o valor da taxa de conversão:"))
                valor=float(input("Insira o valor que quer converter:"))
                print(f"{converter_moeda(valor,taxa):.2f}, {nome_moeda}")    
            case 4:
                print("A sair do programa...")
                break
                        
            case _: # Caso o utilizador digite qualquer outra coisa
                print("Opção inválida! Tente novamente.")