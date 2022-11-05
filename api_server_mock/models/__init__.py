import typing as t
from pydantic import BaseModel, EmailStr, SecretStr, Field



class UserUpdate(BaseModel):
    name: t.Optional[str]
    email: t.Optional[EmailStr]
    password: t.Optional[SecretStr]

class UserCreate(BaseModel):
    email: EmailStr
    password: SecretStr


class LoginUser(BaseModel):
    password: SecretStr
    email: EmailStr

class User(UserUpdate):
    id: str


class ProjectUpdate(BaseModel):
    name: str


class Project(ProjectUpdate):
    id: str

# TODO: define SchemaFields properly
class SchemaField(BaseModel):
    name: str
    type: str
    default: str


class Endpoints(BaseModel):
    url: str
    method: str
    enanbled: bool


class ResourceBase(BaseModel):
    name: str
    schema_: list[SchemaField] = Field(alias='schema')
    endpoints: list[Endpoints]
    count: int


class Resource(ResourceBase):
    id: str