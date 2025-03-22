FROM python:3.9-slim AS builder
WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY server.py github_api.py .gitignore README.md ./
COPY templates/ ./templates/
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
EXPOSE 80
CMD [ "python", "server.py"]

