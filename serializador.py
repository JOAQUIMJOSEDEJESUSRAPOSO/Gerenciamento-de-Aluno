def convertDoc (documento) -> dict:
    return {
        "id": str(documento["_id"]),
        "nome": documento["nome"],
        "idade": documento["idade"],
        "matricula": documento["matricula"],
        "matriculaAtiva": documento["matriculaAtiva"],
    }

def convertDoclist (documentos) -> list:
    return [convertDoc(doc) for doc in documentos]