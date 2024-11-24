FROM python:3.9.13-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /moepdf

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN apk add libreoffice-writer

EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
