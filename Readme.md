# Tinyurl

Link shortener service.

## Build and run

```
docker compose up -d --build
```

## API

### 1. Get token

+ Path: `/api/v1/short_urls`
+ Method: `POST`
+ Request body:
```json
        {
            "long_url": "..."
        }
```
+ Response:
```json
        {
            "token": "..."
        }
```

### 2. Get URL

+ Path: `/api/v1/short_urls/:token`
+ Method: `GET`
+ Response:
```json
        {
            "url": "..."
        }
```



