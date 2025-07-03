pipeline {
    agent any // O pipeline principal roda no agente do Jenkins

    stages {
        stage('Build') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Iniciando o stage de Build...'
                sh 'python -m venv venv'
                sh 'venv/bin/pip install -r requirements.txt'
                echo 'Dependências instaladas.'
            }
        }
        stage('Test') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Iniciando o stage de Teste...'
                sh 'venv/bin/pip install -r requirements.txt' // Instala dependências de novo no container de teste
                sh 'venv/bin/pytest --junitxml=test-reports/results.xml tests/test_conversor.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
