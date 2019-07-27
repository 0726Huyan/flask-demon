from flask import current_app, render_template
from . import celery,mail
from flask_mail import Message
from kombu import serialization
serialization.registry._decoders.pop("application/x-python-serialize")
celery.conf.update(
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
    )
@celery.task()
def send_email():
    msg = Message('Hello from Flask',
                  recipients=['200898052@qq.com'])
    mail.send(msg)

def send_login_email(recipients,subject):
    msg = Message(subject=subject,recipients=[recipients])
    mail.send(msg)

