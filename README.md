# 🚀 Enterprise DevOps & GitOps Lab

![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-%23EF7B4D.svg?style=for-the-badge&logo=argo&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-%230F1689.svg?style=for-the-badge&logo=helm&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)

## 📌 Project Overview
This repository contains an end-to-end DevOps laboratory showcasing the progression from basic configuration management to a fully automated, immutable Kubernetes infrastructure deployed on Google Cloud Platform (GCP) using the GitOps methodology.

The goal of this project is to demonstrate production-grade practices, including Infrastructure as Code (IaC), secret management, declarative continuous deployment, and comprehensive observability.

## 🏗️ Architecture & Tech Stack

* **Infrastructure Provisioning:** Ansible & GCP Compute Engine (Dynamic Inventory)
* **Container Orchestration:** Kubernetes (K3s - High Availability setup)
* **Package Management:** Helm
* **Continuous Deployment (GitOps):** ArgoCD
* **Secrets Management:** Bitnami Sealed Secrets
* **Observability:** Kube-Prometheus-Stack (Prometheus, Grafana, Alertmanager)
* **Ingress Controller:** Traefik

## 🛣️ Project Evolution (Phases)

This lab was built in iterative phases to establish a solid foundation before adding complexity:

* **Phase 1-3:** Fundamentals of Ansible, local Kubernetes (KinD), and packaging a custom Python application using Helm.
* **Phase 4:** Cloud provisioning using Ansible GCP modules to create VPCs, Firewalls, and ephemeral Virtual Machines.
* **Phase 5:** Multi-node K3s cluster deployment on GCP, handling race conditions, `cloud-init`, and automated token exchange between Master and Worker nodes.
* **GitOps & Observability:** Deployment of ArgoCD to take over cluster management, configuring Sealed Secrets for secure credential handling, and deploying the Prometheus/Grafana stack via Server-Side Apply for full cluster monitoring.

## 💡 Key Features & Best Practices
* **Immutable Infrastructure:** Infrastructure can be fully destroyed and recreated reliably using the `teardown.yml` and `site.yml` Ansible playbooks.
* **Zero-Touch Deployments:** Once the base cluster is up, ArgoCD automatically pulls and synchronizes all cluster configurations and applications directly from the `gitops/` directory.
* **Secure Secrets:** No plain-text passwords exist in this repository. All credentials (including Grafana admin passwords and Database credentials) are cryptographically sealed using `kubeseal`.
* **Dynamic Inventories:** Ansible queries the GCP API in real-time to discover node IP addresses, eliminating hardcoded endpoints.

## 🚀 How to Run (Infrastructure lifecycle)

```bash
# 1. Provision Network and VMs
ansible-playbook provision_network.yml
ansible-playbook provision_vm.yml

# 2. Deploy K3s Cluster & ArgoCD
ansible-playbook -i inventory.gcp.yml site.yml

# 3. Clean up resources (Ephemeral approach)
ansible-playbook teardown.yml
```
---

## 👤 Author

**Justino Boggio**

*DevSecOps Engineer | Cloud Engineer | SRE | Information Systems Engineer*

[LinkedIn](https://www.linkedin.com/in/justino-boggio-75a932204) | [GitHub](https://github.com/JustinoBoggio)