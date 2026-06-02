from fastapi import APIRouter
from services.schemas import GrammarInput, GrammarOutput
from services.grammarchecker import check_grammar

router = APIRouter()

@router.post("/check-grammar", response_model=GrammarOutput)
def grammar_checker(request: GrammarInput):
    result = check_grammar(request.text)
    return result