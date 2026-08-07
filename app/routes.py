from fastapi import APIRouter

from app.handlers import indexer_proxy

router = APIRouter()


router.add_api_route(
    "/indexer-proxy",
    indexer_proxy,
    methods=["POST"],
)
