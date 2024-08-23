# Tinyurl

Link shortener service.

## Build and run

```
docker compose up -d --build
```

## Request examples

```bash
$ curl POST -H "Content-Type: application/json" \
   --data '{"long_url": "https://www.someurl.://www.someurl.com/"}' \
   localhost:8000/api/v1/short_urls -v

*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> POST /api/v1/short_urls HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 40
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 201 Created
< date: Fri, 23 Aug 2024 23:14:56 GMT
< server: uvicorn
< content-length: 15
< content-type: application/json
<
* Connection #0 to host localhost left intact
{"token":"quv"}

$ curl localhost:8000/api/v1/short_urls/quv -v

*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /api/v1/short_urls/quv HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.81.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Fri, 23 Aug 2024 23:16:14 GMT
< server: uvicorn
< content-length: 34
< content-type: application/json
<
* Connection #0 to host localhost left intact
{"url":"https://www.someurl.com/"}
```



