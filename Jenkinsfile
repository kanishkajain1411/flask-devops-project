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
            }
        }
    }
}
