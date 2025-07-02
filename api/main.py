# api/main.py

from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI(title="Learn Platform AI Mentor API")

# Define a "route" or "endpoint"
# This decorator tells FastAPI that the function below
# should handle GET requests to the root URL "/"
@app.get("/")
def read_root():
    """
    This is the root endpoint of our API.
    It's a simple health check to see if the service is running.
    """
    return {"message": "Foundation!"}