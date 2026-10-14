# API de Controle de Alunos

API REST desenvolvida em Python utilizando **FastAPI** e **MongoDB** para realizar o gerenciamento de alunos por meio das operações CRUD (Create, Read, Update e Delete).

## 🚀 Tecnologias utilizadas

- **Python 3.13** — linguagem de programação.
- **FastAPI** — criação da API REST.
- **MongoDB** — banco de dados NoSQL.
- **PyMongo** — conexão e operações com o MongoDB.
- **Pydantic** — validação dos dados recebidos pela API.

## 📋 Funcionalidades

- Cadastrar novos alunos.
- Listar todos os alunos cadastrados.
- Atualizar dados de alunos.
- Excluir alunos cadastrados.
- Validar os dados enviados nas requisições HTTP.

## Endpoints

| Método HTTP | Endpoint | Descrição |
|---|---|---|
| `POST` | `/alunos/` | Cadastrar um aluno |
| `GET` | `/alunos/` | Listar todos os alunos |
| `PUT` | `/alunos/{id}` | Atualizar dados de um aluno |
| `DELETE` | `/alunos/{id}` | Excluir um aluno |

*Observação: os endpoints de consulta, atualização e exclusão devem corresponder às rotas efetivamente implementadas no código.*

## 📝 Exemplo de cadastro

Requisição `POST /alunos/`:

```json
{
  "nome": "Otavio",
  "idade": 20,
  "matricula": 3,
  "matriculaAtiva": true
}
```

## 🎯 Objetivo acadêmico

Projeto desenvolvido com o objetivo de praticar a construção de APIs REST, operações CRUD, validação de dados, integração com banco de dados NoSQL e utilização dos métodos HTTP.

## 👨‍💻 Autor

**Joaquim de Jesus**

Projeto acadêmico desenvolvido para fins de estudo e aprendizado em desenvolvimento backend.
