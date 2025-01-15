# PSW-12

### Introdução

Durante o evento Pystack Week - Returnal, pude aprimorar meu conhecimento sobre Python e ter meus primeiros contatos com o framework backend Django por meio de alguns projetos. O objetivo deste repositório é, além de agradecer a Caio Sampaio pela oportunidade, compartilhar meus resultados e tornar possível a visualização dessas ideias para aqueles que não acompanharam o evento.

Utilizando a arquitetura MVT - Models, Views e Templates

## Sobre os projetos

### Aula 1: Sistema de gerenciamento de assinaturas (Python puro e banco de dados)

#### Objetivo:

Quando possuimos assinaturas em diferentes serviços (como Netflix, Amazon Prime, GloboPlay e semelhantes), podemos facilmente nos perder e acabar esquecendo de pagar ou de cancelar alguma, o que dificulta o gerenciamento dos gastos. Este primeiro projeto objetiva funcionar como um gerenciador de assinaturas e seus pagamentos.

#### Funcionalidades:

- Adicionar e remover assinaturas;
- Adicionar e remover pagamentos;
- Consultar o valor gasto mensalmente com assinaturas;
- Visualizar um gráfico de seus gastos nos últimos doze meses.

#### Tecnologias utilizadas:

- Python 3.13.1
    - **Bibliotecas:**
    - SQLModel
    - Pillow
    - Matplotlib
    - PyQt5

#### Como rodar:

Abra uma janela do terminal de seu computador;

Abra a pasta onde deseja clonar este repositório por meio deste comando:

```
cd (caminho da pasta)
```
Digite o comando para clonar o repositório:
```
git clone https://github.com/juliasoares17/PSW-12.git
```
Para Windows:

```
python templates/app.py
```

Para Linux:

```
python3 templates/app.py
```


### Aula 2: Diário online (Aplicação Web com Python e Django)

#### Objetivo:

O objetivo principal deste segundo projeto é oferecer aos usuários uma ferramenta digital intuitiva para registrar seus pensamentos, experiências e memórias de forma organizada, um diário online. Por meio desta aplicação, os usuários podem acompanhar o decorrer de seus dias, identificar padrões e tendências em suas vidas, além de ter um espaço privado para refletir sobre suas jornadas.

#### Funcionalidades:

- Adicionar tags e marcar pessoas em suas anotações;
- Cadastrar pessoas novas;
- Pesquisar anotações por data;
- Visualizar gráficos que mostrar as pessoas e tags mais utilizadas;
