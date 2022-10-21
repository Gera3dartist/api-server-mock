from sqlalchemy import Table, Column, Integer, String, MetaData

from sqlalchemy.dialects.postgresql import JSONB
meta = MetaData()

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata_obj = MetaData(naming_convention=convention)

id_name_public_id_fields = [Column('id', Integer, primary_key = True), Column('name', String), Column('public_id', String)]


user = Table(
   'user', meta,
   Column('email', String), 
   *id_name_public_id_fields
   
)

project = Table(
   'project', meta, 
   *id_name_public_id_fields
)

resource = Table(
    "resource", meta,
    Column('schema', JSONB),
    Column('endpoints', JSONB),     
    Column('count', Integer, default=0)
    *id_name_public_id_fields

)
