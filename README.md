# Teste IntuitiveCare

Este projeto foi desenvolvido como parte do processo seletivo da IntuitiveCare. Ele consiste em 4 testes de diferentes especialidades.

## Tecnologias Utilizadas

- Python 3.12 ou superior

## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou o Python 3.12 ou superior

## Instalação

### 1. Clone este repositório:

   ```bash
   git clone https://github.com/LucasPerrone21/TesteIntuitiveCare.git
   ```
### 2. Navegue até o diretório do projeto:

```bash
cd TesteIntuitiveCare
```
  
### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:
```bash
venv\Scripts\activate
```

No Unix ou MacOS:
```bash
source venv/bin/activate
```

### 5. Instale as depêndencias
```bash
pip install -r requirements.txt
```

## Uso

Para rodar o projeto basta executar os arquivos ```.py``` que estão nas pastas referentes a cada teste (com exceção do teste 4)

Exemplo:

```bash
python teste1/main.py
```
## Como rodar o teste 4

Para rodar o teste 4, basta acessar a pasta do teste 4 com o ```cd teste4``` e executar os comandos a partir do **passo 3**

Depois configure as variáveis de ambiente criando um arquivo ```.env``` e modificando as coisas dentro dele:
```env
POSTGRES_PASSWORD = '2105'
POSTGRES_USER = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432
POSTGRES_DB = 'db_ans'
```

## Documentação da API do teste 4

Rota para a tela em Vue.JS:
```
`http://localhost:8000/
```

Rota para listar as operadoras de acordo com um nome:

```
`http://localhost:8000/operators?name=nomeDaEmpresa
```

Rota para a documentação da API:

```
`http://localhost:8000/docs
```


