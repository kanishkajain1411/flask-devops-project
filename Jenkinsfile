pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kanishkajain1411/flask-devops-project'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag flask-app kanishkajain1411/flask-app:latest'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    docker push kanishkajain1411/flask-app:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker pull kanishkajain1411/flask-app:latest
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 5000:5000 --name flask-app kanishkajain1411/flask-app:latest
                '''
            }
        }
    }
}
