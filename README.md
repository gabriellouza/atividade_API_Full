# StudyManager API

API RESTful para gerenciamento de usuários, cursos e matrículas, construída com FastAPI e SQLAlchemy.

## Funcionalidades
- CRUD completo de usuários
- CRUD completo de cursos
- Criação de matrículas com validações
- Consulta relacional de cursos por usuário
- Tratamento padronizado de erros
- Normalização de campos de texto (remove espaços extras) e bloqueio de texto em branco

## Estrutura de pastas

```bash
app/
├── controllers/
│   └── routes/
├── usecases/
├── repositories/
├── entities/
└── infrastructure/
```

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse: `http://127.0.0.1:8000/docs`

## Endpoints

### Usuários
- `POST /users`
- `GET /users`
- `GET /users/{id}`
- `PUT /users/{id}`
- `DELETE /users/{id}`
- `GET /users/{id}/courses`

### Cursos
- `POST /courses`
- `GET /courses`
- `GET /courses/{id}`
- `PUT /courses/{id}`
- `DELETE /courses/{id}`

### Matrículas
- `POST /enrollments`

## Padrão de resposta

```json
{
  "success": false,
  "message": "User not found",
  "data": null
}
```
