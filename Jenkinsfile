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
            // Remove nohup, use a plain docker build command instead
            sh 'docker build -t ${DOCKER_FRONTEND_IMAGE}:${DOCKER_TAG} ./frontend'
        }
    }
}


        stage('Build Backend') {
            steps {
                script {
                    // Build backend Docker image
                    sh 'docker build -t ${DOCKER_BACKEND_IMAGE}:${DOCKER_TAG} ./backend'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Example test for backend (can be expanded with real tests)
                    sh 'docker run ${DOCKER_BACKEND_IMAGE}:${DOCKER_TAG} npm test'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    // Push Docker images to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                        sh 'docker push ${DOCKER_FRONTEND_IMAGE}:${DOCKER_TAG}'
                        sh 'docker push ${DOCKER_BACKEND_IMAGE}:${DOCKER_TAG}'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Run the Docker Compose file to deploy services
                    sh 'docker-compose -f docker-compose.yml up -d'
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
