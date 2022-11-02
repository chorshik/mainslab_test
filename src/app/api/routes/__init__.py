from fastapi import APIRouter
from app.api.routes.bills import router as bills_router

router = APIRouter()

router.include_router(bills_router, prefix="/bills", tags=["bills"])
