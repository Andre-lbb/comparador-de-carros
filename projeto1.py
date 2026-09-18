import json

class Carros_caracteristicas: 
    def __init__(self, marca, modelo, ano, preco, potencia, consumo_alcool, consumo_gasolina, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.potencia = potencia
        self.consumo_alcool = consumo_alcool
        self.consumo_gasolina = consumo_gasolina
        self.quilometragem = quilometragem
carros = []

#criação arquivo json para salvar os carros
def salvar_carros():
    dados = []
    for veiculo in carros:
        dados.append(veiculo.__dict__)
    with open("carros.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

#importação do arquivo dos carros
def carregar_carros():
    try: 
        with open("carros.json", "r", encoding="utf-8") as arquivo: 
            dados = json.load(arquivo)

            for veiculo in dados: 
                carros.append(
                    Carros_caracteristicas(
                        veiculo["marca"], veiculo["modelo"], veiculo["ano"], veiculo["preco"], veiculo["potencia"], veiculo["consumo_alcool"], veiculo["consumo_gasolina"], veiculo["quilometragem"]
                    )
                )
    except FileNotFoundError:
        pass
carregar_carros()

#lista de opções do programa
opcao = int(input("Digite um número para escolher uma opção:\n" \
"1 - para Cadastrar carro;\n" \
"2 - para Listar carros;\n" \
"3 - para Buscar carros;\n" \
"4 - para Comparar dois carros;\n" \
"5 - para Remover carro;\n" \
"6 - para Sair.\n"))

#tratamento dos casos do programa
match opcao:
    case 1:
        marca = input("Digite as características do carro\n" \
        "Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        preco = int(input("Preço: "))
        potencia = int(input("Potência: "))
        consumo_alcool = float(input("Consumo no álcool (em km/l): "))
        consumo_gasolina = float(input("Consumo na gasolina (em km/l): "))
        quilometragem = int(input("Quilometragem do veículo: "))

        veiculo = Carros_caracteristicas(
            marca, modelo, ano, preco, potencia,consumo_alcool, consumo_gasolina, quilometragem
        )
        carros.append(veiculo)
        salvar_carros()

#lista veículos cadastrados
    case 2: 
        print("--- CARROS CADASTRADOS ---")
        for veiculo in carros: 
            print(f"Marca: {veiculo.marca}")
            print(f"Modelo: {veiculo.modelo}")
            print(f"Ano: {veiculo.ano}")
            print(f"Preço: {veiculo.preco:.2f} R$")
            print(f"Potência: {veiculo.potencia} cavalos")
            print(f"Consumo médio no álcool: {veiculo.consumo_alcool} km/l")
            print(f"Consumo médio na gasolina: {veiculo.consumo_gasolina} km/l")
            print(f"Quilometragem: {veiculo.quilometragem}km\n")

#busca veículo
    case 3: 
        print("\n--- FILTROS DE PESQUISA ---")
        marca_busca = input("\nMarca (deixe vazio para ignorar): ")
        modelo_busca = input("Modelo (deixe vazio para ignorar): ")
        ano_minimo = input("Ano mínimo (deixe vazio para ignorar): ")
        preco_maximo = input("Valor máximo (deixe vazio para ignorar): ")
        potencia_minima = input("Potência mínima, em cavalos (deixe vazio para ignorar): ")

        encontrado = False
        for veiculo in carros:
            if marca_busca != "" and veiculo.marca.lower() != marca_busca.lower():
                continue
            if modelo_busca != "" and veiculo.modelo.lower() != modelo_busca.lower():
                continue
            if ano_minimo != "" and veiculo.ano < int(ano_minimo):
                continue
            if preco_maximo != "" and veiculo.preco > float(preco_maximo):
                continue
            if potencia_minima != "" and veiculo.potencia < int(potencia_minima):
                continue
            encontrado = True

            print(f"\nMarca: {veiculo.marca}")
            print(f"Modelo: {veiculo.modelo}")
            print(f"Ano: {veiculo.ano}")
            print(f"Preço: {veiculo.preco} R$")
            print(f"Potencia: {veiculo.potencia} Cavalos");
            print(f"Consumo médio no álcool: {veiculo.consumo_alcool} km/l")
            print(f"Consumo médio na gasolina: {veiculo.consumo_gasolina} km/l")
            print(f"Quilometragem: {veiculo.quilometragem}km\n")

        if not encontrado:
                print("\nNenhum veículo encontrado!")

#compara carros
    case 4:
        print("--- COMPARADOR DE DOIS CARROS ---")
        for i, veiculo in enumerate(carros):
            print(f"{i+1} - {veiculo.marca} {veiculo.modelo} ({veiculo.ano})")

        def escolha_veiculo(mensagem, carros):
            while True:
                indice = int(input(mensagem))
                if indice < 1 or indice > len(carros):
                    print(f"Escolha valores entre 1 e {len(carros)}!")
                    continue
                return carros[indice-1]

        carro1 = escolha_veiculo("Escolha o primeiro veículo: ", carros)
        carro2 = escolha_veiculo("Escolha o segundo veículo: ", carros)
            
        if carro1.preco < carro2.preco:
            print(f"O primeiro carro é {carro2.preco - carro1.preco} R$ mais barato!")
        else:
            print(f"O segundo carro é {carro1.preco - carro2.preco} mais barato!")

        if carro1.potencia < carro2.potencia:
            print(f"O primeiro carro tem {carro2.potencia - carro1.potencia} cavalos a mais do que o carro 2!")
        else: 
            print(f"O segundo carro tem {carro1.potencia - carro2.potencia} cavalos a mais do que o carro 1!")    

        if carro1.consumo_alcool < carro2.consumo_alcool:
            print(f"O primeiro carro faz {carro2.consumo_alcool - carro1.consumo_alcool:.2f} a mais com um litro de álcool do que o carro 2!")
        else:
            print(f"O segundo carro faz {carro1.consumo_alcool - carro2.consumo_alcool:.2f} a mais com um litro de álcool do que o carro 1!")

        if carro1.consumo_gasolina < carro2.consumo_gasolina:
            print(f"O primeiro carro faz {carro2.consumo_gasolina - carro1.consumo_gasolina:.2f} a mais com um litro de gasolina do que o carro 2!")
        else:
            print(f"O segundo carro faz {carro1.consumo_gasolina - carro2.consumo_gasolina:.2f} a mais com um litro de gasolina do que o carro 1!")

        if carro1.quilometragem < carro2.quilometragem:
            print(f"O primeiro carro tem {carro2.quilometragem - carro1.quilometragem} quilometros a menos do que o carro 2!")
        else:
            print(f"O segundo carro tem {carro1.quilometragem - carro2.quilometragem} quilometros a menos do que o carro 1!")

#exclusão veículo
    case 5:
        print("--- EXCLUIR VEÍCULO ---")
        if not carros:
            print("Não há veículos cadastrados para serem excluídos!")

        for i, veiculo in enumerate(carros):
            print(f"{i+1} - {veiculo.marca} {veiculo.modelo} ({veiculo.ano})")
        
            def escolha_veiculo(mensagem, carros):
                while True:
                    indice = int(input(mensagem))
                    if indice < 1 or indice > len(carros):
                        print(f"Escolha valores entre 1 e {len(carros)}!")
                        continue
                    return carros[indice-1]

        carro_escolhido = escolha_veiculo("Escolha um veículo para ser excluído: ",carros)
        carros.remove(carro_escolhido)
        salvar_carros()
        print(f"{veiculo.marca} {veiculo.modelo} ({veiculo.ano}) foi excluído do sistema!")

#sair
    case 6: 
        print("Você escolheu sair.")
        print("Finalizando programa!\n")