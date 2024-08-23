# Tinyurl

Link shortener service.

## Build and run

```
docker compose up -d --build
```

## Request examples

```bash
$ curl -H "Content-Type: application/json" --data '{"long_url": "https://www.someurl.://www.someurl.com/"}' localhost:8000/api/v1/short_urls

{"token":"quv"}

$ curl localhost:8000/api/v1/short_urls/quv

{"url":"https://www.someurl.com/"}
```



