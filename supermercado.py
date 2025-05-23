"""2- Planejando compras no supermercado:

Você foi ao supermercado com um orçamento de R$100. Escreva um algoritmo que permita ao usuário inserir o nome e o valor de cada produto que ele deseja comprar. O sistema deve :

Somar os valores dos produtos,
Informar quando o orçamento for ultrapassado,
Ao final, mostre uma lista de compras com os nomes e preços, e o total gasto.
- Requisitos:

O algoritmo deve parar quando o orçamento for ultrapassado ou quando o usuário decidir parar.
Use estruturas de petição e decisão."""

orcamento = 100.00
total_gasto = 0.0
lista_compras = []

print("Bem-vindo ao sistema de compras! Seu orçamento é de R$100.00")

while True:

    nome_produto = input("\nDigite o nome do produto (ou 'sair' para encerrar): ")
    
 
    if nome_produto.lower() == 'sair':
        break
    
    try:
        valor_produto = float(input(f"Digite o valor de {nome_produto}: R$"))
    except ValueError:
        print("Valor inválido! Digite um número.")
        continue
    

    if total_gasto + valor_produto > orcamento:
        print(f"\nATENÇÃO: O produto {nome_produto} ultrapassa seu orçamento!")
        print(f"Total gasto: R${total_gasto:.2f}")
        print(f"Orçamento restante: R${orcamento - total_gasto:.2f}")
        break
    

    lista_compras.append((nome_produto, valor_produto))
    total_gasto += valor_produto
    
  
    print(f"\nProduto adicionado: {nome_produto} - R${valor_produto:.2f}")
    print(f"Total parcial: R${total_gasto:.2f}")
    print(f"Saldo restante: R${orcamento - total_gasto:.2f}")


print("\n--- RESUMO DAS COMPRAS ---")
for produto, valor in lista_compras:
    print(f"- {produto}: R${valor:.2f}")

print(f"\nTotal gasto: R${total_gasto:.2f}")
print(f"Orçamento inicial: R${orcamento:.2f}")
print(f"Saldo restante: R${orcamento - total_gasto:.2f}")

if total_gasto > orcamento:
    print("\nAVISO: Você ultrapassou seu orçamento!")
elif total_gasto == orcamento:
    print("\nVocê gastou exatamente seu orçamento!")
else:
    print("\nVocê ficou dentro do orçamento!")