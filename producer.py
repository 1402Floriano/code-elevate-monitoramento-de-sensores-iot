from kafka import KafkaProducer
from faker import Faker
import json
import time

# Configuração do Faker para gerar dados falsos
fake = Faker()

# Configuração do Producer Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Função para gerar dados de sensores
def gerador_dados_sensores(id_sensor):
    return {
        'id_sensor': id_sensor,
        'temperatura': round(fake.random_number(digits=2) + fake.random.uniform(0, 1), 2),
        'umidade': round(fake.random_number(digits=2) + fake.random.uniform(0, 1), 2),
        'dt_hr': fake.iso8601()
    }

# Enviar dados continuamente para o tópico Kafka
topico = 'dados_sensores'
print(f" 📋 Enviando dados para o tópico {topico}...")

try:
    while True:
        for id_sensor in [1, 2]:  # Simulando 2 sensores
            data = gerador_dados_sensores(id_sensor)
            producer.send(topico, data)
            print(f" 🔄 Dados enviados do sensor {id_sensor}: {data}")
        producer.flush()
        time.sleep(3)  # Envia dados a cada 3 segundos
except KeyboardInterrupt:
    print(" ⚠️  Producer interrompido.")
finally:
    producer.close()