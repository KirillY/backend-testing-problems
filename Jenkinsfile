pipeline {
  agent any
  stages {
    stage('git clone') {
      steps {
        git(url: 'https://github.com/KirillY/backend-testing-problems.git', branch: 'master')
      }
    }
    stage('change dir') {
      steps {
        dir(path: 'backend-testing-problems')
      }
    }
    stage('docker-compose up') {
      steps {
        sh '''docker-compose build
docker-compose up'''
      }
    }
  }
}