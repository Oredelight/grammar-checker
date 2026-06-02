from pydantic import BaseModel


class GrammarInput(BaseModel):
    text: str

class Issue(BaseModel):
    message: str

class GrammarOutput(BaseModel):
    original: str
    corrected: str
    issues: list[Issue]
