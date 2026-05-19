# 🤖 AI Platform Observability

<div align="center">

A Kubernetes-native observable AI inference platform built using **FastAPI**, **Ollama**, **Docker**, **Prometheus**, **Grafana**, **Kubernetes**, **HPA autoscaling**, and **Helm**.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/K8s-Orchestration-326ce5.svg)](https://kubernetes.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 Overview

This project demonstrates how to build, monitor, containerize, scale, and deploy AI inference workloads using **production-style infrastructure** and **platform engineering practices**. It bridges the gap between local AI experimentation and production-ready deployment.

> **Most AI projects stop at chatbot demos.** This project focuses on **AI infrastructure**, **platform engineering**, **observability**, **autoscaling**, and **Kubernetes-native deployment**.

---

## 🏗️ Architecture

```text
User Request
      ↓
┌─────────────┐
│  FastAPI       │    ← AI API Gateway
│  Inference     │
└──────┬──────┘
        ↓
┌─────────────┐
│   Ollama       │    ← Local LLM Inference Engine
│  LLM Model     │
└──────┬──────┘
        ↓
┌─────────────┐
│ Prometheus     │    ← Metrics Collection & Scraping
└──────┬──────┘
        ↓
┌─────────────┐
│  Grafana       │    ← Visualization & Dashboards
└─────────────┘
        ↑
┌─────────────┐
│ Kubernetes    │    ← Orchestration + HPA Autoscaling
└─────────────┘
```

---

## ✨ Features

### Core Capabilities
- ✅ **FastAPI AI Inference API** — High-performance async API for LLM interactions
- ✅ **Local LLM Inference** — Powered by Ollama for private, on-premise AI
- ✅ **Dockerized Deployment** — Reproducible containerized environments
- ✅ **Multi-container Orchestration** — Docker Compose for local development

### Observability & Monitoring
- ✅ **Prometheus Metrics Instrumentation** — Real-time request counting, latency tracking, and throughput metrics
- ✅ **Grafana Dashboards** — Visualize AI service performance, traffic patterns, and autoscaling behavior
- ✅ **Health Checks** — Liveness and readiness probes for reliable deployments

### Kubernetes & DevOps
- ✅ **Kubernetes Deployment Manifests** — Production-ready YAML configurations
- ✅ **Horizontal Pod Autoscaler (HPA)** — CPU-based auto-scaling (min: 2, max: 10)
- ✅ **Helm Chart Packaging** — Templated, reusable deployment packages
- ✅ **Resource Management** — Proper resource requests and limits defined

### Production Best Practices
- Infrastructure automation
- Distributed systems debugging patterns
- GitOps-ready structure
- Clean separation of concerns

---

## 🛠️ Tech Stack

| Category        | Technologies                                                          |
| --------------  | --------------------------------------------------------------------  |
| **Language**    | Python 3.9+                                                           |
| **Framework**   | FastAPI, Uvicorn                                                      |
| **AI/LLM**      | Ollama                                                                |
| **Containers**  | Docker, Docker Compose                                                |
| **Orchestration**| Kubernetes, KIND (Kubernetes IN Docker)                              |
| **Package Manager** | Helm v3+                                                        |
| **Monitoring**  | Prometheus, Grafana                                                   |
| **CI/CD**       | *(Planned: GitHub Actions, ArgoCD)*                                   |

---

## 📁 Project Structure

```text
ai-platform-observability/
├── app/
│    └── main.py                    # FastAPI application
├── monitoring/
│    └── prometheus.yml             # Prometheus configuration
├── k8s/                           # Kubernetes manifests
│    ├── ai-api-deployment.yaml
│    ├── ai-api-service.yaml
│    └── ai-api-hpa.yaml
├── helm/
│    └── ai-platform/               # Helm chart
│        ├── Chart.yaml
│        ├── values.yaml
│        └── templates/
│            ├── deployment.yaml
│            ├── hpa.yaml
│            ├── service.yaml
│            └── NOTES.txt
├── Dockerfile                     # Container build file
├── docker-compose.yml             # Local stack orchestration
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md                      # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python** 3.9+ installed
- **Docker** and **Docker Compose** installed
- **Kubernetes** cluster (local KIND or remote)
- **Helm** v3+ installed (for Helm deployment)
- **Ollama** installed and running (for LLM inference)

---

### 🐍 Running Locally (FastAPI Only)

#### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate          # On macOS/Linux
# venv\Scripts\activate           # On Windows
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Start Ollama

Ensure Ollama is running with your preferred model:

```bash
ollama serve                      # Start Ollama server
ollama pull llama3                # Download a model (e.g., Llama 3)
```

#### 4. Run FastAPI Application

```bash
uvicorn app.main:app --reload
```

#### 5. Open Swagger UI

Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to explore the interactive API documentation.

---

### 🐳 Docker Deployment

#### 1. Build Docker Image

```bash
docker build -t ai-platform-observability:latest .
```

#### 2. Run Docker Compose Stack

```bash
docker compose up -d
```

#### 3. Verify Containers

```bash
docker ps
```

You should see the following services running:
- **FastAPI API** — AI inference service
- **Prometheus** — Metrics collection
- **Grafana** — Dashboard visualization

---

### 🔍 Access Services

#### Grafana Dashboard
- **URL**: [http://localhost:3000](http://localhost:3000)
- **Username**: `admin`
- **Password**: `admin`

> 💡 **Note**: On first login, you'll be prompted to change the default password.

#### Prometheus
- **URL**: [http://localhost:9090](http://localhost:9090)

**Useful Metrics to Explore:**
| Metric                                    | Description                            |
| ----------------------------------------  | -------------------------------------  |
| `llm_requests_total`                      | Total number of LLM inference requests |
| `llm_request_latency_seconds_sum`         | Sum of request latencies               |
| `llm_request_latency_seconds_count`       | Count of latency samples               |
| `llm_request_latency_seconds_avg`         | Average request latency                |

---

### ☸️ Kubernetes Deployment

#### 1. Create KIND Cluster

```bash
kind create cluster --name k8-prac
```

#### 2. Load Docker Image Into KIND

```bash
kind load docker-image ai-platform-observability:latest --name k8-prac
```

#### 3. Deploy Kubernetes Manifests

```bash
kubectl apply -f k8s/
```

#### 4. Verify Resources

```bash
# Check pods
kubectl get pods

# Check services
kubectl get svc

# Check HPA status
kubectl get hpa
```

---

### 🏎️ Horizontal Pod Autoscaler (HPA)

The project includes a declarative HPA configuration with the following features:

- **CPU-based autoscaling** — Automatically adjusts replicas based on CPU utilization
- **Minimum replicas**: `2`
- **Maximum replicas**: `10`
- **Target CPU utilization**: Configurable (typically 70%)
- **Automatic scaling during high load** — No manual intervention required

#### Test the HPA

Generate load to trigger autoscaling:

```bash
# Run a simple load test
for i in {1..100}; do
  curl -X POST http://localhost:8080/generate \
      -H "Content-Type: application/json" \
      -d '{"prompt": "Explain Kubernetes scheduling"}' &
done
wait

# Watch HPA scaling events
kubectl get hpa -w
```

---

### 🎩 Helm Deployment

#### 1. Validate Helm Chart

```bash
cd helm/ai-platform
helm lint .
```

#### 2. Render Templates (Dry Run)

```bash
helm template ai-release .
```

#### 3. Install Helm Release

```bash
helm install ai-release .
```

#### 4. Verify Helm Release

```bash
helm list
kubectl get all
```

---

## 📡 API Endpoints

### Generate AI Response

```http
POST /generate
Content-Type: application/json

{
    "prompt": "Explain Kubernetes scheduling"
}
```

**Response:**

```json
{
    "response": "Kubernetes scheduling is the process by which the Kubernetes control plane assigns pods to nodes...",
    "model": "llama3",
    "timestamp": "2024-01-15T10:30:00Z"
}
```

---

### Metrics Endpoint

```http
GET /metrics
Content-Type: text/plain; version=0.0.4
```

Prometheus scrapes this endpoint for:
- **Request count** — Total and per-endpoint request counts
- **Request latency** — Histogram of response times
- **Throughput metrics** — Requests per second, error rates

---

## 📊 Observability

### What Prometheus Collects
- ✅ Request count (`llm_requests_total`)
- ✅ Latency metrics (`llm_request_latency_seconds_*`)
- ✅ Throughput metrics (requests/second)
- ✅ Error rates and success ratios

### What Grafana Visualizes
- ✅ Request traffic over time
- ✅ Response latency distributions
- ✅ Autoscaling behavior (pod count changes)
- ✅ Kubernetes workload metrics
- ✅ Service health status

---

## 🏭 Production Concepts Demonstrated

This project demonstrates practical AI platform engineering concepts used in production environments:

| Concept                            | Implementation                                                         |
| ---------------------------------  | ---------------------------------------------------------------------  |
| **AI Inference Platform Engineering** | Structured API with monitoring, error handling, and scaling        |
| **Kubernetes Orchestration**       | Multi-container deployments with proper lifecycle management           |
| **Containerized AI Services**      | Dockerized inference engine with reproducible builds                   |
| **Observability & Monitoring**     | Metrics-driven debugging with Prometheus + Grafana                     |
| **Autoscaling AI Workloads**       | HPA for dynamic resource allocation based on demand                    |
| **Resource Management**            | CPU/memory requests and limits to ensure fair scheduling               |
| **Helm Templating**                | Reusable, configurable deployment packages                             |
| **Production Deployment Workflows**   | From local dev to Kubernetes with standardized processes            |
| **Distributed Systems Debugging**     | Structured logging, health checks, and metric collection             |
| **Infrastructure Automation**       | Git-managed infrastructure as code                                    |

---

## 🎯 Why This Project Matters

Most AI projects stop at chatbot demos. They rarely address:

- ❌ How to **monitor** AI inference in production
- ❌ How to **scale** LLM services under load
- ❌ How to **containerize** AI workloads reliably
- ❌ How to **observe** latency, throughput, and errors at scale

This project fills that gap by demonstrating:

> ✅ **AI Infrastructure** — Production-grade deployment patterns  
> ✅ **Platform Engineering** — Standardized, repeatable workflows  
> ✅ **Observability** — Metrics, logging, and dashboards  
> ✅ **Autoscaling** — Dynamic resource management for AI workloads  
> ✅ **Kubernetes-Native Deployment** — Cloud-agnostic orchestration  

---

## 🚧 Future Improvements

Contributions are welcome! Here's what's on the roadmap:

### Short-term
- [ ] **GitHub Actions CI/CD** — Automated testing and deployment pipelines
- [ ] **OpenTelemetry Tracing** — Distributed tracing across services
- [ ] **Ingress Controller** — External access with TLS termination
- [ ] **Rate Limiting** — API rate limiting to prevent abuse

### Medium-term
- [ ] **ArgoCD GitOps Deployment** — Declarative GitOps workflows
- [ ] **Kubernetes-Native Ollama Deployment** — Run Ollama within K8s clusters
- [ ] **Distributed Inference** — Multi-node LLM inference support
- [ ] **Request Queueing** — Asynchronous processing for high-volume workloads

### Long-term
- [ ] **GPU Node Support** — NVIDIA GPU acceleration via Kubernetes Device Plugins
- [ ] **Advanced Monitoring Dashboards** — Custom Grafana panels for AI-specific metrics
- [ ] **Multi-Model Support** — Switch between different LLMs dynamically
- [ ] **A/B Testing Framework** — Compare model performance in production

---

## 📸 Screenshots

> *Add screenshots here to showcase:*
> - Grafana dashboards showing live metrics
> - Prometheus query results for AI inference metrics
> - Kubernetes pods and HPA scaling events
> - Helm release management
> - Swagger UI interactive API documentation

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use conventional commits format
- Update documentation for any new features
- Ensure all tests pass before submitting

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs) (after running locally)
- **Grafana Dashboard**: [http://localhost:3000](http://localhost:3000) (after Docker Compose up)
- **Prometheus UI**: [http://localhost:9090](http://localhost:9090) (after Docker Compose up)

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) — Modern, fast web framework for building APIs
- [Ollama](https://ollama.com/) — Run large language models locally
- [Kubernetes](https://kubernetes.io/) — Container orchestration platform
- [Prometheus](https://prometheus.io/) — Monitoring system and time series database
- [Grafana](https://grafana.com/) — Observability and data visualization platform
- [Helm](https://helm.sh/) — The package manager for Kubernetes

---

<div align="center">

**Built with ❤️ for AI Platform Engineers**

⭐ If this project helped you, please give it a star!

</div>