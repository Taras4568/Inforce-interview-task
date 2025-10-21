FROM python:3.12-slim-bookworm AS builder
WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends build-essential gcc libpq-dev ca-certificates && rm -rf /var/lib/apt/lists/*
COPY api/requirements.txt /app/
RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY api/ /app/
ENV PYTHONUNBUFFERED=1
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
