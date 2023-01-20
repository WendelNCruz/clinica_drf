
# Django Clínica

Sistema desenvolvido para construção de API. 

Tecnologias: Python, Django, Django REST framework, HTML, CSS e JavaScript.


# Dependências(Requirements)


- asgiref==3.5.2
- autopep8==2.0.1
- Django==4.1.4
- django-crispy-forms==1.14.0
- djangorestframework==3.14.0
- pycodestyle==2.10.0
- pytz==2022.6
- sqlparse==0.4.3
- tomli==2.0.1


## Instalação

Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y libxml2 gcc python3-dev libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo apt update
```

1 Gere um .env local


2 Instalar dependências:

```bash
pip install -r requirements.txt
```
3 Sincronize a base de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

4 Crie um usuário (Administrador do sistema):
```bash
python manage.py createsuperuser
```

5 Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):
```bash
python manage.py runserver
```

## Funcionalidades

- API (Interface de Programação de Aplicação) na qual
gestor da clínica (superusuário) poderá cadastrar: 
    - Especialidades
    - Médicos e
    - Disponibilizar horários para marcar as consultas.

- API com cinco  Endpoints.

- Restrições:
    - Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia
    - Não deve ser possível criar uma agenda para um médico em um dia passado
