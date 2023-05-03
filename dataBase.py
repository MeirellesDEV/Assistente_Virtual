import sqlite3
import random
import string
import time

tamanho = 5
caracteres = string.ascii_letters + string.digits
nomeTabela = ''.join(random.choice(caracteres) for i in range(tamanho))
usuario = 'ximbinha'
email = 'teste'
senha = '987'

conn = sqlite3.connect('bacaxinho.db')

# Cria um objeto cursor
cursor = conn.cursor()

# Criando o usuario e inserindo no banco
cursor.execute("INSERT INTO usuario(nome,email,senha,identificador)VALUES(?,?,?,?)",(usuario,email,senha,nomeTabela))
conn.commit()

time.sleep(2)

cursor.execute("SELECT id FROM usuario u WHERE u.identificador = '"+nomeTabela+"'")
resultado = cursor.fetchall()
id_usuario = resultado[0][0]

time.sleep(2)

cursor.execute("INSERT INTO identificadores(identificador, id_usuario)VALUES(?,?)",(nomeTabela, id_usuario))
conn.commit()

time.sleep(2)

# Cria uma tabela "clientes"
cursor.execute('''CREATE TABLE '''+nomeTabela+'''(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	id_usuario INTEGER NOT NULL,
	id_sentimento INTEGER NOT NULL,
	dt_insercao DATE NOT NULL,
	
	FOREIGN KEY (id_usuario) REFERENCES usuario(id),
	FOREIGN KEY (id_sentimento) REFERENCES sentimento(id)
)''')

# # Salva as alterações e fecha a conexão
conn.commit()
conn.close()