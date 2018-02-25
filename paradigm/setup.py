from setuptools import setup

setup(
    name='paradigm',
    packages=['paradigm'],
    include_package_data=True,
    install_requires=[
        'flask','pandas','Sphinx','Nose','flask_sqlalchemy','influxdb','flask-socketio','eventlet','celery','sqlalchemy','protobuf','redis'
    ],
)
