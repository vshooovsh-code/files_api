from fastapi import FastAPI
from app.api.v01.files import router as files_router
app = FastAPI()


app.include_router(files_router, prefix="/api/v1", tags=["files"])