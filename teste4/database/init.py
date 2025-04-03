from database import db
from model.OperaroraRegistroAtivo import OperadoraRegistroAtivo
from model.PlanoDados import PlanoDados

try:
    db.connect()
    db.create_tables([PlanoDados, OperadoraRegistroAtivo])
    print("Database connected and tables created successfully.")
except Exception as e:
    print(f"Error connecting to the database: {e}")