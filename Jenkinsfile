pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
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
