pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
       stage('Build') {
            steps {
                sh 'python app.py'
            }
        }
        stage('After build Stage') { 
            steps {
                echo 'This is afte build stage'
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
