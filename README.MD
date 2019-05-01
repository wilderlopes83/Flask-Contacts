Baseado no curso disponível em: https://www.youtube.com/playlist?list=PLZ8sofC1-EAYdK1uCVBuBe8MWe6RvZ8Sb


- Para funcionar o sistema, é necessário instalar o pipenv (depende do pip3 instalado):

    sudo pip3 install pipenv

- Depois, criar o ambiente virtual:

    pipenv --three

- Próximo passo, é ativar o ambiente virtual
    
    pipenv shell

Com o ambiente virtual funcionando, instalações de componentes etc serão isolados da instalação da máquina.

- instalando dependencias com pipenv
   pipenv install Flask-RESTful==0.3.7
   pipenv install Flask-SQLAlchemy==2.3.2

- para criar um ambiente shell de interação do flask:
   flask shell

# tive problema durante muito tempo para conseguir instalar o psycopg2 (pipenv install psycopg2==2.8.2). Depois de muito pesquisar, descobri que estava faltando a dependência para o python 3.7, que é a versão utilizada no target do arquivo PipFile. Comando para instalar sudo apt-get install python3.7-dev

#obs: Para funcionar, é necessário setar as variáveis de ambiente abaixo. Pesquisar como automatizar isso

- setando variavel de ambiente:
    export FLASK_APP=main.py

- para configurar como ambiente de desenv:
   export FLASK_ENV=development

- para rodar a aplicação
   flask run

- para rodar o migrate
   - flask db init  
   - flask db migrate 
   - flask db upgrade


#Comando para rodar Postgres no Docker:
---rodar instancia do Postgres

docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $media/wilder/HDD-DADOS/docker-volumes/volumes/postgres:/var/lib/postgresql/data  postgres

--conectar via psql
psql -h localhost -U postgres -d postgres   (senha docker)   