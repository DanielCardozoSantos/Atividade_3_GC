pipeline {
    agent any

    stages {
        stage('Test: Listar Arquivos') {
            steps {
                // O checkout já aconteceu antes deste passo.
                // Se chegarmos aqui, significa que o código foi baixado.
                echo '>>> O checkout do Git parece ter funcionado!'
                echo '>>> Verificando os arquivos na pasta de trabalho (workspace):'
                
                // Comando para listar arquivos (funciona em Linux e Windows)
                sh 'ls -la' 
            }
        }
    }
    
    post {
        always {
            echo '>>> Fim do pipeline de teste.'
        }
    }
}
