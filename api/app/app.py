# --coding:utf-8--
import tiktoken
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputString(BaseModel):
    string: str
    model: str = "gpt-3.5-turbo"

@app.post("/num_tokens")
async def count_num_tokens(input_string: InputString):
    string = input_string.string
    model = input_string.model
    assert isinstance(string, str)
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return {"num_tokens": num_tokens}
