from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()  

job_queue = {}
job_status = {}

class Job(BaseModel):
    org_id: str
    app_version_id: str
    test_path: str
    priority: str
    target: str

@app.post("/submit")
def submit_job(job: Job):
    job_id = str(uuid.uuid4())
    job_queue[job_id] = job.dict()
    job_status[job_id] = "queued"
    return {"job_id": job_id, "status": "queued"}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id not in job_status:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": job_id, "status": job_status[job_id]}
