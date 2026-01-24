from fastapi import APIRouter, Request
import logging

from api.api.models import RAGRequest, RAGResponse

from api.rag.retrieval_generation import rag_pipeline

logger = logging.getLogger(__name__)

rag_router = APIRouter()


@rag_router.post("/")
def rag(
    request: Request,
    payload: RAGRequest
) -> RAGResponse:

    result = rag_pipeline(payload.query)

    return RAGResponse(
        request_id=request.state.request_id,
        answer=result["answer"]
    )


api_router = APIRouter()
api_router.include_router(rag_router, prefix="/rag", tags=["rag"])
