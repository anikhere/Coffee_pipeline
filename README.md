# CoffeeQual — Batch Prediction Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green) ![Docker](https://img.shields.io/badge/Docker-28.2-blue) ![AWS ECR](https://img.shields.io/badge/AWS-ECR-orange) ![AWS EC2](https://img.shields.io/badge/AWS-EC2-orange) ![MLflow](https://img.shields.io/badge/MLflow-DagsHub-purple)

A production-grade MLOps pipeline that predicts coffee quality based on sensory features. Built end-to-end from data ingestion to live EC2 deployment with CI/CD automation.

**Live Demo:** http://13.201.3.243:8080

---

## What It Does

Upload a CSV file of coffee samples with sensory attributes — aroma, density, and other key quality indicators — and the pipeline returns a batch quality prediction for each sample instantly via a FastAPI web interface.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Data Storage | SQLite → CSV |
| ML Training | scikit-learn, GridSearchCV |
| Experiment Tracking | MLflow + DagsHub |
| Artifact Storage | AWS S3 |
| API | FastAPI + Uvicorn |
| Containerization | Docker |
| Image Registry | AWS ECR |
| Deployment | AWS EC2 (Ubuntu 22.04) |
| CI/CD | GitHub Actions |

---

## Pipeline Architecture

```
SQLite Database
      ↓
Data Ingestion → Data Validation → Data Transformation
      ↓
Model Training (GridSearchCV) → Model Evaluation
      ↓
MLflow Tracking (DagsHub) + S3 Artifact Storage
      ↓
FastAPI App → Dockerized → Pushed to ECR
      ↓
GitHub Actions CI/CD → EC2 Deployment
      ↓
Live Batch Prediction Interface
```

---

## Project Structure

```
coffee_pipeline/
├── src/
│   ├── components/          # Ingestion, Validation, Transformation, Trainer, Evaluator
│   ├── pipeline/            # Training pipeline orchestration
│   ├── config/              # Config classes for each component
│   └── utils/               # Helper functions, model utils
├── data/                    # SQLite DB and exported CSV
├── templates/               # FastAPI HTML frontend
├── .github/workflows/       # GitHub Actions CI/CD
├── Dockerfile
├── requirements.txt
└── app.py                   # FastAPI entry point
```

---

## CI/CD Pipeline

Every push to `main` triggers GitHub Actions which:

1. Configures AWS credentials from GitHub Secrets
2. Logs into Amazon ECR
3. Builds the Docker image
4. Pushes the image to ECR

The EC2 instance then pulls the latest image and runs the updated container.

---

## Running Locally

**Prerequisites:** Docker, AWS credentials configured

```bash
git clone https://github.com/tahaanik729/Coffee_pipeline.git
cd Coffee_pipeline
```

Build and run:
```bash
docker build -t coffeepipeline .
docker run -d -p 8080:8080 -e DAGSHUB_USER_TOKEN=your_token coffeepipeline
```

Visit `http://localhost:8080`

---

## Environment Variables

| Variable | Description |
|---|---|
| `DAGSHUB_USER_TOKEN` | DagsHub access token for MLflow tracking |
| `AWS_ACCESS_KEY_ID` | AWS IAM access key |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key |
| `AWS_REGION` | AWS region (ap-south-1) |
| `ECR_LOGIN_ACCESS` | ECR registry URL |
| `ECR_REPO_NAME` | ECR repository name |

---

## Key Learnings

- Modular MLOps pipeline structure separating concerns across components
- MLflow experiment tracking integrated with DagsHub for remote logging
- Docker containerization for reproducible production environments
- AWS S3 for persistent artifact storage across pipeline runs
- GitHub Actions CI/CD for automated build and push to ECR
- EC2 deployment with security group configuration
- Debugging production issues: credential management, port configuration, dependency conflicts

---

## Author

Taha Anik — BCA Student | ML/MLOps Engineer in Progress

[GitHub](https://github.com/tahaanik729) | [DagsHub](https://dagshub.com/tahaanik729)
