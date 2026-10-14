from fastapi import FastAPI, HTTPException
from pymongo import AsyncMongoClient, ReturnDocument
from serializador import convertDoc, convertDoclist
from pydantic import BaseModel
from mongoDbURL import mongoUrl


client = AsyncMongoClient(mongoUrl)
app = FastAPI()
database = client.get_database("basededados")
collection = database.get_collection("alunos")

class Aluno(BaseModel):
    nome: str
    idade: int
    matricula: int
    matriculaAtiva: bool

@app.post("/alunos/")
async def adicionaAluno(aluno: Aluno):
    await collection.insert_one(aluno.model_dump())
    return {"message": "aluno adicionado", "aluno": aluno}

@app.get("/alunos/")
async def listaAlunos():
    alunos = await collection.find().to_list()
    return {"alunos": convertDoclist(alunos)}

@app.get("/alunos/{nome}")
async def consultarAluno(nome: str):
    aluno = await collection.find_one({"nome": nome})
    if aluno:
        return{"aluno": convertDoc(aluno)}
    raise HTTPException(status_code=404, detail=f"Item width name {nome} not foud")



@app.put("/alunos/{nome}")
async def atualizarAluno(nome: str, aluno: Aluno):
    atualizarAluno = await collection.find_one_and_update(
        {"nome": nome},
        {"$set": aluno.model_dump()},
        return_document=ReturnDocument.AFTER,
    )

    if atualizarAluno:
        return {"message": "Aluno Atualizado", "aluno": convertDoc(atualizarAluno)}
    raise HTTPException(status_code=404, detail=f"Item with name {nome} not found")

@app.delete("/alunos/{nome}")
async def excluiAluno(nome: str):
    deletaAluno = await collection.delete_one({"nome": nome})

    if deletaAluno:
        return {"message": "Aluno Excluido", "aluno": nome}
    raise HTTPException(status_code=404, detail=f"Item with name {nome} not found")