import sqlalchemy
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):

    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id= {self.id}, name={self.name}, fullname={self.fullname}):"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50))
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_address})"

# Conexão com o banco de dados

engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())


with Session(engine) as session:
    victor = User(
        name='victor',
        fullname='victor Mascarenhas',
        address=[Address(email_address='julianam@email.com')]
    )

    sandy = User(
        name='sandy',
        fullname='Sandy Cardoso',
        address=[Address(email_address='sandy@email.br'),
                 Address(email_address='sandyc@email.org')]
    )

    patrick = User(name='patrick', fullname='Patrick Cardoso')

    # enviando para o BD (persitência de dados)
    session.add_all([victor, sandy, patrick])

    session.commit()
# Recuperando usuários a partir de condição de filtragem
stmt = select(User).where(User.name.in_(['victor', 'sandy']))
for user in session.scalars(stmt):
    print(user)


# Recuperando os endereços de Sandy
stmt_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
    print(address)


# Recuperando info de maneira ordenada
print("------------------")
order_stmt = select(User).order_by(User.fullname.desc())
for result in session.scalars(order_stmt):
    print( result)


print("------------------")
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)


# Executando statement a partir da connection
print('--------------')
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

print('--------------')
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)
