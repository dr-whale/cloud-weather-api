from src.yandex import Client, ClientError, InvalidMethodError, BadConfigError, InvalidArgumentError
from src.lib import CacheManager
from config import yandex
import pika, datetime, json

def error_decorator(func):
    def test_wrapper():
        code = 500
        message = 'Error'
        try:
            return func()
        except InvalidArgumentError as exp:
            code = 404
            message = str(exp)
        except BadConfigError as exp:
            code = 403
            message = str(exp)
        except InvalidMethodError as exp:
            code = 412
            message = str(exp)
        except ClientError as exp:
            code = 400
            message = str(exp)
        except Exception as exp:
            code = 500
            message = str(exp)
        return json.dumps({"status": "error", "message": message, "code": code})
    test_wrapper.__name__ = func.__name__
    return test_wrapper

weather_client = None

def client_create():
    global weather_client
    if not weather_client:
        weather_client = Client(yandex.BASE_URL, yandex.API_KEY)
    return weather_client

# @error_decorator
def weather_send(date):
    weather = CacheManager().get(date)
    if not weather:
        full_day = client_create().weather_req(yandex.DATA_URL, yandex.PARAMS)['forecasts'][0]['parts']['day']
        CacheManager().remember(date, json.dumps(dict(temperature = full_day['temp_avg'], condition = full_day['condition'])))
        weather = CacheManager().get(date)
    channel.queue_declare(queue = 'weather', durable = True)
    channel.basic_publish(exchange = '', routing_key = 'weather', body = weather)
    print('Weather send')
    
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()
channel.queue_declare(queue = 'date', durable = True)

def callback(ch, method, properties, body):
    weather_send(json.loads(body)['date'])

channel.basic_consume(queue = 'date', on_message_callback = callback, auto_ack = True)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
