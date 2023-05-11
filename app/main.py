"""Main module"""
import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.places.routes import weather_router
from app.weather_data.routes import weather_data_router


Base.metadata.create_all(bind=engine)


def init_app():
    """
    Initializing app
    Return: FastAPI instance.
    """
    my_app = FastAPI()
    my_app.include_router(weather_router)
    my_app.include_router(weather_data_router)

    return my_app


app = init_app()


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app)
