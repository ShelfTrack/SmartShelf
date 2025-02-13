ShelfTrack/                     # 🌟 Root Project Directory
│── backend/                     # 📂 Django Backend
│   │── core/                     # 📂 Main Django App
│   │   │── migrations/           # 📂 Django Migrations
│   │   │   ├── __init__.py       # 📝 Required for Python module
│   │   ├── __init__.py           # 📝 Marks `core` as a module
│   │   ├── admin.py              # ⚙️ Django Admin Configuration
│   │   ├── apps.py               # ⚙️ App Configuration
│   │   ├── models.py             # 📊 Database Models
│   │   ├── views.py              # 🎭 Business Logic
│   │   ├── urls.py               # 🌍 API Routing
│   │   ├── serializers.py        # 🔗 Django REST Framework Serializers (Optional)
│   │   ├── tests.py              # 🧪 Unit Tests
│   │── __init__.py               # 📝 Marks `backend` as a module
│   │── manage.py                 # 🏗 Django Management Script
│   │── settings.py               # ⚙️ Django Settings
│   │── urls.py                   # 🌍 Project URLs
│   │── wsgi.py                   # 🚀 Web Server Gateway Interface
│   │── asgi.py                   # 🚀 Async Server Gateway Interface (Optional)
│── frontend/                     # 📂 PyQt6 Frontend
│   │── main.py                    # 🖥️ PyQt6 Main GUI Application
│   │── ui/                        # 📂 UI Files (if using .ui XML files)
│   │   ├── main_window.ui         # 🎨 Qt Designer UI File (Optional)
│   │── assets/                    # 🎨 Icons, Images, and Stylesheets
│   │   ├── logo.png               # 🖼 Logo for Software
│   │   ├── styles.qss             # 🎨 Stylesheet for PyQt6
│   │── components/                # 📂 Reusable UI Components
│   │   ├── sidebar.py             # 📜 Sidebar Menu (Optional)
│── database/                     # 📂 Database Files (Optional for SQLite)
│   │── db.sqlite3                 # 🗄 SQLite Database (If Used)
│── scripts/                      # 📂 Utility Scripts (Optional)
│   │── backup.py                  # 🔄 Database Backup Script
│── docs/                         # 📂 Documentation
│   │── README.md                  # 📖 Project Overview
│   │── CONTRIBUTING.md             # 🙌 Contribution Guidelines
│── .github/                       # 🤖 GitHub Configuration Files
│   │── workflows/                 # 🔄 GitHub Actions CI/CD
│   │── dependabot.yml              # 🛠 Dependency Updates
│── .gitignore                     # 🚫 Git Ignore Unwanted Files
│── requirements.txt               # 📜 Python Dependencies
│── LICENSE                        # ⚖️ Open Source License
│── README.md                      # 📖 Project Documentation
