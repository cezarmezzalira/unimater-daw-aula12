# Conteúdo desta aula

- Criação de uma API REST usando o framework FastAPI

## Criando um projeto novo

Vamos criar via terminal uma pasta nova para o nosso projeto:

```bash
mkdir aula12-api-rest-pratica
```

Em seguida, vamos abrir a nossa pasta com o Visual Studio Code:

```bash
code aula12-api-rest-pratica
```

## Configurando o ambiente

Em seguida, o que temos que fazer é configurar nosso projeto com um ambiente virtual, para termos um projeto apenas com as bibliotecas que ele precisa.

Para isso, com a pasta do nosso projeto aberta no VS Code, vamos abrir o terminal e digitar o comando abaixo:

```bash
python -m venv .venv
```

Ao executar esse comando, o VS Code irá detectar o novo ambiente virtual e irá ativa-lo automaticamente.

## Criando o projeto e inicializando o repositório git

Na raiz do projeto, vamos criar uma pasta chamada src. 

Dentro dela vamos criar uma pasta chamada app.

Em seguida, vamos criar um arquivo chamado `__main__.py`

Esse arquivo será o ponto de entrada da nossa aplicação Python.

### Inicializando o repositório git

No terminal, vamos digitar o seguinte comando:

```bash
git init
```

Em seguida, vamos criar um arquivo chamado `.gitignore` na raiz do nosso projeto e copiar o arquivo que está neste [link](https://github.com/github/gitignore/blob/main/Python.gitignore).

Este arquivo faz com que a nossa pasta .venv e outros arquivos que estão na raiz do projeto sejam ignorados pelo git.

Agora, vamos fazer nosso primeiro commit, adicionando todos os arquivos, através dos comandos abaixo:

```bash
git add .
git commit -m "Commit inicial"
```
