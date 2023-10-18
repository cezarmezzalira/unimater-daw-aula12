import json
from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.get("/{nome}")
async def responda_nome(request: Request):
    # Recupero os parâmetros enviados pelo path (barra de endereços)
    params = request.path_params
    # Recupero apenas o parâmetro nome
    nome = params.get("nome")
    # Crio o conteúdo de resposta (dict) e converto para string
    response_content = json.dumps({"message": f"Olá {nome}"})
    # Crio uma instancia da classe response, passando como parâmetros o conteúdo
    # e o tipo de conteúdo (json)
    response = Response(content=response_content,
                        media_type="application/json",
                        status_code=200)
    # Devolvo a resposta
    return response


@app.post("/outro")
async def responda_outro(request: Request):
    # Recupero os dados do body
    body = await request.body()
    # Converto o o body de bytes para dict {chave: valor}
    body = json.loads(body)
    # Recupero a propriedade nome
    nome = body.get("nome")
    # Recupero a propriedade valor
    valor = body.get("valor")
    # Retorno diretamente um dict, que é entendido como um retorno JSON
    return {"message": f"Nome: {nome} - Valor: {valor}"}
