from fastapi import APIRouter, Request, Response, Query
from fastapi.responses import JSONResponse
from database.database import db
from model.OperaroraRegistroAtivo import OperadoraRegistroAtivo
from playhouse.shortcuts import model_to_dict

operator_router = APIRouter()



@operator_router.get("/")
async def _get_operators(response: Response, name: str = Query(None, description="Nome da operadora para buscar")):
    """
    Get all operators, limited to 10 results.
    """
    query = OperadoraRegistroAtivo.select().limit(10)
    
    if name:
        query = query.where(OperadoraRegistroAtivo.nome_fantasia.contains(name)).limit(10)
    
    operators = list(query.dicts())
    
    for item in operators:
        if "data_registro_ans" in item and item["data_registro_ans"]:
            item["data_registro_ans"] = item["data_registro_ans"].strftime("%Y-%m-%d")
            
    
    if not operators:
        return JSONResponse(content={"message": "No operators found"}, status_code=404)

    return JSONResponse(content=operators, status_code=200)

@operator_router.get("/{operator_id}")
async def _get_operator_by_id(operator_id: int, response: Response):
    """
    Get operator by ID.
    """
    operator = OperadoraRegistroAtivo.get_or_none(OperadoraRegistroAtivo.id == operator_id)
    
    if not operator:
        return JSONResponse(content={"message": "Operator not found"}, status_code=404)
    
    if operator.data_registro_ans:
        operator.data_registro_ans = operator.data_registro_ans.strftime("%Y-%m-%d")
        
    formatted_operator = model_to_dict(operator)

    return JSONResponse(content=formatted_operator, status_code=200)