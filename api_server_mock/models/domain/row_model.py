from pydantic import BaseConfig, BaseModel


class RowModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        # serialiezer from db -> model goes here
