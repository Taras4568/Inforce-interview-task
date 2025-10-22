FROM python:3.11-slim AS builder
WORKDIR /install

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app

RUN useradd -m appuser
USER appuser

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
