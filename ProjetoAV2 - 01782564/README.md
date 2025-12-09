# Projeto AV2 - Django (esqueleto)

Pequeno projeto Django de exemplo para a tarefa AV2.

Conteúdo:
- App `gestao` com modelos `Cliente` e `Pedido`.
- Operações CRUD para ambos os modelos (List, Create, Detail, Update, Delete).

Setup (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

URLs principais (após `runserver`):
- `http://127.0.0.1:8000/` -> lista de clientes (página inicial)
- `http://127.0.0.1:8000/admin/` -> admin Django

Observações:
- Este repositório contém apenas um esqueleto; execute os comandos acima para instalar dependências e iniciar o servidor.
