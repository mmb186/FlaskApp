from setuptools import setup

setup(
    name='paradigm',
    packages=['paradigm'],
    include_package_data=True,
    install_requires=[
        'flask','Flask-SQLAlchemy','flask-socketio','eventlet','celery'
    ],
)