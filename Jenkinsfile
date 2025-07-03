pipeline {

    agent any

    stages {
       
        stage('Build and Test in Docker') {
            agent {
                
                docker { image 'python:3.9-slim' }
            }
            steps {
                
                echo 'Checking out code...'
                checkout scm

                
                echo 'Installing dependencies...'
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'

                
                echo 'Running tests...'
                sh '. venv/bin/activate && pytest --junitxml=reports/results.xml tests/'
            }
        }
    }
    
    post {
        always {
            echo 'Publishing test results...'
           
            junit 'reports/results.xml'
            
            cleanWs()
        }
    }
}
