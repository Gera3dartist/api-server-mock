from pydantic import BaseModel, EmailStr


class UserUpdate(BaseModel):
    name: str
    email: EmailStr


class User(UserUpdate):
    id: str


class ProjectUpdate(BaseModel):
    name: str


class Project(ProjectUpdate):
    id: str

# TODO: define fields properly
class Field(BaseModel):
    name: str
    type: str
    default: str


class Endpoints(BaseModel):
    url: str
    method: str
    enanbled: bool


class ResourceBase(BaseModel):
    name: str
    schema: list[Field]
    endpoints: list[Endpoints]
    count: int


class Resource(ResourceBase):
    id: str