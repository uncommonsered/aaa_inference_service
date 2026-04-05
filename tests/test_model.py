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
    assert isinstance(embedding, list)

    texts = ["AAA", "Трипл Эй", "Академия Аналитиков Авито"]
    for text in texts:
        embedding = asyncio.run(infer(model, text))
        assert embedding is not None
        assert len(embedding) > 0
        assert isinstance(embedding, list)

    text = ""
    embedding = asyncio.run(infer(model, text))
    assert embedding is not None
    assert len(embedding) > 0
    assert isinstance(embedding, list)


def test_init_model():
    model = init_model()
    assert isinstance(model, SentenceTransformer)
