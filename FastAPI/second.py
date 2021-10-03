from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/ = result = {"detail":"Not Found"}
# http://127.0.0.1:8000/items/5?q=somequery = result = {"item_id":5,"q":"somequery"}
# http://127.0.0.1:8000/items/5 = result = {"item_id":5,"q":null}
# karena q bersifat optional

# http://127.0.0.1:8000/q=hello = result = {"detail":"Not Found"}
# karena value dari item_id tidak ada

# Documentation API : http://127.0.0.1:8000/docs
