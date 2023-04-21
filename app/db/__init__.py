from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(getenv("DB_URL"), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
mapper_registry = registry()
Base = mapper_registry.generate_base()
