from peewee import AutoField, DateField, CharField, DecimalField, IntegerField
from database.database import BaseModel



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