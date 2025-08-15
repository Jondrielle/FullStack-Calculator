from fastapi import APIRouter
from backend.logic.calculator import add, sub, multiply, division, exponent 
from backend.models.arithmetic_models import multiValueOperations, divisionOperation

router = APIRouter()

@router.get("/")
async def add_route():
    return {"message": "Hello Calculator App"}

@router.post("/add")
def addition(request: multiValueOperations):
    return {"result": add(request.x, request.y)}

@router.post("/sub")
def subtraction(request: multiValueOperations):
    return {"result": sub(request.x, request.y)}   

@router.post("/multiply")
def multiplication(request: multiValueOperations):
    return {"result": multiply(request.x, request.y)} 

@router.post("/divide")
def division_route(request: divisionOperation):
    return {"result": division(request.x, request.y)} 

@router.post("/exponent")
def exponential(request: multiValueOperations):
    return {"result": exponent(request.x, request.y)}