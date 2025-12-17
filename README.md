# UniControl
Unified Linux & Windows Management Platform
📘 UniControl

Unified Linux & Windows Asset Management System

UniControl is a centralized asset management and compliance tracking system designed to manage Linux and Windows machines from a single control plane. It provides a REST API, Admin UI, and is built with Django + Django REST Framework.

🚀 Features

📋 Centralized asset inventory

🖥️ Supports Linux & Windows systems

🔐 Django Admin dashboard

🔁 REST API for automation & integrations

🧩 Modular apps (assets, policies, audit, users)

🕒 Asset lifecycle tracking (created, updated, status)

⚙️ Ready for Ansible / Agent-based extensions

🏗️ Architecture Overview

UniControl
│
├── assets/        # Asset inventory & models
├── audit/         # Audit logs (future)
├── policies/      # Compliance policies (future)
├── users/         # RBAC & user management
│
├── unicontrol/    # Core Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .gitignore

🛠️ Tech Stack
Layer	Technology
Backend	Django 6.0
API	Django REST Framework
Database	SQLite (dev)
Admin UI	Django Admin
OS	Linux / Windows
Version Control	Git & GitHub

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/Sourav-777/unicontrol.git
cd unicontrol/backend

2️⃣ Create virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Create admin user
python manage.py createsuperuser

6️⃣ Run server
python manage.py runserver

🌐 Access URLs
Purpose	URL
Admin Panel	http://127.0.0.1:8000/admin/

Asset API	http://127.0.0.1:8000/api/assets/
📡 Example API Response
[
  {
    "hostname": "linux-server-01",
    "os_type": "linux",
    "ip_address": "10.0.0.25",
    "owner": "IT Team",
    "status": "active",
    "compliance_status": false,
    "created_at": "2025-12-18T00:25:10Z"
  }
]

🔒 Security & Future Enhancements

🔐 Role-Based Access Control (RBAC)

🛡️ Compliance policy engine

📊 Audit logs

🧠 Agent-based data collection

🐳 Docker support

🌐 Frontend dashboard (React)

👨‍💻 Author

Sourav Mohapatra
Backend / Infrastructure Enthusiast
GitHub: https://github.com/Sourav-777

📄 License

This project is licensed under the MIT License.
