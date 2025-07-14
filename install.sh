#!/bin/bash
set -e
apt-get update && apt-get install -y python3 python3-pip python3-venv
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install fastapi==0.101.0 "uvicorn[standard]"==0.23.2 sqlalchemy[asyncio]==2.0.20 asyncpg==0.28.0 pydantic==1.10.12 httpx==0.24.1 pytest==7.4.0 pytest-asyncio==0.21.1
