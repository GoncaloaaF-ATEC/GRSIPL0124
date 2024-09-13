import mysql.connector

#criar conn
conn = mysql.connector.connect( user= "root"
  password= "root",
  host= "127.0.0.1",
  database= "Alunos")

cursor = conn.cursor(dictionary=True)


#modificar DB
cursor.execute("INSERT INTO Aluno(nome, numero) VALUES ('Novo Nome2', 99)")
cursor.execute("INSERT INTO Aluno(nome, numero) VALUES ('Novo Nome3', 99)")


conn.commit()


# ler dados

cursor.execute('SELECT * FROM Aluno')

results = cursor.fetchall()

for row in results:
  id = row['id']
  nome = row['nome']
  numero = row['numero']
  print(f"id: {id}, numero: {numero}, nome: {nome}")



conn.close()
