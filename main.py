from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from controller import MainTasks  # Assuming MainTasks is a class in the controller module

app = FastAPI()

# Initialize the MainTasks class
task = MainTasks.AllTask()

# Define a Pydantic model for request validation (if needed)
class ChoiceModel(BaseModel):
    choice: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}

# Endpoint for cleanup menu
@app.post("/cleanup")
def cleanup_menu(directory: str):
    try:
        # Pass the directory string to the cleanup_menu method
        task.cleanup_menu(directory)
        return {"message": f"Cleanup task executed successfully for directory: {directory}."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint for compress menu
@app.post("/compress")
def compress_menu():
    try:
        # Assuming compress_menu is a function in the same module
        compress_menu()
        return {"message": "Compress task executed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to exit (not applicable in HTTP, but included for completeness)
@app.post("/exit")
def exit_app():
    return {"message": "Exiting the application."}

# Endpoint to handle choices (if you want to keep the choice logic)
@app.post("/task")
def handle_task(choice: ChoiceModel):
    if choice.choice == '1':
        return cleanup_menu()
    elif choice.choice == '2':
        return compress_menu()
    elif choice.choice == '3':
        return exit_app()
    else:
        raise HTTPException(status_code=400, detail="Invalid choice. Please try again.")