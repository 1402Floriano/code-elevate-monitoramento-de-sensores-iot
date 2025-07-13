from kafka import KafkaConsumer
import json
import sqlite3
from datetime import datetime

# Configuração do Consumer Kafka
consumer = KafkaConsumer(
    'dados_sensores',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Configuração do banco de dados SQLite
conn = sqlite3.connect('bd_sensores.db')
cursor = conn.cursor()

# Criação da tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_monitoramento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_sensor INTEGER,
        temperatura REAL,
        umidade REAL,
        dt_hr TEXT
    )
''')
conn.commit()

print(" 🔄 Consumindo dados do tópico dados_sensores...")

try:
    for mensagem in consumer:
        data = mensagem.value
        cursor.execute('''
            INSERT INTO tb_monitoramento (id_sensor, temperatura, umidade, dt_hr)
            VALUES (?, ?, ?, ?)
        ''', (data['id_sensor'], data['temperatura'], data['umidade'], data['dt_hr']))
        conn.commit()
        print(f" 💾 Dados salvos no banco: {data}")
except KeyboardInterrupt:
    print(" ⚠️  Consumer interrompido.")
finally:
    conn.close()
    consumer.close()