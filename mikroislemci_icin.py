import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue_name = 'hello'


channel.queue_declare(queue=queue_name)


def send_message(message):
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    print(f" [x] Sunucu: Mesaj gönderildi: {message}")

send_message("SA kanka!")
#kuyruğa kodu yolladık
