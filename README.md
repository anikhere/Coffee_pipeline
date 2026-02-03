# Coffee Quality MLOps Pipeline

## 1. Problem Statement

The goal of this project is to build a clean, production-style MLOps pipeline that predicts whether a coffee sample is of **good quality or not** based on its features. The focus of this project is **engineering quality, modular design, and reproducibility**, not model complexity.

---

## 2. Pipeline Stages

The pipeline is designed in clearly separated stages:

1. **Data Ingestion** – Load and validate raw coffee data
2. **Data Validation** – Basic schema and sanity checks
3. **Data Transformation** – Feature preparation for modeling
4. **Model Training** – Train a simple ML model
5. **Model Evaluation** – Compare metrics and select the best model
6. **Experiment Tracking** – Track runs and artifacts using MLflow
7. **Inference Service** – Serve predictions using Flask
8. **Containerization** – Run the full system using Docker

Each stage is modular and independently testable.

---

## 3. How to Run

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the pipeline:

   ```bash
   python main.py
   ```
5. Start the Flask app (for inference):

   ```bash
   python app/app.py
   ```

(Docker support will allow running the entire system using a single command.)

---

## 4. Tech Stack Used

* Python
* Scikit-learn
* MLflow
* Flask
* Docker
* YAML (for configuration)
* Logging module

---

## 5. Folder Structure Explanation

```
coffee-mlops/
│
├── components/        # Core ML pipeline components
├── pipeline/          # Pipeline orchestration logic
├── utils/             # Reusable helper functions
├── config/            # Configuration files (YAML)
├── constants/         # Project-wide constants
├── data/              # Sample / raw data
├── logs/              # Application and pipeline logs
├── tests/             # Unit tests
├── docker/            # Dockerfile and dockerignore
├── app/               # Flask inference service
├── main.py            # Pipeline entry point
└── README.md          # Project documentation
```

The structure follows industry-style separation of concerns and is designed to scale as the project grows.

---

**Note:** This project prioritizes clean architecture, reproducibility, and MLOps best practices over model complexity.
