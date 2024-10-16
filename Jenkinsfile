pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/shaurya2093/DevOps-unit_testing.git' // Update with your GitHub repository
        DOCKER_IMAGE_NAME = 'shaurya/backend-app'  // Your Docker Hub image name
        DOCKER_TAG = 'latest'  // Change to version as needed
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository from GitHub
                git branch: 'main', url: "${https://github.com/shaurya2093/DevOps-unit_testing.git}" 
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for backend
                    sh 'docker-compose up --build'
                }
            }
        }
    

        stage('Deploy') {
            steps {
                script {
                    // Example command to run the container on your server
                    sh 'docker run -d -p 8081:80'
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

