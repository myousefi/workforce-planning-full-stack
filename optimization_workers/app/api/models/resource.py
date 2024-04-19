from pydantic import BaseModel


class Resource(BaseModel):
    resource_ID: str
    profile: str
    private: bool
    disable: bool
