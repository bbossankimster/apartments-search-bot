from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime, Boolean

engine = create_engine('sqlite:///webapp.db', echo=False)


Base = declarative_base()
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    group_id = Column(Float(), unique=True, nullable=True)
    date = Column(String, nullable=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    vk_unique_id = Column(String, nullable=True)
    # Values after parsing
    price = Column(Float(), unique=True, nullable=True)
    rooms = Column(Float(), unique=True, nullable=True)
    neighbours = Column(Integer(), unique=True, nullable=True)
    is_parcing_successfull = Column(Boolean(), nullable=True)
    is_rent_room = Column(Boolean(), nullable=True)

    def __repr__(self):
        return '<Post id: {} {}>'.format(self.id, self.description)

# Создание таблицы
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

for instance in session.query(Post).order_by(Post.id): 
    print(instance)
