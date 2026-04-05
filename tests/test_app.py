from polls.aiohttp_polls.app import app
from polls.aiohttp_polls.routes import setup_routes
from polls.aiohttp_polls.models import init_model, infer
import pytest


@pytest.fixture
async def client(aiohttp_client):
    return await aiohttp_client(app)


@pytest.mark.asyncio
async def test_embed(client):
    data = {"text": ["ААА"]}
    resp = await client.post("/embed", json=data)
    json_response = await resp.json()
    assert "embedding" in json_response
    assert isinstance(json_response["embedding"], list)
    assert len(json_response["embedding"]) > 0
