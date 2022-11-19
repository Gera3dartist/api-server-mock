from datetime import datetime
from sqlalchemy import DateTime, Table, Column, Integer, String, ForeignKeyConstraint, UniqueConstraint

from sqlalchemy.dialects.postgresql import JSONB

from .base import meta


users = Table(
    'users', meta,
    Column('email', String), 
    Column('id', Integer, primary_key = True),
    Column('name', String), 
    Column('public_id', String),
    Column('created_at', DateTime),
    Column('updated_at', DateTime, onupdate=datetime.utcnow)

)

project = Table(
    'project', meta, 
    Column('id', Integer, primary_key = True),
    Column('name', String), 
    Column('public_id', String),
    Column('created_at', DateTime),
    Column('updated_at', DateTime, onupdate=datetime.utcnow)
)

resource = Table(
    "resource", meta,
    Column('schema', JSONB),
    Column('endpoints', JSONB),     
    Column('count', Integer, default=0),
    Column('id', Integer, primary_key = True),
    Column('name', String), 
    Column('public_id', String),
    Column('created_at', DateTime),
    Column('updated_at', DateTime, onupdate=datetime.utcnow)
    )

resource_data = Table(
    "resource_data", meta,
    Column('data', JSONB),
    Column('resource_id', Integer),
    Column('project_id', Integer),
    Column('id', Integer, primary_key = True),
    ForeignKeyConstraint(
        ["project_id"], ["project.id"]
    ),
     ForeignKeyConstraint(
        ["resource_id"], ["resource.id"]
    ),
    UniqueConstraint("resource_id", "project_id", name="project_resource_data"),
    Column('created_at', DateTime),
    Column('updated_at', DateTime, onupdate=datetime.utcnow)
)
