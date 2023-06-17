import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse, HTMLResponse
from random_emoji import random_emoji

app = FastAPI()


@app.get("/")
async def root_get():
    return HTMLResponse('Hi! This is a root page. '
                        f'You can check <a href=\"/redirect\">redirect</a> page {random_emoji()}')


@app.get("/redirect")
async def redirect():
    return RedirectResponse('/')


@app.get("/{code:int}")
async def status_codes(code: int):
    if code < 600:
        return HTMLResponse(f'Status code is {code} {random_emoji()}',status_code=code)
    return HTMLResponse(f"Nothing here. You reached /{code} {random_emoji()}", status_code=404)


@app.get("/file")
async def get_sample_file():
    return FileResponse('example.txt')


@app.get("/json")
async def get_sample_file():
    return JSONResponse({'text': f"Hello! This is a json response! {random_emoji()}"})


@app.get("/{path:path}")
async def default_response(path: str):
    return HTMLResponse(f"Nothing here. You reached /{path} {random_emoji()}", status_code=404)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
