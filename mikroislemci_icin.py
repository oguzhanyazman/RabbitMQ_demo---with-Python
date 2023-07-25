import pika

# RabbitMQ sunucusuna bağlanmak için connection oluşturun
connection = pika.BlockingConnection(pika.ConnectionParameters('RABBITMQ_HOST'))
channel = connection.channel()


queue_name = 'ogox'


channel.queue_declare(queue=queue_name)

# Mesaj alma
def receive_message(ch, method, properties, body):
    print(f"Mikro Mesaj alındı: {body}")

channel.basic_consume(queue=queue_name, on_message_callback=receive_message, auto_ack=True)

print('Mikro Mesajları bekliyor.')
channel.start_consuming()
