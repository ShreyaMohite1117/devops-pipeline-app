pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = 'shreyamohite1117/devops-pipeline-app'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                bat '"C:\\Users\\rishu\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe" install -r requirements.txt'
                bat '"C:\\Users\\rishu\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe" install pytest'
                bat '"C:\\Users\\rishu\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest test_app.py -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:latest ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat "docker login -u %DOCKERHUB_CREDENTIALS_USR% -p %DOCKERHUB_CREDENTIALS_PSW%"
                bat "docker push %IMAGE_NAME%:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat "kubectl apply -f deployment.yaml"
                bat "kubectl apply -f service.yaml"
                bat "kubectl rollout restart deployment/devops-pipeline-app"
                bat "kubectl rollout status deployment/devops-pipeline-app"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
