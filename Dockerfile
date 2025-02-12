# 1. Python rasmidan foydalanamiz
FROM python:3.x

# 2. Ishlash katalogini belgilash
WORKDIR /app

# 3. Loyiha fayllarini konteynerga nusxalash
COPY . /app/

# 4. virtual muhitni yaratish
RUN python -m venv /opt/venv

# 5. virtual muhitni faollashtirish
RUN . /opt/venv/bin/activate

# 6. Talablar faylini o'rnatish (requirements.txt)
RUN pip install -r requirements.txt

# 7. `gunicorn`ni o'rnatish
RUN pip install gunicorn

# 8. Django migratsiyalarini bajarish va statik fayllarni to'plash
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# 9. Django ilovasini ishga tushirish (gunicorn)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:$PORT"]
