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
                //bash 'python app.py'
                echo 'in build checking'
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
