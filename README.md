# Projeto Agenda

## Descrição

Projeto Agenda é uma aplicação web para gerenciamento de contatos pessoais. Qualquer usuário pode criar uma conta, fazer login, e realizar operações de criação, leitura, atualização e exclusão (CRUD) tanto do seu perfil quanto dos contatos armazenados.

## Funcionalidades

- Cadastro de usuários (registro)
- Login e logout de usuários
- CRUD de usuários (atualização do perfil)
- CRUD de contatos pessoais

## Tecnologias Utilizadas

- Django (backend)
- HTML e CSS (frontend)
- SQLite (banco de dados padrão)
  
## Estrutura do Projeto

- `Agenda/`  
  - `base_static/` — arquivos estáticos, principalmente CSS  
  - `base_templates/` — templates base em HTML  
  - `contact/` — app principal com migrations, templates, views, forms, models e urls  
  - `project/` — configurações do Django (settings, urls, etc)

## Requisitos

- Python (versão conforme especificada no `requirements.txt`)
- Dependências listadas no arquivo `requirements.txt`

## Como rodar localmente

1. Crie e ative um ambiente virtual (venv):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

2. Instale as denpendências:

   ```bash
   pip install -r requirements.txt

3. Rode o servidor de desenvolvimento:

   ```bash
   python manage.py runserver

4. Acesse o sistema pelo navegador em:

   ```bash
    http://127.0.0.1:8000/

