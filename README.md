# Inference Service (rubert-mini-frida)

## Описание

Сервис для получения эмбеддингов текста через HTTP API. Использован **aiohttp**, так этот фреймворк
асинхронный и был опыт его использования.


## Запуск и использование

```bash
docker build -t app:1 .
docker run -p 8000:8000 app:1
```

### Проверка сервиса

```bash
curl http://localhost:8000/health
PYTHONPATH=. pytest tests/
```
(должен быть установлен pytest)

### Примеры использования 
```bash
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": "ААА"}'
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": ["ААА"]}'
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": ["А", "А", "А"]}'
```

Возвращает json вида ```python {'embeddings' : [...]}```
Где внутри списка находятся эмбеддинги в порядке их следования в json-запросе, который должен иметь вид: ```python {'text' : [...]}```
Ключом может быть или список текстов, или один текст строкой

## Метрики

Используются:

- Latency (P50/P90/P99) 
- Throughput

Ноутбук с замером метрик находится в этом же репозитории (metrics_test.ipynb)