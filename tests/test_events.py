import asyncio
import pytest
from httpx import AsyncClient
from app.main import app
from app.db import init_db

@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope="module", autouse=True)
async def setup_db():
    await init_db()

@pytest.mark.anyio
async def test_event_validation():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Missing event_type
        r = await ac.post("/events/", headers={"Authorization": "Bearer user1"}, json={"description": "Desc"})
        assert r.status_code == 422
        # Invalid event_type (contains space)
        r = await ac.post("/events/", headers={"Authorization": "Bearer user1"}, json={"event_type": "bad event", "description": "test"})
        assert r.status_code == 422
        # Invalid authorization
        r = await ac.post("/events/", json={"event_type": "login"})
        assert r.status_code == 422 or r.status_code == 401

@pytest.mark.anyio
async def test_event_log_and_retrieve():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {"event_type": "login", "description": "Logged in", "metadata": {"action": "sign_in"}}
        post_resp = await ac.post("/events/", headers={"Authorization": "Bearer user1"}, json=payload)
        assert post_resp.status_code == 200, post_resp.text
        data = post_resp.json()
        assert data["event_type"] == "login"
        get_resp = await ac.get("/events/", headers={"Authorization": "Bearer user1"})
        out = get_resp.json()
        assert get_resp.status_code == 200
        assert "items" in out
        assert out["total"] >= 1
