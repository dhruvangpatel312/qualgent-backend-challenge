# QualGent Backend Challenge – Emulator Job System

## Overview

This project contains a CLI tool and a backend server designed to submit, track, and manage test jobs for mobile app testing infrastructure. It mimics the functionality needed to queue and run AppWright-style tests on Android (and eventually iOS) emulators hosted on Google Cloud Platform (GCP).


##  Project Structure

###  main.py – FastAPI Backend Server
- `POST /submit`: Submits a job with org ID, app version, test path, priority, and target (device/emulator)
- `GET /status/{job_id}`: Returns status for a given job ID
- Stores jobs in memory (`job_queue` and `job_status` dictionaries)

###  qgjob.py – CLI Tool
- `submit`: Sends a job submission request to the backend server
- `status`: Checks status of a previously submitted job by its ID

---

##  How to Run the Project

### 1. Start Backend Server
```bash
uvicorn main:app --reload
