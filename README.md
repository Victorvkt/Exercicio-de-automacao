📦 Automação de Cadastro de Produtos com Python

Este projeto é uma automação em Python que realiza o cadastro automático de produtos em um site, utilizando PyAutoGUI para interação com a interface gráfica e Pandas para leitura e controle da base de dados.

A automação foi desenvolvida para evitar cadastros duplicados, mesmo quando o script é executado várias vezes com a mesma base de dados.

🚀 Funcionalidades

Abertura automática do navegador

Login automático no sistema

Leitura de produtos a partir de um arquivo CSV

Preenchimento automático de formulário

Controle de histórico para não cadastrar produtos repetidos

Criação automática de arquivo de controle (produtos_cadastrados.csv)

Scroll automático para continuar o cadastro

🛠️ Tecnologias Utilizadas

Python 3

PyAutoGUI – automação de teclado e mouse

Pandas – leitura e manipulação de dados

OS – verificação e criação de arquivos

Time – controle de tempo entre ações

📂 Estrutura do Projeto
📁 automacao-cadastro-produtos
│
├── automação_cadastro_produtos.py
├── produtos.csv
├── produtos_cadastrados.csv   # criado automaticamente
└── README.md

📄 Arquivo produtos.csv

A base de dados deve conter as seguintes colunas:

codigo,marca,tipo,categoria,preco_unitario,custo,obs


Exemplo:

123,Apple,Notebook,Eletrônicos,5000,4200,Produto premium

🧠 Como funciona o controle de duplicidade

Cada produto é identificado pelo campo codigo

Após o cadastro, o código é salvo no arquivo:

produtos_cadastrados.csv


Antes de cadastrar um produto, o script verifica:

Se o código já existe → pula

Se não existe → cadastra

Isso permite executar a automação várias vezes sem duplicar dados.

▶️ Como executar o projeto

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


Instale as dependências:

pip install pyautogui pandas


Ajuste as coordenadas (x e y) conforme sua resolução de tela

Execute o script:

python automação_cadastro_produtos.py

🛑 Como parar a automação em caso de erro

Mova o mouse rapidamente para o canto superior esquerdo da tela

Ou pressione Ctrl + C no terminal

O PyAutoGUI possui um sistema de segurança (failsafe) ativado por padrão.

⚠️ Observações Importantes

As coordenadas do mouse variam de acordo com a resolução da tela

Execute a automação sem usar o computador durante o processo

O site utilizado é apenas para fins educacionais

📌 Objetivo do Projeto

Este projeto tem como objetivo praticar automação com Python, lógica de programação e controle de dados, simulando um cenário real de automação de sistemas.

📄 Licença

Este projeto é apenas para fins educacionais.
