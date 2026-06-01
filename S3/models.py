import os
from peewee import SqliteDatabase, Model, AutoField, CharField, TextField, BooleanField, ForeignKeyField, DateTimeField
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SqliteDatabase(os.path.join(BASE_DIR, "role_service.db"))

class BaseModel(Model):
    class Meta:
        database = db

class Role(BaseModel):
    id = AutoField()  # Явно объявлен первичный ключ
    name = CharField(max_length=50, unique=True, null=False)  # Валидация минимальной длины будет в сервисе
    description = TextField(max_length=200, null=True)
    is_active = BooleanField(default=True, null=False)

class RolePermission(BaseModel):
    id = AutoField()  # Явно объявлен первичный ключ
    role_id = ForeignKeyField(Role, backref="role_permissions", null=False, on_delete="CASCADE")  # Явное имя поля
    permission_id = CharField(max_length=100, null=False)  # ID разрешения из внешнего сервиса
    granted_at = DateTimeField(default=datetime.now, null=False)

def init_db():
    db.connect()
    db.create_tables([Role, RolePermission], safe=True)
    db.close()

def get_db():
    return db

if __name__ == "__main__":
    init_db()
    print("База данных инициализирована.")