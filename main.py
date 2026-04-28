from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI(title="EventPlanner Spec")

class EventType(str, Enum):
    workshop = "Workshop"
    teambuilding = "TeamBuilding"
    dinner = "Dinner"

class Event(BaseModel):
    event_name: str
    event_type: EventType
    attendees: int
    total_estimated_cost: float

@app.post("/analyze-event")
def analyze_event(event: Event):
    cost_per_person = event.total_estimated_cost / event.attendees
    
    if cost_per_person > 100:
        status = "Rejected: Over Budget"
    elif 50 <= cost_per_person <= 100:
        status = "Needs Manager Approval"
    else:
        status = "Auto-Approved"
        
    return {
        "event": event.event_name,
        "cost_per_person": round(cost_per_person, 2),
        "status": status,
        "policy_applied": "Global Expense Policy 2024"
    }
