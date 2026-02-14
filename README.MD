# DevOps Infrastructure Lab 🚀

A full-stack infrastructure project demonstrating the evolution from traditional VM provisioning to Cloud-Native Kubernetes orchestration.

## 🏗️ Architecture Overview

### Phase 1: Ansible (VM-based) 🛠️
Legacy infrastructure provisioning using **Ansible**.
- **Tech Stack:** Nginx, Python Flask, PostgreSQL.
- **Key Features:**
  - Role-based architecture.
  - Security via Ansible Vault.
  - Automated connectivity checks.
  - CI/CD with GitHub Actions (Linting & Syntax Checks).

### Phase 2: Kubernetes (Container-based) ☸️
Modern Cloud-Native deployment using **Kind (Kubernetes in Docker)**.
- **Tech Stack:** Docker, Kubernetes, Python.
- **Key Features:**
  - Declarative YAML manifests.
  - Persistent Volumes for Database reliability.
  - ConfigMaps & Secrets management.
  - Self-healing architecture (Liveness/Readiness probes).

## 🚀 Quick Start

### Prerequisites
- Docker & WSL2
- Ansible & Molecule
- Kind & Kubectl

### Running Phase 2 (Kubernetes)
1. Create the cluster:

```bash
    kind create cluster --config phase-2-kubernetes/kind-config.yaml
```

2. Build & Load the image:

```bash
    cd phase-2-kubernetes/app
    docker build -t my-python-app:v1 .
    kind load docker-image my-python-app:v1 --name ansible-lab
```
3. Deploy manifests:

```bash
    kubectl apply -f phase-2-kubernetes/k8s/
```

4. Access the App:

```bash
    kubectl port-forward -n ansible-lab service/python-app-service 8080:80
    # Open browser at http://localhost:8080
```