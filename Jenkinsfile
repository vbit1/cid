pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
       stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vbit1/cid.git' 
            }
        }
        stage('Build') {
            steps {
                bash 'which python3'
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
