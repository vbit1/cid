pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sample-python-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment logic here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
