# PSW-12

### Introdução

Durante o evento Pystack Week - Returnal, pude aprimorar meu conhecimento sobre Python e ter meus primeiros contatos com o framework backend Django por meio de alguns projetos. O objetivo deste repositório é, além de agradecer a Caio Sampaio pela oportunidade, compartilhar meus resultados e tornar possível a visualização dessas ideias para aqueles que não acompanharam o evento.

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
Abra a pasta do primeiro projeto com este comando:
```
cd PSW-12/aula1-assinaturas
```
Antes de prosseguir para baixar as dependências, há a opção de criar um **ambiente virtual**. Não é uma etapa obrigatória, mas um ambiente virtual permite que você baixe as tecnologias utilizadas neste projeto sem deixá-las diretamente em seu computador, evitando possíveis conflitos.

Para criar um ambiente virtual, será necessário já ter o Python instalado em sua máquina. 

Para Windows:

- Baixe o instalador do Python:

  - Acesse [python.org/downloads](https://www.python.org/downloads/).
  - Escolha a versão desejada e baixe o instalador compatível com o Windows (a versão mais recente estará logo no começo da página)


- Execute o instalador:

  - Execute o arquivo baixado e marque a opção "Add Python to PATH" antes de prosseguir.

  - Escolha "Customize installation" se desejar personalizar as opções ou "Install Now" para uma instalação padrão.

- Abra o Prompt de Comando e verifique a instalação:

    ```
    python --version
    ```
    Deve retornar a versão instalada. Caso contrário, revise a configuração do PATH.

- Crie e ative o ambiente (dentro da pasta do projeto):
    ```
    python -m venv nome_do_ambiente
    ```
    ```
    nome_do_ambiente\Scripts\Activate   
    ```
    Você verá o nome do ambiente virtual no início da linha do terminal.

<br>
Para Linux:

Em distribuições modernas, o Python pode vir pré-instalado. Verifique com:
```
python3 --version
```
Caso não esteja instalado, prossiga com os próximos passos.

- Instale o Python com o gerenciador de pacotes da sua distribuição:

  - Debian/Ubuntu:

    ```
    sudo apt update
    sudo apt install python3 python3-pip
    ```
  - Fedora:

     ```
    sudo dnf install python3 python3-pip
    ```
- Verifique a instalação:
    ```
    python3 --version
    ```
    Deve retornar a versão instalada.

- Crie e ative o ambiente virtual (dentro da pasta do projeto):
    ```
    python3 -m venv nome_do_ambiente
    ```
    ```
    source nome_do_ambiente/bin/activate
    ```
    Você verá o nome do ambiente virtual no início da linha do terminal.
<br>
<br>

Após seguir os passos adequados para o seu sistema operacional, com o ambiente ativado, baixe as dependências do projeto:
```
pip install -r requirements.txt 
```
Por fim, rode o arquivo "app.py" do diretório "templates":

Para Windows:
```
python templates/app.py
```
Para Linux:
```
python3 templates/app.py
```

Você poderá interagir com o projeto por meio de seu terminal.

### Aula 2: Diário online (Aplicação Web com Python e Django)

#### Objetivo:

O objetivo principal deste segundo projeto é oferecer aos usuários uma ferramenta digital intuitiva para registrar seus pensamentos, experiências e memórias de forma organizada, um diário online. Por meio desta aplicação, os usuários podem acompanhar o decorrer de seus dias, identificar padrões e tendências em suas vidas, além de ter um espaço privado para refletir sobre suas jornadas.

#### Funcionalidades:

- Adicionar tags e marcar pessoas em suas anotações;
- Cadastrar pessoas novas;
- Pesquisar anotações por data;
- Visualizar gráficos que mostram as pessoas mais marcadas e as tags mais utilizadas;

#### Tecnologias utilizadas:

- Python 3.13.1
    - **Bibliotecas:**
    - Pillow
    - Django

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
Abra a pasta do segundo projeto:
```
cd PSW-12/aula2-diario
```
Siga os passos para criar e ativar o ambiente virtual (opcional);

Baixe as dependências:
```
pip install -r requirements.txt 
```
No caso deste projeto, será necessário rodar e interrompê-lo uma vez para que o banco de dados seja gerado corretamente. Para isso, digite o seguinte comando:

Para Windows:
```
python manage.py runserver
```
Para Linux:
```
python3 manage.py runserver
```
Aperte CTRL + C para interrompê-lo em seguida.

Para garantir que todas as tabelas necessárias surgirão, digite o comando:

Para Windows:
```
python manage.py migrate
```

Para Linux:
```
python3 manage.py migrate
```
E rode o projeto novamente:

Para Windows:
```
python manage.py runserver
```
Para Linux:
```
python3 manage.py runserver
```
<<<<<<< HEAD


## Conclusão

A Pystack Week - Returnal certamente foi um evento que agregou muito ao meu portifólio na área da tecnologia. Algumas horas de esforço que certamente valeram à pena.

### Próximos passos
#### - Adicionar o terceiro projeto ao repositório;  
Caio Sampaio, ao todo, guiou a codificação de três projetos durante a PSW, porém meu terceiro projeto, que trata-se de um encurtador de links, está enfrentando um pequeno problema relacionado à função de gerar QR code. Resolverei-o o quanto antes para poder adicioná-lo a este repositório.

#### - Customizar o segundo projeto;  
O projeto do diário online envolve HTML e CSS, e a aparência atual dele é a padrão, que foi ensinada pelo próprio Caio durante o evento. No entanto, quando tiver a oportunidade em meio à minha rotina, pretendo customizar este projeto, tanto visualmente quanto com possíveis novas funcionalidades.

#### - Aperfeiçoar o gerador do gráfico do primeiro projeto;  
No gerenciador de assinaturas, há a funcionalidade de gerar um gráfico baseado nos gastos do usuário durante os últimos doze meses. No entanto, este gráfico não está perfeito visualmente. Pretendo torná-lo mais apresentável o mais rápido possível.

Novamente, agradeço ao Caio pela oportunidade e pela disponibilidade e paciência. Posso afirmar que esse evento foi uma ótima prática de minhas habilidades em Python e uma introdução extremamente agradável ao framework Django. Estou ansiosa para desenvolver mais aplicações combinando essas duas tecnologias.