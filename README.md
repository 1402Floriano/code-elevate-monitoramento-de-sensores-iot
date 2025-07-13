# Sistema de Monitoramento de Sensores IoT

Este projeto implementa um sistema simples e funcional de monitoramento de sensores IoT em tempo real, utilizando Python, Kafka, Docker e um banco de dados SQLite. O sistema simula dados de dois sensores IoT, envia esses dados para um tópico Kafka (via Producer), consome os dados para processamento (via Consumer) e os armazena em um banco de dados local.

## Objetivo
Atender ao desafio de criar um sistema de monitoramento IoT com as seguintes funcionalidades:
- **Producer**: Gera dados falsos de sensores (temperatura e umidade) e os envia para um tópico Kafka.
- **Consumer**: Consome os dados do tópico Kafka e os salva em um banco de dados SQLite.
- **Ambiente**: Utiliza Docker para configurar e rodar Kafka e Zookeeper.

## Pré-requisitos
Antes de iniciar, certifique-se de que os seguintes itens estão instalados na sua máquina:
- **Docker**: Necessário para rodar Kafka e Zookeeper. Baixe e instale pelo site oficial [Docker](https://www.docker.com/get-started/). Certifique-se de que o Docker Desktop (no Windows/Mac) ou o Docker Engine (no Linux) está funcionando.
- **Python 3.x**: Necessário para executar os scripts do Producer e Consumer. Baixe e instale pelo site oficial [Python](https://www.python.org/downloads/).
- **Git (opcional)**: Para clonar o projeto, se aplicável. Caso contrário, os arquivos podem ser baixados manualmente.

## Estrutura do Projeto
O projeto está organizado da seguinte forma:
```
code-elevate-monitoramento-de-sensores-iot/
│
├── consumer.py # Script Python para consumir dados do Kafka e salvar no banco de dados
├── docker-compose.yml # Configuração do Docker para Kafka e Zookeeper
├── producer.py # Script Python para gerar e enviar dados de sensores ao Kafka
├── README.md # Documentação do projeto
└── view_tb_monitoramento.py # Script python para executar visualização automatica do SQLite
```
Após a execução, um arquivo `bd_sensores.db` será criado no diretório para armazenar os dados dos sensores.

## Instalação
Siga os passos abaixo para configurar o ambiente e preparar o projeto para execução.

### 1. Baixar ou Clonar o Projeto
- Se estiver usando Git, clone o repositório (se aplicável) ou copie os arquivos para um diretório local.
- Caso contrário, crie uma pasta chamada `code-elevate-monitoramento-de-sensores-iot` e adicione os arquivos fornecidos (`docker-compose.yml`, `producer.py`, `consumer.py` e `README.md`).

### 2. Instalar Dependências do Python
- Abra um terminal (Prompt de Comando, PowerShell ou Terminal, dependendo do sistema operacional) no diretório do projeto.
- Instale as bibliotecas Python necessárias para os scripts:
    ```bash
    pip install kafka-python faker
Isso instalará as bibliotecas kafka-python (para interação com Kafka) e faker (para geração de dados falsos).

### 3. Verificar o Docker
- Certifique-se de que o Docker está instalado e rodando. No terminal, execute:
    ```bash
    docker --version
Se o comando retornar a versão do Docker, está tudo certo. Caso contrário, instale o Docker conforme mencionado nos pré-requisitos.

## Configuração e Execução
Siga os passos abaixo para configurar o ambiente Kafka e executar o sistema de monitoramento.

### 1. Iniciar Kafka e Zookeeper com Docker
- No diretório do projeto (onde está o docker-compose.yml), execute o comando abaixo para iniciar os serviços Kafka e Zookeeper em background:
    ```bash
    docker-compose up -d
- Aguarde cerca de 30 segundos a 1 minuto para que os serviços iniciem completamente.
- Verifique se os serviços estão rodando corretamente:
    ```bash
    docker-compose ps
- Você deve ver dois serviços listados: kafka e zookeeper, ambos com status Up. Caso contrário, consulte a seção "Solução de Problemas" abaixo.

### 2. Executar o Producer
- Abra um terminal no diretório do projeto e execute o script do Producer para começar a enviar dados falsos de sensores ao Kafka:
    ```bash
    python producer.py
- Você verá mensagens no terminal indicando que os dados estão sendo enviados, como _Dados enviados do sensor 1: {...}_. O Producer enviará dados a cada 5 segundos.
- Deixe este terminal aberto enquanto o Producer estiver rodando.

### 3. Executar o Consumer
- Abra um segundo terminal no mesmo diretório do projeto e execute o script do Consumer para consumir os dados do Kafka e salvá-los no banco de dados SQLite:
    ```bash
    python consumer.py
- Você verá mensagens no terminal indicando que os dados estão sendo salvos, como _Dados salvos no banco: {...}_.
- Deixe este terminal aberto enquanto o Consumer estiver rodando.

### 4. Parar a Execução
- Para parar o Producer ou o Consumer, pressione Ctrl + C no terminal correspondente.
- Para parar os serviços Docker (Kafka e Zookeeper), execute no diretório do projeto:
    ```bash
    docker-compose down

## Visualização dos Dados
Os dados consumidos pelo consumer.py são salvos em um banco de dados SQLite chamado `bd_sensores.db` no diretório do projeto. Para visualizar esses dados, siga uma das opções abaixo.

### Opção 1: Usar uma Ferramenta Gráfica (Recomendado)
- Baixe e instale o DB Browser for SQLite, uma ferramenta gratuita e fácil de usar: [DB Browser for SQLite](https://sqlitebrowser.org/dl/)
- Abra o programa, clique em "Open Database" e selecione o arquivo `bd_sensores.db` no diretório do projeto.
- Vá até a aba "Browse Data" e selecione a tabela `tb_monitoramento` para ver os dados salvos (colunas: id, id_sensor, temperatura, umidade, dt_hr).

### Opção 2: Usar o SQLite via Terminal
- Se o SQLite estiver instalado, abra um terminal no diretório do projeto e execute:
    ```bash
    sqlite3 bd_sensores.db
- Dentro do SQLite, execute a consulta:
    ```sql
    SELECT * FROM tb_monitoramento LIMIT 10;
Isso mostrará os primeiros 10 registros salvos.
- Para instalar o SQLite no Windows, baixe os binários em [SQLite Download Page](https://www.sqlite.org/download.html) e siga as instruções de configuração no PATH.

### Opção 3: Usar um Script Python Simples
- Crie um arquivo chamado view_data.py no diretório do projeto com o seguinte conteúdo:
    ```python
    import sqlite3

    # Conectar ao banco de dados
    conn = sqlite3.connect('bd_sensores.db')
    cursor = conn.cursor()

    # Consultar os primeiros 10 registros
    cursor.execute('SELECT * FROM tb_monitoramento LIMIT 10')
    rows = cursor.fetchall()

    # Exibir os dados
    print("Dados salvos no banco de dados (primeiros 10 registros):")
    for row in rows:
        print(row)

    # Fechar a conexão
    conn.close()
- Execute o script com:
    ```python
    python view_tb_monitoramento.py
Isso mostrará os dados diretamente no terminal.
