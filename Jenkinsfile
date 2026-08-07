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

        stage('Debug Credentials') {
            steps {
                bat "echo Username is: %DOCKERHUB_CREDENTIALS_USR%"
                bat "echo First 4 chars of token: %DOCKERHUB_CREDENTIALS_PSW:~0,4%"
                bat "echo Last 4 chars of token: %DOCKERHUB_CREDENTIALS_PSW:~-4%"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                bat "echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin"
                bat "docker push %IMAGE_NAME%:latest"
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
