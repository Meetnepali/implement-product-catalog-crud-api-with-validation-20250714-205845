FROM python:3.11-slim
WORKDIR /workspace
COPY . .
RUN pip install --upgrade pip \
    && pip install fastapi==0.101.0 "uvicorn[standard]"==0.23.2 sqlalchemy[asyncio]==2.0.20 asyncpg==0.28.0 pydantic==1.10.12 httpx==0.24.1 pytest==7.4.0 pytest-asyncio==0.21.1
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
