from fastapi import APIRouter

router = APIRouter()

@router.get("/add")
async def add_route():
    return {"message": "Add route here"}
