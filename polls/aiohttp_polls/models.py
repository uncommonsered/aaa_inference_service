import asyncio

from sentence_transformers import SentenceTransformer


def init_model(model_name: str = "sergeyzh/rubert-mini-frida"):
    model = SentenceTransformer(model_name)
    return model


async def infer(model, text: str):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, model.encode, text)
