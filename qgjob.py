import argparse
import requests

BASE_URL = "http://127.0.0.1:8000"

def submit_job(org_id, app_version_id, test_path, priority, target):
    payload = {
        "org_id": org_id,
        "app_version_id": app_version_id,
        "test_path": test_path,
        "priority": priority,
        "target": target
    }
    response = requests.post(f"{BASE_URL}/submit", json=payload)
    if response.status_code == 200:
        print("✅ Job submitted successfully!")
        print(response.json())
    else:
        print("❌ Failed to submit job")
        print(response.text)

def check_status(job_id):
    response = requests.get(f"{BASE_URL}/status/{job_id}")
    if response.status_code == 200:
        print("📦 Job Status:")
        print(response.json())
    else:
        print("❌ Failed to get status")
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description="QualGent CLI - qgjob")
    subparsers = parser.add_subparsers(dest="command")

    # Submit command
    submit_parser = subparsers.add_parser("submit")
    submit_parser.add_argument("--org-id", required=True)
    submit_parser.add_argument("--app-version-id", required=True)
    submit_parser.add_argument("--test", required=True)
    submit_parser.add_argument("--priority", default="normal")
    submit_parser.add_argument("--target", choices=["device", "emulator", "browserstack"], required=True)

    # Status command
    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--job-id", required=True)

    args = parser.parse_args()

    if args.command == "submit":
        submit_job(args.org_id, args.app_version_id, args.test, args.priority, args.target)
    elif args.command == "status":
        check_status(args.job_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
