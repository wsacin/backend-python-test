from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from alayatodo import app

engine = create_engine('sqlite:///' + app.config['DATABASE'],
                       convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import alayatodo.models
    Base.metadata.create_all(bind=engine)
