// Jenkinsfile

pipeline {
    agent any // O pipeline principal roda em qualquer agente disponível

    stages {
        stage('Build') {
            agent {
                // Usa um contêiner Docker com Python para este estágio
                docker {
                    image 'python:3.9-slim'
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
                // Usa outro contêiner Docker isolado para os testes
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                echo 'Iniciando o estágio de Teste...'
                // Instala as dependências também no contêiner de teste
                sh 'pip install -r requirements.txt'
                // Executa os testes e gera um relatório JUnit
                sh 'pytest --junitxml=test-results.xml tests/'
            }
            post {
                // Sempre arquiva os resultados dos testes
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
    post {
        // Ações que acontecem no final do pipeline
        always {
            echo 'Pipeline finalizado. Limpando o workspace.'
            cleanWs()
        }
    }
}
