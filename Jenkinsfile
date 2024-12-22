pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stages{
            stage('Build')
            steps{
                sh 'python app.py'
            }
        }
        stage('After build Stage') { 
            steps {
                echo 'This is another stage'
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
