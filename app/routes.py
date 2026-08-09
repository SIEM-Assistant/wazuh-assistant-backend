from fastapi import APIRouter

from app.handlers import indexer_proxy
from app.handlers import generate_query

router = APIRouter()


router.add_api_route(
    "/indexer-proxy",
    indexer_proxy,
    methods=["POST"],
)

router.add_api_route(
    "/generate-query",
    generate_query,
    methods=["POST"]
)
