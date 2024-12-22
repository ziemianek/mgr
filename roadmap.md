
## Roadmap

### Phase 1: Initial Setup
1. **Setup AWS Infrastructure**
   - Setup AWS account and configure IAM roles
   - Create a VPC using Terraform
   - Setup EKS cluster using Terraform
   - Configure kubectl to connect to EKS cluster

### Phase 2: Application Preparation
2. **Database Improvements**
   - Fix warnings in MySQL container
   - Create health checks for MySQL DB
   - Add persistent volume to DB
   - Enhance database security

3. **GitHub Repository Setup**
   - Better setup for GitHub repo
   - Move API reference to docs/

4. **Docker and Ansible Enhancements**
   - Add parameters to docker_compose role
   - Add role to build API image
   - Add generic image building step to Ansible
   - Better design for roles to create/delete local environment

### Phase 3: Deployment and CI/CD
5. **Kubernetes Deployment**
   - Use Kubernetes to run app
   - Create Kubernetes manifests for the application
   - Deploy the application to EKS using kubectl

6. **CI/CD Pipeline**
   - Setup GitHub Actions for CI/CD
   - Configure GitHub Actions to build and push Docker images
   - Configure GitHub Actions to deploy to EKS

### Phase 4: GitOps and Frontend
7. **GitOps Implementation**
   - Do GitOps research
   - Setup GitOps

8. **Frontend Development**
   - Create simple frontend for the app

### Phase 5: Miscellaneous
9. **General Improvements**
   - Rethink the current setup and improve