from fastapi import APIRouter
from backend.logic.calculator import add, sub, multiply, division, exponent 
from backend.models.arithmetic_models import multiValueOperations, divisionOperation

router = APIRouter()

@router.get("/")
async def add_route():
    return {"message": "Hello Calculator App"}

@router.post("/add")
def addition(request: multiValueOperations):
    return add(request.x, request.y)

@router.post("/sub")
def subtraction(request: multiValueOperations):
    return sub(request.x, request.y)   

@router.post("/multiply")
def multiplication(request: multiValueOperations):
    return multiply(request.x, request.y) 

@router.post("/divide")
def division_route(request: divisionOperation):
    return division(request.x, request.y) 

@router.post("/exponent")
def exponential(request: multiValueOperations):
    return exponent(request.x, request.y)