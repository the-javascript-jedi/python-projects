from fastapi import FastAPI
app=FastAPI()

#  uvicorn books:app --reload
@app.get("/api-endpoint")
async def first_api():
    return {"message":"Hello Nithin"}