// Jenkinsfile

pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.9-slim'
                    // Adicione esta linha para rodar como root
                    args '--user root'
                }
            }
            steps {
                echo 'Iniciando o estágio de Build...'
                sh 'pip install -r requirements.txt'
                echo 'Build concluído com sucesso!'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.9-slim'
                    // Adicione esta linha também no estágio de Teste
                    args '--user root'
                }
            }
            steps {
                echo 'Iniciando o estágio de Teste...'
                sh 'pip install -r requirements.txt'
                sh 'pytest --junitxml=test-results.xml tests/'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finalizado. Limpando o workspace.'
            cleanWs()
        }
    }
}
