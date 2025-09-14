# 🚀 Projeto Django: Book Manager API

Este é um projeto Django que consiste em um aplicativo RESTful utilizando **Django REST Framework**. O projeto permite que usuários criem contas, façam login, e gerenciem uma **coleção de livros** consumindo dados de uma API pública (Open Library API).  

---

## 🌟 Funcionalidades

- **Cadastro de Usuários:** Permite criar novos usuários com autenticação segura. 👤  
- **Login e Autenticação JWT:** Usuários recebem tokens JWT para acessar endpoints protegidos. 🔑  
- **Adicionar Livros à Coleção:** Busca livros pelo título na Open Library API e adiciona à coleção do usuário. 📚  
- **Remover Livros da Coleção:** Permite remover livros da coleção do usuário. ❌  
- **Visualizar Coleção:** Listagem de todos os livros adicionados pelo usuário. 📝  

---

## 🛠️ Tecnologias Utilizadas

- **Django:** Framework web utilizado para construir a aplicação. 🐍  
- **Django REST Framework:** Biblioteca para construção de APIs RESTful. 🔧  
- **Open Library API:** API pública para buscar informações de livros. 📖  
- **JWT (JSON Web Token):** Para autenticação e autorização segura. 🔐  

---

## 🛠️ Instalação e Configuração do Projeto  

Siga os passos abaixo para configurar e executar o projeto localmente.

### 🔄 1. Clonar o Repositório

```bash
git clone https://github.com/leodymann/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2
```

### 2️⃣ Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
```

### 3️⃣ Ative o ambiente virtual:

- No Windows:
```bash
venv\Scripts\activate
```
- No macOS/Linux:
```bash
source venv/bin/activate
```

### 4️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5️⃣ Aplicar Migrações do Banco de Dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Criar Superusuário

```bash
python manage.py createsuperuser
```
- Siga as instruções para definir username,email e senha.

### 7️⃣ Rodar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```
- O servidor ficará disponível em:
```bash
http://127.0.0.1:8000/
```

### 8️⃣ Testar a API
## 📌 Rotas da API

Aqui estão os principais endpoints disponíveis no projeto.

| Método | Endpoint                                          | Autenticação      | Descrição |
|--------|---------------------------------------------------|-------------------|-----------|
| **GET**    | `/api/books/search/?title=<titulo>`                | ✅ Obrigatória    | Busca livros na Open Library a partir de um título. |
| **GET**    | `/api/books/collections/`                          | ✅ Obrigatória    | Lista todos os livros da coleção do usuário autenticado. |
| **POST**   | `/api/books/collections/add/`                      | ✅ Obrigatória    | Adiciona um livro à coleção do usuário. |
| **DELETE** | `/api/books/collections/<id>/remove/`              | ✅ Obrigatória    | Remove um livro específico da coleção do usuário. |
| **POST**   | `/api/users/register/`                             | ❌ Não requerida | Registra um novo usuário. |
| **POST**   | `/api/token/`                                      | ❌ Não requerida | Gera token de autenticação (JWT ou SimpleJWT). |

---

### 🔑 Notas sobre autenticação
- Os endpoints marcados como **Obrigatória** requerem envio de token de autenticação.  
- Exemplo de header:  
  ```http
  Authorization: Bearer <SEU_TOKEN>

```bash
✅ Pronto! Agora você já pode usar a API Book Manager com autenticação JWT e gerenciamento de coleção de livros.
```
