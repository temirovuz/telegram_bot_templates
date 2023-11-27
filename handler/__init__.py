from aiogram import Router
from .start import router as start
from .orders import router as orders

router = Router()
router.include_router(start)
router.include_router(orders)
