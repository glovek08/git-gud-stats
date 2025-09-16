from app import create_app
from dotenv import load_dotenv  # type: ignore

load_dotenv()

app = create_app()
