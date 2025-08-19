from fastapi import APIRouter
from backend.logic.calculator import evaluate_expression 
from backend.models.arithmetic_models import mathExpression,multiValueOperations, divisionOperation

router = APIRouter()

@router.post("/calculate")
async def calculate(expression: mathExpression):
    return {"result": evaluate_expression(expression.expr)}

