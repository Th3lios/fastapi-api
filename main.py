

from fastapi import FastAPI
from api import users, courses, sections
import sentry_sdk

sentry_sdk.init(
    dsn="https://1373feb551490e49d6ec8580c5fd7423@o1110400.ingest.sentry.io/4506525927276544",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = FastAPI(
    title="FastAPI MLS",
    description="FastAPI MLS",
    version="0.1.0",
    openapi_url="/openapi.json",
    contact={
        "name": "Elias",
        "email": "earayad@hotmail.cl",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)
        
@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0
    
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)