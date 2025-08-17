from fastapi import APIRouter
from backend.logic.calculator import evaluate_expression 
from backend.models.arithmetic_models import mathExpression,multiValueOperations, divisionOperation

router = APIRouter()

@router.get("/")
async def add_route():
    return {"message": "Hello Calculator App"}

@router.post("/calculate")
async def calculate(expression: mathExpression):
    return {"result": evaluate_expression(expression.expr)}

