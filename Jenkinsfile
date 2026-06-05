pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kanishkajain1411/flask-devops-project'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
                sh 'docker build -t flask-app .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh '''
                docker login -u your-dockerhub-username -p your-password
                docker tag flask-app your-dockerhub-username/flask-app:latest
                docker push your-dockerhub-username/flask-app:latest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker pull your-dockerhub-username/flask-app:latest
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 5000:5000 --name flask-app your-dockerhub-username/flask-app:latest
                '''
            }
        }
    }
}
