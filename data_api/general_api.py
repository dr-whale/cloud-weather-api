from flask import Flask, request
from error import ValidationError
import json, pika, datetime


app = Flask(__name__)

@app.route('/date')
def date_send():
    request_date = request.args.get('date')
    try:
        datetime.datetime.strptime(request_date, '%d.%m.%Y')
    except: 
        raise ValidationError('Value not Date')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue = 'date', durable = True)
    channel.basic_publish(exchange = '', routing_key = 'date', body = json.dumps(dict(date = request_date)))
    connection.close()
    return 'Date send'
