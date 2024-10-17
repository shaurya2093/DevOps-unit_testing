pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/shaurya2093/DevOps-unit_testing.git'  // Your GitHub repository URL
        DOCKER_FRONTEND_IMAGE = 'shaurya2093/frontend-app'  // Docker image for frontend
        DOCKER_BACKEND_IMAGE = 'shaurya2093/backend-app'  // Docker image for backend
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository from GitHub
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Build Frontend') {
            steps {
                script {
                    // Build frontend Docker image
                    bat "docker build -t ${DOCKER_FRONTEND_IMAGE}:${DOCKER_TAG} ./frontend"
                }
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    // Build backend Docker image
                    bat "docker build -t ${DOCKER_BACKEND_IMAGE}:${DOCKER_TAG} ./backend"
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        // Login to Docker Hub
                        bat "docker login -u %DOCKERHUB_USER% -p %DOCKERHUB_PASSWORD%"
                    }
                }
            }
        }

        stage('Push Docker Images to DockerHub') {
            steps {
                script {
                    // Push frontend and backend images to Docker Hub
                    bat "docker push ${DOCKER_FRONTEND_IMAGE}:${DOCKER_TAG}"
                    bat "docker push ${DOCKER_BACKEND_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

        stage('Logout from DockerHub') {
            steps {
                script {
                    // Logout from Docker Hub
                    bat 'docker logout'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                script {
                    // Initialize Terraform in the working directory
                    sh 'terraform init'
                }
            }
        }

        stage('Terraform Plan') {
            steps {
                script {
                    // Run Terraform plan to show the execution plan
                    sh 'terraform plan -out=plan.out'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                script {
                    // Apply the Terraform plan
                    sh 'terraform apply -auto-approve plan.out'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    // Verify resources like EKS cluster or services deployed properly
                    sh 'kubectl get svc'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
