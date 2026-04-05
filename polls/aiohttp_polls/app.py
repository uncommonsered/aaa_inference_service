import asyncio
import logging

import aiohttp
from aiohttp import web

from polls.aiohttp_polls.models import infer, init_model
from polls.aiohttp_polls.routes import setup_routes

logging.basicConfig(filename="logs.log", level=logging.ERROR)

app = web.Application()
setup_routes(app)

async def on_startup(app):
    app["model"] = init_model()

async def handler(request):
    return web.Response(text="ans_text")


async def embed_handler(request):
    data = await request.json()
    model = app["model"]
    texts = data["text"]
    if isinstance(texts, str):
        texts = [texts]
    tasks = [infer(model=model, text=text) for text in texts]
    embeddings = await asyncio.gather(*tasks)
    embeddings_list = [embedding.tolist() for embedding in embeddings]

    return web.json_response({"embedding": embeddings_list})


async def health_handler(responce):
    return web.json_response({"status": "OK"})


app.add_routes([web.post("/embed", embed_handler), web.get("/health", health_handler)])

web.run_app(app, host ="0.0.0.0", port=8000)
