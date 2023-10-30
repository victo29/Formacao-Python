from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
engine = create_engine('sqlite:///:memory') # Persiste dados

metadata_obj = MetaData(schema='teste')

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)
