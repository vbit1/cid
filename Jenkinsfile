pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bash 'pip install -r requirements.txt'
                // installed req
            }
        }

        stage('Run Tests') {
            steps {
                //running tests
                bash 'python -m unittest discover -s . -p "test_*.py"'
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
