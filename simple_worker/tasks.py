from celery import Celery
from celery.utils.log import get_task_logger
import shutil
import os


logger = get_task_logger(__name__)

app = Celery('tasks',
             broker='amqp://admin:mypass@rabbit:5672',
             backend='rpc://')



@app.task
def download_file(url):
    destination_path = '/simple_worker/downloads'
    try:
        os.makedirs(destination_path, exist_ok=True)
        
        shutil.copy(url, destination_path)
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")