# Medical Manager

Medical Manager is a management system for healthcare professionals, developed in Django. The system allows the registration and monitoring of patients, registration of appointments, management of tasks and sharing of information.

## 🚀 Features

- Patient registration and management
- Logging appointments with video upload
- Task system (todo) per query
- Patient mood record
- Public Query Sharing
- Payment status system
- Viewing Query History
- Generation of accompanying charts

## 📋 Pre requisites

- Python 3.x
- Django 5.1
- Pillow (for image manipulation)

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/Emicy963/medical-manager.git
cd medical-manager
```

2. Create a virtual environment
```bash
python -m venv .venv
```

3. Activate the virtual environment
```bash
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

4. Install the dependencies
```bash
pip install -r requirements.txt
```

5. Perform migrations
```bash
python manage.py migrate
```

6. Create a superuser
```bash
python manage.py createsuperuser
```

7. Start the server
```bash
python manage.py runserver
```

## 🛠️ Configurações

The project is configured with:
- SQLite as a database
- Media file support
- Custom Messaging with Tailwind CSS
- Standard language: Portuguese
- Debug enabled for development

## 📁 Project Structure

```
medical-manager/
├── core/                   # Settings main project
├── patients/              # Aplicação principal
├── media/                 # Uploaded media files
├── templates/             # Templates HTML
│   └── static/           # Static files
├── manage.py
└── requirements.txt
```

## 🔐 Environment Variables

Remember to configure the following variables in production:
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS

## 📊 Data Models

- `Patients`: Manages patient information
- `Todos`: Task system
- `Consult`: Query log

## 🤝 Contributing

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Licença

This project is under the MIT license. View the archive `LICENSE` for more details.

## 👥 Author

Cafu Dev - [Emicy963](https://github.com/Emicy963)
