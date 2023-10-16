from fastapi import Body, FastAPI, Request, Response

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Olá pessoal!"}


@app.post("/")
async def criar_registro(request: Request, response: Response):
    body = await request.body()
    print(body)
    response.body = body
    response.status_code = 200
    return response
