# Dados históricos sobre covid-19

Construção de uma api(restful) para fornecer dados históricos sobre a evolução dos casos e número de óbitos do covid-19 nos estados do Brasil

## Instalação

Faça um fork do projeto e clone para sua máquina

### Pré-requisitos

<ul>
  <li>Phython3</li>
  <li>Pip3</li>
  <li>Virtualenv</li>
</ul>

### Bibliotecas utilizadas
<ul>
  <li>Flask</li>
  <li>Flask-Cors</li>
  <li>Flask-Restplus</li>
  <li>requests</li>
</ul>

### Instalação de dependências
Na raiz do projeto execute os seguintes comandos
```
  source middleware-covid/bin/activate
```
```
  pip3 install requirements.txt
```

### Executando o projeto
Na raiz do projeto execute
```
python3 app.py
```
Para verificar se ocorreu tudo certo acesse este link:
[localhost:5000](http://localhost:5000)
<br>
Se ocorreu tudo certo você deve visualizar a documentação da api

### Consultando dados
Desenvolvimento
```
http://localhost:5000/api/data/?initialDate=yyyy-MM-dd&lastDate=yyyy-MM-dd&uf=uf
```
Produção
```
https://middleware-covid19.herokuapp.com/api/data/?initialDate=yyyy-MM-dd&lastDate=yyyy-MM-dd&uf=uf
```
### Site
[dashboard-covid19](https://nostalgic-beaver-d44652.netlify.app)

### Base de dados
[covid19-brazil-api](https://github.com/devarthurribeiro/covid19-brazil-api)

## Contribuidores

* **Alan Fernandes** - *Perfil github* - [alanfernandes63](https://github.com/alanfernandes63)
