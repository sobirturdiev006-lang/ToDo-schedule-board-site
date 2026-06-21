# 📋 Vazifalar — Todo App

Django asosida qurilgan shaxsiy vazifalar boshqaruv tizimi.

## 🚀 Funksiyalar

- Foydalanuvchi ro'yxatdan o'tish va kirish (django-allauth)
- Vazifa qo'shish, tahrirlash, o'chirish
- Vazifani bajarildi/bajarilmadi deb belgilash
- Kategoriyalar bo'yicha guruhlash
- Muhimlik darajasi (past, o'rta, yuqori)
- Holat va kategoriya bo'yicha filtrlash
- Har bir foydalanuvchi faqat o'z vazifalarini ko'radi
- Profil sahifasi va parol o'zgartirish

## 🛠️ Texnologiyalar

- Python 3.11
- Django 5.x
- django-allauth
- SQLite
- HTML/CSS (dark theme)

## ⚙️ O'rnatish
```bash
# Reponi klonlash
git clone https://github.com/username/todo.git
cd todo

# Virtual muhit
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Kutubxonalar
pip install -r requirements.txt

# Migratsiya
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Serverni ishga tushirish
python manage.py runserver
```

## 📁 Loyiha strukturasi
```
todo/
├── config/          → Sozlamalar (settings, urls)
├── todos/           → Asosiy ilova (models, views, forms)
├── templates/
│   └── account/     → Allauth shablonlar
    └── todos/   → HTML shablonlar
├── manage.py
└── requirements.txt
```

## 🔑 Muhim sozlamalar

`.env` faylida saqlang (hozircha `settings.py` da):
```python
SECRET_KEY = 'your-secret-key'
DEBUG = True
```

## 📸 Ko'rinishi

Dark theme asosida qurilgan minimal dizayn.

## 📄 Litsenziya

MIT