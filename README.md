# Fome Zero
# 1. Problema de negócio
   
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações. Para entender melhor o negócio e conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, este projeto tem como objetivo identificar pontos chaves da empresa, respondendo às perguntas utilizando dados! Para isso iremos responder as seguintes perguntas de negócios:


## Geral:
  1. Quantos restaurantes únicos estão registrados?
  2. Quantos países únicos estão registrados?
  3. Quantas cidades únicas estão registradas?
  4. Qual o total de avaliações feitas?
  5. Qual o total de tipos de culinária registrados?

## Países:
  1. Qual o nome do país que possui mais cidades registradas?
  2. Qual o nome do país que possui mais restaurantes registrados?
  3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
  4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
  5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
  6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
  7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
  8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
  9. Qual o nome do país que possui, na média, a maior nota média registrada?
  10. Qual o nome do país que possui, na média, a menor nota média registrada?
  11. Qual a média de preço de um prato para dois por país?

## Cidades:
  1. Qual o nome da cidade que possui mais restaurantes registrados?
  2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
  3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
  4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
  5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
  6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
  7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
  8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes:
  1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
  2. Qual o nome do restaurante com a maior nota média?
  3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
  4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
  5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
  6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
  7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
  8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

# 3. Estratégia da solução

### 1. Entender os dados que estamos trabalhando:
	a. O que cada coluna representa?
	b. Existem colunas que podem ser removidas do DataFrame, por possuir somente 1 valor em todas as linhas?
### 2. Fazer uma limpeza nos dados:
	a. Verificar se existem dados duplicados
	b. Entender as variáveis disponíveis na base de dados fazendo uma tabela de estatística descritiva.
	c. Verificar se há dados faltantes e remove-los
### 3. Explorar os dados e responder as perguntas:
	a. Começar respondendo as perguntas sem usar programação, apenas para planejar a sua solução.
	b. Com o planejamento feito, implementar os passos/ações utilizando a linguagem de programação.
	c. Se necessário, utilizar gráficos para consolidar e validar a resposta.

# 4. Top 3 Insights de dados
1. A Índia é o principal país da plataforma, com maior quantidade de cidades e restaurantes cadastrados. 
2. Apesar de ser o principal país da plataforma, a Índia não possui nenhuma cidade entre as 10 primeiras em restaurantes com tipos de culinária distintos, Birmingham da Inglaterra é a principal cidade com mais restaurantes ecléticos.
3. A indonésia é o país com menor quantidade de restaurantes cadastrados e também o que possui maior preço médio de pratos para duas pessoas, isso pode ser um indicativo do motivo pelo qual o país tem maior dificuldade de se expandir o número de restaurantes na plataforma.

# 5. O produto final do projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://jp1mendes-fomezero.streamlit.app/

![dash](https://github.com/user-attachments/assets/1f841fde-d0dc-4a19-b7b2-b4285f9f5c71)

# 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam as métricas de negócio definidas da melhor forma possível.
