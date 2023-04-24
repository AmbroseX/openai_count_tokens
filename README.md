# openai_count_tokens


# docker use

```shell
docker build -t openai_count_tokens:v1.0 .
```

RUN docker-compose
```shell
docker-compose up -d
```

# Post使用
```shell
curl --location 'http://localhost:8001/str_tokens' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "string": "this is a message你好# -- coding:utf-8 --import tiktokenfrom fastapi import FastAPIfrom pydantic import BaseModel",
    "model": "gpt-3.5-turbo"
```

返回值：
```json
{
    "num_tokens": 28
}
```