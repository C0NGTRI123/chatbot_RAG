from fastapi import APIRouter, Body, Query
from fastapi_base.response import ResponseObject

from app.src.schemas.general_config import LangCode, ModelCode
from app.src.services.kie_service import KieService

kie_routers = APIRouter()
kie_service = KieService()


@kie_routers.post("/kie-ollama/")
async def response(
    *,
    text: str = Body(embed=True, description="Content of OCR results"),
    model_name: ModelCode = Query(..., description="Name of model"),
    lang: LangCode = Query(..., description="code of Language"),
):
    data = kie_service.extract(text, model_name, lang)
    return ResponseObject(data=data)
