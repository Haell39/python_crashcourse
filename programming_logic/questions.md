# Exercícios de Python para Varejo

## 🟢 Nível Fácil: Variáveis e Condicionais Simples

**Foco:** Entender como manipular dados básicos de sell-out e estoque.

1. **Soma de Vendas:** Peça dois valores de vendas e imprima a soma total.
2. **Conversor de Lead Time:** Peça o tempo de entrega em dias e converta para horas.
3. **Média de Notas:** Receba 3 notas de um treinamento e calcule a média.
4. **Alerta de Estoque:** Peça a quantidade de um produto; se for menor que 10, imprima "Repor Estoque".
5. **Custo de Frete:** Se o estado for "PE", o frete é R$ 20,00; senão, é R$ 10,00.
6. **Par ou Ímpar:** Receba um número de ID e diga se ele é par ou ímpar.
7. **Maior de Idade:** Verifique se um colaborador tem 18 anos ou mais para contratação.
8. **Calculadora de Bônus:** Se a venda for acima de R$ 1.000, dê 10% de desconto.
9. **Positivo ou Negativo:** Verifique se o saldo de estoque inserido é positivo, negativo ou zero.
10. **Comparador de Preços:** Peça o preço de dois produtos concorrentes e diga qual é o mais barato.

---

## 🟡 Nível Médio: Laços (Loops) e Listas

**Foco:** Processar múltiplos registros de promotores e visitas ao PDV.

1. **Contagem de Lojas:** Use um laço para imprimir os números de 1 a 10 (IDs das lojas).
2. **Soma de Lista:** Crie uma lista com 5 valores de vendas e calcule a soma total.
3. **Filtro de Ruptura:** Dada uma lista de estoques `[5, 0, 12, 0, 8]`, conte quantos estão em zero.
4. **Tabuada de Vendas:** Peça um número e mostre a tabuada dele (útil para projeção de metas).
5. **Busca em Lista:** Verifique se o produto "Shampoo" está presente em uma lista de mercadorias.
6. **Maior Venda:** Em uma lista de valores, encontre e imprima o maior valor vendido no dia.
7. **Média de Visitas:** Receba o tempo de 5 visitas de um promotor e calcule a média de tempo no PDV.
8. **Inversor de Nome:** Peça o nome de um cliente e imprima-o de trás para frente.
9. **Filtro de Estado:** Dada uma lista de estados, imprima apenas os que forem "PE" ou "SP".
10. **Validador de Nota:** Peça uma nota de NPS (1 a 5); enquanto o usuário digitar fora desse intervalo, peça novamente.

---

## 🔴 Nível "Real-World": Lógica Aplicada ao Varejo

**Foco:** Simular desafios reais que você encontrará no Programa de Desenvolvimento do Estagiário (PDE).

1. **Relatório de Desempenho:** Dada uma lista de vendas, crie uma nova lista apenas com valores acima de R$ 500,00.
2. **Classificação de Ruptura:** Se o atraso for > 0, classifique como "Ruptura"; se for <= 0, "No Prazo".
3. **Bonificação Escalonada:** Venda > 1000 (10% bônus), entre 500 e 1000 (5%), abaixo (0%).
4. **Frequência de Produtos:** Conte quantas vezes o produto "Pipoca" aparece em uma lista de pedidos.
5. **Dicionário de Preços:** Crie um dicionário com `produto: preço` e peça para o usuário consultar um valor.
6. **Limpeza de Dados:** Dada uma lista com nomes e valores nulos (None), remova os nulos e imprima a lista limpa.
7. **Ranking de Promotores:** Receba nomes e total vendido; identifique quem vendeu mais para ganhar o prêmio do mês.
8. **Análise de NPS:** Calcule a porcentagem de notas 5 (Promotores) em uma lista de avaliações de clientes.
9. **Simulação de Giro:** Comece com um estoque de 50; peça vendas sucessivas até que o estoque chegue a zero.
10. **KPI de Execução:** Crie uma função que receba `Preço Estimado` e `Preço Real`; se a diferença for > 10%, retorne "Alerta de Gôndola".