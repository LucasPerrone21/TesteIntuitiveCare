from peewee import AutoField, DateField, CharField, DecimalField
from database.database import BaseModel


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



