pipeline {
    agent any
    
    environment {
        REPO_URL = 'https://github.com/shaurya2093/DevOps-unit_testing.git'  // Your GitHub repository URL
        DOCKER_FRONTEND_IMAGE = 'shaurya/frontend-app'  // Docker image for frontend
        DOCKER_BACKEND_IMAGE = 'shaurya/backend-app'  // Docker image for backend
        DOCKER_TAG = 'latest'
    }

    triggers {
        // Poll SCM for changes every minute (or use webhook for real-time triggers)
        pollSCM('https://d813-2409-40c2-1008-ae8c-5102-1ce3-9d14-d3e2.ngrok-free.app')  // You can replace this with a webhook if preferred
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
                    // Build frontend Docker image (Windows format for bat)
                    bat 'docker build -t %DOCKER_FRONTEND_IMAGE%:%DOCKER_TAG% ./frontend'
                }
            }
        }

        stage('Build Backend') {
            steps {
                script {
                    // Build backend Docker image (Windows format for bat)
                    bat 'docker build -t %DOCKER_BACKEND_IMAGE%:%DOCKER_TAG% ./backend'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // Push Docker images to Docker Hub using credentials from environment variables
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin'
                        bat 'docker push %DOCKER_FRONTEND_IMAGE%:%DOCKER_TAG%'
                        bat 'docker push %DOCKER_BACKEND_IMAGE%:%DOCKER_TAG%'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Run the Docker Compose file to deploy services
                    bat 'docker-compose -f docker-compose.yml up -d'
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
