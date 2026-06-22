from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    subject: str = "General Inquiry"
    message: str = Field(min_length=10)

@app.post("/contact")
def submit_contact(message: ContactMessage):
    return {
        "status": "success",
        "info": f"Message received from {message.name}."
    }
