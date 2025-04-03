from peewee import *
import os



db = PostgresqlDatabase(
    os.getenv('POSTGRES_DB'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT'),
)

class BaseModel(Model):
    class Meta:
        database = db





