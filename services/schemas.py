from pydantic import BaseModel, field_validator


class GrammarInput(BaseModel):
    text: str
    @field_validator("text")
    def not_empty(cls, value):
        if not value.strip():
            raise ValueError("Text cannot be empty")
        return value

class Issue(BaseModel):
    message: str
    context: str
    offset: int
    length: int

class GrammarOutput(BaseModel):
    original: str
    corrected: str
    issues: list[Issue]
