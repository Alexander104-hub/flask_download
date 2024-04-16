from flask import Flask, request
from celery import Celery

app = Flask(__name__)
simple_worker = Celery('simple_worker',
                    broker='amqp://admin:mypass@rabbit:5672',
                    backend='rpc://')

@app.route('/download')
def download():
    url = request.args.get('url')
    r = simple_worker.send_task('tasks.download_file', kwargs={'url': url})
    return r.id
