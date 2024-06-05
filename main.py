from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/get")
async def get_request(request: Request):
    return {
        "args": request.query_params,
        "headers": request.headers,
        "origin": request.client.host,
        "url": str(request.url)
    }


@app.post("/post")
async def post_request(request: Request, item: Item):
    return {
        "args": request.query_params,
        "data": item,
        "headers": request.headers,
        "origin": request.client.host,
        "url": str(request.url)
    }


@app.put("/put")
async def put_request(request: Request, item: Item):
    return {
        "args": request.query_params,
        "data": item,
        "headers": request.headers,
        "origin": request.client.host,
        "url": str(request.url)
    }


@app.delete("/delete")
async def delete_request(request: Request):
    return {
        "args": request.query_params,
        "headers": request.headers,
        "origin": request.client.host,
        "url": str(request.url)
    }


@app.get("/status/{code}")
async def status_code(code: int):
    return Response(status_code=code)


@app.get("/redirect/{n}")
async def redirect_n_times(n: int):
    if n <= 0:
        return {"message": "Reached final destination"}
    return RedirectResponse(url=f"/redirect/{n-1}")


@app.get("/headers")
async def headers(request: Request):
    return {"headers": request.headers}


@app.get("/ip")
async def ip(request: Request):
    return {"origin": request.client.host}


@app.get("/user-agent")
async def user_agent(request: Request):
    return {"user-agent": request.headers.get("user-agent")}


@app.get("/delay/{n}")
async def delay_response(n: int):
    import asyncio
    await asyncio.sleep(n)
    return {"message": f"Response delayed by {n} seconds"}
