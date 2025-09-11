# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.openapi.utils import get_openapi
from app import create_app
from dotenv import load_dotenv  # type: ignore

# from .routers import stats

load_dotenv()

app = create_app()
