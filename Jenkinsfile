pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
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
