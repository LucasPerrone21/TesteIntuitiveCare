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


class PlanoDados(BaseModel):
    id = AutoField()
    data = DateField(null=False)
    reg_ans = CharField(max_length=8, null=False)
    cd_conta_contabil = CharField(max_length=9, null=False)
    descricao = CharField(max_length=150, null=False)
    vl_saldo_inicial = DecimalField(max_digits=20, decimal_places=2, null=False)
    vl_saldo_final = DecimalField(max_digits=20, decimal_places=2, null=False)
    
    class Meta:
        table_name = 'tbl_plano_dados'


class OperadoraRegistroAtivo(BaseModel):
    id = AutoField()
    reg_operadora = CharField(max_length=6, null=True)
    cnpj = CharField(max_length=14, null=True)
    razao_social = CharField(max_length=140, null=True)
    nome_fantasia = CharField(max_length=140, null=True)
    modalidade = CharField(max_length=140, null=True)
    logradouro = CharField(max_length=40, null=True)
    numero = CharField(max_length=20, null=True)
    complemento = CharField(max_length=40, null=True)
    bairro = CharField(max_length=30, null=True)
    cidade = CharField(max_length=30, null=True)
    uf = CharField(max_length=2, null=True)
    cep = CharField(max_length=8, null=True)
    ddd = CharField(max_length=4, null=True)
    telefone = CharField(max_length=20, null=True)
    fax = CharField(max_length=20, null=True)
    endereco_eletronico = CharField(max_length=255, null=True)
    representante = CharField(max_length=50, null=True)
    cargo_representante = CharField(max_length=40, null=True)
    regiao_de_comercializacao = IntegerField(null=True)
    data_registro_ans = DateField(null=True)
    
    class Meta:
        table_name = 'tbl_operadoras_registro_ativo'

try:
    db.connect()
    db.create_tables([PlanoDados, OperadoraRegistroAtivo])
    print("Database connected and tables created successfully.")
except OperationalError as e:
    print(f"Error connecting to the database: {e}")

