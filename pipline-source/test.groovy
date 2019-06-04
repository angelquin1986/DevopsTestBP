pipeline {
  agent { docker { image 'python:3.6' } }
  stages {
    stage('build') {
      steps {
        sh 'virtualenv .venv'
        sh 'source .venv/bin/activate'
        sh 'pip install -r requirements.txt'
      }
    }
  }
}