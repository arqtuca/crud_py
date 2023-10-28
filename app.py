from fastapi import FastAPI
import uvicorn
import mysql.connector
from pydantic import BaseModel


class Aluno(BaseModel):
  nome: str
  idade: int
  nota_primeiro_semestre: float
  nota_segundo_semestre: float
  nome_professor: str
  numero_sala: int


app = FastAPI()

@app.get('/conectar')
def conectar():

  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="011292",
    database="bd_escola"
  )
  return connection

@app.post('/criar_aluno')
def criar_aluno(aluno: Aluno):

  connection = conectar()
  cursor = connection.cursor()

  # Insere o aluno no banco de dados
  sql = "INSERT INTO alunos (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala) VALUES (%s, %s, %s, %s, %s, %s)"
  val = (aluno.nome, aluno.idade, aluno.nota_primeiro_semestre, aluno.nota_segundo_semestre, aluno.nome_professor, aluno.numero_sala)
  cursor.execute(sql, val)

  connection.commit()
  return cursor.lastrowid


if __name__ == '__main__':
  uvicorn.run(app, host='00.0.0.0', port=8000)
