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
```

### Примеры использования 
```bash
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": "ААА"}'
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": ["ААА"]}'
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"text": ["А", "А", "А"]}'
```

## Метрики

Используются:

- Latency (P50/P90/P99) 
- Throughput

Ноутбук с замером метрик находится в этом же репозитории (metrics_test.ipynb)