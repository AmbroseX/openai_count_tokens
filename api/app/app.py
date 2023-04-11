# --coding:utf-8--
import tiktoken
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InputString(BaseModel):
    string: str = "This is a string."
    model: str = "gpt-3.5-turbo"


class InputMessages(BaseModel):
    messages: list = [{"role": "system", "content": "Serve me as a writing and programming assistant"},
                      {"role": "user", "content": "hello"}]
    model: str = "gpt-3.5-turbo"


@app.post("/str_tokens")
async def count_str_tokens(input_string: InputString):
    string = input_string.string
    model = input_string.model
    assert isinstance(string, str)
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return {"num_tokens": num_tokens}


@app.post("/messages_tokens")
async def count_messages_tokens(input_message: InputMessages):
    messages = input_message.messages
    model = input_message.model
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = 0
    for message in messages:
        num_tokens += 4
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
    num_tokens += 2
    return {"num_tokens": num_tokens}
