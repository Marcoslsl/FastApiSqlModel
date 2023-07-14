from fastapi import APIRouter
from .gems import (
    gem_get_router,
    gem_create_router,
    gem_delete_router,
    gem_update_router,
)

router = APIRouter()
router.include_router(gem_get_router)
router.include_router(gem_create_router)
router.include_router(gem_delete_router)
router.include_router(gem_update_router)
