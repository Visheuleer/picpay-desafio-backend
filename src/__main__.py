from fastapi import FastAPI
from mysqldb import db_connection
from models import Base
from routes import wallet_router



app = FastAPI()
app.include_router(wallet_router)

if __name__ == "__main__":
    import uvicorn
    Base.metadata.create_all(bind=db_connection.engine)
    uvicorn.run(app)




