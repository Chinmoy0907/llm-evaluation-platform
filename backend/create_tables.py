from backend.database.db import engine
from backend.database.db import Base

from backend.database import models

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")