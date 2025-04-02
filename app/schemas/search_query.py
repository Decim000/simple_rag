from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
    query: str
    metadata: dict | None = Field(default=None)
