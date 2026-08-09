from pydantic import BaseModel, Field

class GenerateQueryRequest(BaseModel):
    user_prompt: str = Field(example="Prompt given by user (SOC Analyst)")

class GenerateQueryResponse(BaseModel):
    message: str = Field(example="Message to be shown to user")
    query: dict = Field(example={
        "dsl query": "to be sent to Wazuh Indexer"
    })
