pipeline {
    agent any // Agente inicial para orquestrar o pipeline.

    stages {
        // ========== ESTÁGIO DE BUILD (CONTÊINER 1) ==========
        stage('Build') {
            agent {
                // Inicia o primeiro contêiner Docker isolado.
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo 'Build Container: Checking out code...'
                checkout scm

                echo 'Build Container: Installing dependencies...'
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'

                // "Guarda" o diretório inteiro do projeto para o próximo estágio.
                // 'project_files' é o nome que damos para o nosso "pacote".
                echo 'Build Container: Stashing files...'
                stash name: 'project_files', includes: '**/*'
            }
        }

        // ========== ESTÁGIO DE TESTE (CONTÊINER 2) ==========
        stage('Test') {
            agent {
                // Inicia um segundo contêiner Docker, novo e isolado.
                docker { image 'python:3.9-slim' }
            }
            steps {
                // Pega os arquivos que foram "guardados" pelo estágio de Build.
                echo 'Test Container: Unstashing files...'
                unstash 'project_files'

                echo 'Test Container: Running tests...'
                // Ativa o ambiente virtual (que foi criado no stash) e roda os testes.
                sh '. venv/bin/activate && pytest --junitxml=reports/results.xml tests/'
            }
        }
    }

    // Bloco final para publicar os resultados e limpar.
    post {
        always {
            echo 'Publishing test results...'
            junit 'reports/results.xml'
            cleanWs()
        }
    }
}
