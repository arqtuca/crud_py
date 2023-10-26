
import mysql.connector

def conectar():

  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="011292",
    database="bd_escola"
  )

  return connection

def criar_aluno(nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala):

  connection = conectar()
  cursor = connection.cursor()

  # Insere o aluno no banco de dados
  sql = "INSERT INTO alunos (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala) VALUES (%s, %s, %s, %s, %s, %s)"
  val = (nome, idade, nota_primeiro_semestre, nota_segundo_semestre, nome_professor, numero_sala)
  cursor.execute(sql, val)

  connection.commit()

  return cursor.lastrowid

