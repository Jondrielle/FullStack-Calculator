from pydantic import BaseModel, field_validator, ValidationError

class multiValueOperations(BaseModel):
    x: float
    y: float

class divisionOperation(BaseModel):
    x: float
    y: float

    @field_validator('y')
    def y_must_not_be_zero(cls, value):
        if value == 0:
            raise ValueError('Division by zero is not allowed')
        return value

class mathExpression(BaseModel):
    expr: str
