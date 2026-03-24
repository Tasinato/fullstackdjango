# 🚀 Fullstack Django Project

Projeto desenvolvido com Django para estudo e construção de aplicações web completas, seguindo boas práticas de desenvolvimento, organização e versionamento.

---

## 📦 Tecnologias

- Python 3.14
- Django 6
- Poetry
- SQLite (desenvolvimento)

---

## 📁 Estrutura do Projeto

    fullstackdjango/
    │
    ├── mysite/            # Configuração principal do Django
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    │
    ├── polls/             # App principal (exemplo)
    │   ├── models.py
    │   ├── views.py
    │   ├── admin.py
    │   └── migrations/
    │
    ├── manage.py
    ├── pyproject.toml
    └── .gitignore

---

## ⚙️ Setup

### 1. Clonar repositório

    git clone https://github.com/Tasinato/fullstackdjango.git
    cd fullstackdjango

---

### 2. Instalar dependências

    poetry install

---

### 3. Ativar ambiente

    poetry shell

---

### 4. Rodar migrations

    python manage.py migrate

---

### 5. Executar servidor

    python manage.py runserver

Acesse: http://127.0.0.1:8000/

---

## 🛠️ Admin

Criar superusuário:

    python manage.py createsuperuser

Acessar: http://127.0.0.1:8000/admin/

---

## 📊 Models

### Question
- Texto da pergunta
- Data de publicação

### Choice
- Relacionamento com Question
- Texto da opção
- Contador de votos

---

## 🔗 Relacionamento

- 1 Question → N Choices

---

## 🧠 Boas práticas

- Uso de __str__ nos models
- Migrations versionadas
- .gitignore configurado corretamente
- Estrutura padrão Django
- Ambiente isolado com Poetry

---

## 🚀 Próximos passos

- Criar views e rotas (/polls/)
- Templates HTML
- Sistema de votação
- PostgreSQL
- Deploy

---

## 👨‍💻 Autor

Rafael Tasinato
