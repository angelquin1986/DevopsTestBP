pipeline {
    agent { docker { image 'python:3.6.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}