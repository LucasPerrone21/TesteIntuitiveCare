from fastapi import APIRouter, Request, Response, Query
from fastapi.responses import JSONResponse
from database.database import db, OperadoraRegistroAtivo
import datetime
import json

operator_router = APIRouter()



@operator_router.get("/")
async def _get_operators(response: Response, name: str = Query(None, description="Nome da operadora para buscar")):
    """
    Get all operators.
    """
    query = OperadoraRegistroAtivo.select()
    
    if name:
        query = query.where(OperadoraRegistroAtivo.nome_fantasia.contains(name))
    
    operators = list(query.dicts())
    
    for item in operators:
        if "data_registro_ans" in item and item["data_registro_ans"]:
            item["data_registro_ans"] = item["data_registro_ans"].strftime("%Y-%m-%d")
            
    print(f"Operators found: {operators}")
    

    if not operators:
        return JSONResponse(content={"message": "No operators found"}, status_code=404)

    return JSONResponse(content=operators, status_code=200)