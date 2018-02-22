from setuptools import setup

setup(
    name='paradigm',
    packages=['paradigm'],
    include_package_data=True,
    install_requires=[
        'flask','flask_sqlalchemy','Flask-InfluxDB','flask-socketio','eventlet','celery','sqlalchemy','protobuf','redis'
    ],
)
