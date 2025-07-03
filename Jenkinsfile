pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                dockerfile { filename 'Dockerfile.build' } 
            }
            steps {
                echo "--- Inspecionando a sintaxe do código Python ---"
                sh 'python -m py_compile src/conversor.py'
            }
        }

        stage('Test') {
            agent {
                dockerfile { filename 'Dockerfile.test' } 
            }
            steps {
                echo "--- Executando testes com Pytest ---"
                sh 'pytest --junitxml=report.xml tests/' // Gera um relatório que o Jenkins entende
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }
    }
    post {
        always {
            echo "Pipeline finalizada. Limpando o workspace."
            cleanWs() 
        }
    }
}
