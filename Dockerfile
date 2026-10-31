FROM python:3.14.10-slim-trixie

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY gunicorn.conf.py .

EXPOSE 8000

CMD ["gunicorn", "src.main:app"]
