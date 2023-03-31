# Solicitando dados do usuário
nome_arquivo = input("Digite o nome do arquivo a ser criado: ")
nome_cliente = input("Informe o nome do cliente: ")
data_compra = input("Informe a data da compra (no formato dd/mm/aaaa): ")
valor_total = float(input("Informe o valor total da compra: "))
forma_pagamento = input("Informe a forma de pagamento: ")
quantidade_produtos = int(input("Informe a quantidade de produtos: "))

pasta = "./recibos/"

# Criando arquivo de texto e escrevendo os dados do recibo fiscal
with open(pasta + nome_arquivo, "w") as arquivo:
    arquivo.write("Recibo Fiscal\n\n")
    arquivo.write(f"Nome do cliente: {nome_cliente}\n")
    arquivo.write(f"Data da compra: {data_compra}\n")
    arquivo.write(f"Valor total da compra: R$ {valor_total:.2f}\n")
    arquivo.write(f"Forma de pagamento: {forma_pagamento}\n")
    arquivo.write(f"Quantidade de produtos: {quantidade_produtos}\n")

# Fechando o arquivo
arquivo.close()

print("Recibo fiscal gerado com sucesso!")