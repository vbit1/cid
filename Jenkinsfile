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
                // Checkout code from SCM (replace with your SCM )
                git branch: 'main', url: 'https://github.com/vbit1/cid.git'
            }
        }
       stage('Check for Bash') {
            steps {
                script {
                    try {
                        // Check if bash is available
                        bash 'which bash || echo "bash not found"'
                    } catch (Exception e) {
                        echo "Error: ${e.message}"
                    }
                }
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
