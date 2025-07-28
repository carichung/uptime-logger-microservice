# Uptime Logger Microservice 🚦

A cloud-ready microservice built with **FastAPI**, **Docker**, and **Terraform** for logging and monitoring website uptime. Easily deployable to AWS EC2 with full Infrastructure as Code.

---

## Features

- REST API to check the uptime of configurable URLs
- Logs results to a SQLite database
- Containerized with Docker & Docker Compose
- Automated AWS deployment with Terraform
- Ready for cloud-native expansion (RDS, ECS, EKS, etc.)

---

## Architecture

[User/Browser]
|
v
[FastAPI App in Docker] <----> [SQLite DB]
|
v
[AWS EC2] (Provisioned by Terraform)


---

## Quick Start (Local Development)

**Clone the repo:**
git clone https://github.com/carichung/uptime-logger-microservice.git
cd uptime-logger-microservice
Run locally with Docker Compose:

docker compose up --build
Visit: http://localhost:8000/check-uptime

Cloud Deployment (AWS Example)
Build and push your Docker image to Docker Hub:

docker login
docker tag uptime-logger YOUR_DOCKERHUB_USERNAME/uptime-logger:latest
docker push YOUR_DOCKERHUB_USERNAME/uptime-logger:latest

Configure your AWS key pair and find a valid Ubuntu AMI for your region.

Edit infra-terraform/main.tf:

Update the AMI ID, key name, and Docker image as above.

Deploy with Terraform:

cd infra-terraform
terraform init
terraform apply
Access your app:
http://<EC2_PUBLIC_IP>:8000/check-uptime

Configuration
URLs to monitor:
Edit the urls_to_monitor list in app/main.py.

Database:
Default is SQLite. For production, you can switch to RDS/PostgreSQL.

File Structure
css
Copy
Edit
uptime-logger-microservice/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── infra-terraform/
    └── main.tf
    


Author
Name: Cari (GitHub)
Role: Cloud Student


License
MIT
