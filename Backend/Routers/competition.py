from fastapi import APIRouter

router = APIRouter(
    prefix="/competition",
    tags=['Create and manage competitions.']
)

@router.get("/")
async def get_competition():
    return {"message": "Get all competitions."}