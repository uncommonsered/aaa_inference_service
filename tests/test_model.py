from polls.aiohttp_polls.models import infer
from polls.aiohttp_polls.models import init_model
from sentence_transformers import SentenceTransformer
import asyncio

model = init_model()


def test_infer():
    text = "ААА"
    embedding = asyncio.run(infer(model, text))
    assert embedding is not None
    assert len(embedding) > 0

    texts = ["AAA", "Трипл Эй", "Академия Аналитиков Авито"]
    for text in texts:
        embedding = asyncio.run(infer(model, text))
        assert embedding is not None
        assert len(embedding) > 0

    text = ""
    embedding = asyncio.run(infer(model, text))
    assert embedding is not None
    assert len(embedding) > 0


def test_init_model():
    model = init_model()
    assert isinstance(model, SentenceTransformer)
