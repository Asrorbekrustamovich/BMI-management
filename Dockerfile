# 1. Python rasmidan foydalanamiz
FROM python:3.9.13  

# 2. Ishlash katalogini belgilash
WORKDIR /app

# 3. Talablar faylini nusxalash va o'rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Loyiha fayllarini nusxalash
COPY . .

# 5. Django migratsiyalarini bajarish va statik fayllarni to'plash
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# 6. Django ilovasini ishga tushirish (gunicorn)
ENV PORT=8000
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:$PORT"]