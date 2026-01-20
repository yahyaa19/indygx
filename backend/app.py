from fastapi import FastAPI
from .api.company_full_profile import router as company_router
from .api.company_secondary_routes import router as company_secondary_router

app = FastAPI(
    title="IndyGX Company Intelligence API",
    version="1.0.0",
)

@app.get("/", tags=["system"])
def read_root():
    return {"message": "Welcome to the IndyGX Company Intelligence API"}

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}

# Register routers
app.include_router(
    company_router,
    prefix="/companies",
    tags=["companies"]
)


# ...
# Rest of the code
app.include_router(
    company_secondary_router,
    prefix="/company-secondary",
    tags=["company-secondary"]
)