# Todo-List-using-Django

<img width="1709" height="849" alt="Screenshot 2026-03-19 at 1 57 56 AM" src="https://github.com/user-attachments/assets/a3e281aa-29cf-4a14-9b6c-e6be95eab46d" />


#  Django Todo App

A clean, user-authenticated Todo List web application built with **Django**. Each user can manage their own private tasks — create, complete, and delete todos with a simple interface.

---

##  Features

- 🔐 User authentication — signup, login, and logout
- 📝 Create todos with a title
- ✅ Toggle todos as complete / incomplete
- 🗑️ Delete todos
- 👤 Each user only sees their own todos
- 🛡️ Login-protected todo page
- 🔧 Django Admin panel support

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite (default) |
| Auth | Django built-in authentication |
| Frontend | Django templates (HTML) |
| Deployment | ASGI-ready |

---

## 📁 Project Structure

```
todo/
│
├── todo/                   # Django project config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── todo_app/               # Main app
│   ├── models.py           # Todoo model
│   ├── views.py            # signup, login, todo, logout views
│   ├── admin.py            # Admin panel config
│   └── templates/
│       ├── signup.html
│       ├── login.html
│       └── todo.html
│
└── manage.py
```

---

##  Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for Admin panel)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  URL Routes

| URL | View | Description |
|---|---|---|
| `/signup` | `signup` | Register a new account |
| `/login` | `login_view` | Log in to your account |
| `/todo` | `todo_view` | Your personal todo list |
| `/logout` | `logout_view` | Log out |
| `/admin` | Django Admin | Admin panel |

---

##  Data Model

### `Todoo`

| Field | Type | Description |
|---|---|---|
| `title` | CharField | Title of the task (max 100 chars) |
| `description` | TextField | Optional description |
| `completed` | BooleanField | Done status (default: False) |
| `user` | ForeignKey | Owner (linked to Django User) |
| `created_at` | DateTimeField | Creation timestamp |
| `updated_at` | DateTimeField | Last updated timestamp |

---

## 🔒 Authentication Flow

1. User signs up → automatically logged in → redirected to `/todo`
2. Login with username & password → redirected to `/todo`
3. Accessing `/todo` without login → redirected to `/login`
4. Logout → redirected to `/login`

---

##  Admin Panel

The admin panel is customized for the `Todoo` model:

- Displays: title, completion status, user, and creation date
- Filterable by: completion status, user, and date
- Searchable by: title and description
- Superusers see all todos; staff see only their own

Access at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📌 Future Improvements

- [ ] Add due dates to todos
- [ ] Priority levels (low / medium / high)
- [ ] Edit todo title inline
- [ ] REST API with Django REST Framework
- [ ] Deploy to Railway / Render / Heroku

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by [Your Name](https://github.com/your-username)
