<h1 align="center">
chatterbox
</h1>
<p align="center">
<img alt="last commit" src="https://img.shields.io/github/last-commit/grvela/chatterbox?color=blue">
<img alt="made by rodrigo" src="https://img.shields.io/badge/made_by-rodrigo-blue">
<img alt="progress" src="https://img.shields.io/badge/status-in_progress-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-blue">
</p>
<h4 align="center">
		<a href="#pencil-sobre-o-projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#rocket-stack">Stack</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#blue_book-configurando-ambiente">Configurando ambiente</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#dart-rodando-aplicação">Rodando aplicação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
		<a href="#clipboard-contato">Contato</a>
</h4>

 
 ## :pencil: Sobre o projeto 
**Resumo**: Este projeto é um exemplo de integração das tecnologias: Flask, Firebase e Rasa.

**Tema**:  
O dono de uma grande pizzaria local pediu para você, que projetasse um site para divulgar sua franquia. 
Ele precisa que você mostre as principais informações e serviços de seu restaurante.
Além de atrair mais clientes, ele deseja automatizar algumas funções.
O seu trabalho é desenvolver um assistente virtual capaz de atender os pedidos e encaminha-los para produção.
Espera-se que o chatbot envie todas as requisições já feitas para um banco de dados afim de serem armazenadas e visualizadas na pagina inicial do site.

**Objetivo**: 
Demonstrar o uso de chatbots em aplicações web 

## :rocket: Stack
<p align="center">
<img alt="flask" src="https://img.shields.io/badge/flask-backend-blue?style=for-the-badge&logo=flask">
<img alt="rasa" src="https://img.shields.io/badge/rasa-backend-blue?style=for-the-badge&logo=dependabot">
</p>
<p align="center">
<img alt="html" src="https://img.shields.io/badge/html-frontend-red?style=for-the-badge">
<img alt="css" src="https://img.shields.io/badge/css-frontend-red?style=for-the-badge">
<img alt="js" src="https://img.shields.io/badge/javascript-frontend-red?style=for-the-badge">
</p>
<p align="center">
	<img alt="fetch api" src="https://img.shields.io/badge/fetch api-rest-green?style=for-the-badge">
</p>
<p align="center">
	<img alt="firebase" src="https://img.shields.io/badge/firebase-database-FFCA28?style=for-the-badge&logo=firebase">
</p>

## :blue_book: Configurando ambiente

  
Antes de começar, é preciso ter duas ferramentas instaladas:
- **Pyenv** :  Permite que você instale outras versões do python em sua máquina
- **Virtualenv**: Permite criar ambientes virtuais em sua máquina
 
 Instalação:
 ```bash
 # clone o projeto
 git https://github.com/grvela/chatterbox.git
 # entre na pasta do projeto
 cd chatterbox/
 # instale esta versão do python 
 pyenv install 3.7.2
 # crie uma máquina virtual a partir dela
 virtualenv -p ~/.pyenv/versions/3.7.2/bin/python nome_da_máquina_virtual
 # ative sua máquina virtual
 source nome_da_máquina_virtual/bin/activate
 # instale as tecnologias utilizadas
 pip install -r requeriments.txt
```
  

## :dart: Rodando aplicação

Para utilizar os recursos do bot é preciso treina-lo:
```bash
# chatterbox/chat
rasa train
```
Feito isso, utilizaremos três terminais. Cada um rodando um serviço diferente. Note o diretório em que cada comando dever ser executado.

No terminal um:
```bash
# chatterbox/chat
rasa run actions
```
No terminal dois:
```bash
# chatterbox/chat
rasa run actions
```
No terminal três:
```bash
# chatterbox/
python run.py
```
  

## :clipboard: Contato

[![](https://img.shields.io/badge/linkedin-rodrigo-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rodrigo-andr%C3%A9-a504a3195/
)



