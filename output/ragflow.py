from fastapi import FastAPI
from pydantic import BaseModel
from adapter import adapter
import uuid

app = FastAPI()

# --- MODELS --- #

class SessionRequest(BaseModel):
    pass

class CompletionRequest(BaseModel):
    question: str
    stream: bool
    session_id: str

# --- ENDPOINTS --- #

@app.post("/api/v1/agents/{flow_id}/sessions")
def create_session(flow_id: str, _: SessionRequest):
    new_session_id = str(uuid.uuid4())
    return {
        "session_id": new_session_id,
        "flow_id": flow_id
    }

@app.post("/api/v1/agents/{flow_id}/completions")
def handle_completion(flow_id: str, data: CompletionRequest):
    adapted_response = adapter(
        question=data.question,
        session_id=data.session_id,
        flow_id=flow_id
    )
    return adapted_response
