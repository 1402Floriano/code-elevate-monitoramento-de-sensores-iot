import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('bd_sensores.db')
cursor = conn.cursor()

# Consultar os primeiros 10 registros
cursor.execute('SELECT * FROM tb_monitoramento LIMIT 10')
rows = cursor.fetchall()

# Exibir os dados
print("Dados salvos no banco de dados (primeiros 10 registros):")
for row in rows:
    print(row)

# Fechar a conexão
conn.close()