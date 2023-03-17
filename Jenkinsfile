pipeline {
    agent any
    environment{
        DOCKER_TAG = "0.0.4"
    }

    stages {
        stage('Git Checkout') {
            steps {
                git url:'https://github.com/javahometech/python-app', branch: 'master'
            }
        }
        stage('Docker Build') {
            steps {
                sh "docker build -t kammana/pyapp:${DOCKER_TAG} ."
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'pwd', usernameVariable: 'usr')]) {
                    sh "docker login -u ${usr} -p ${pwd}"
                }
            }
        }
        stage('Docker Push') {
            steps {
               sh "docker push kammana/pyapp:${DOCKER_TAG}"
            }
        }
        stage("Dev Deploy"){
            steps{
                sshagent(['docker-ssh']) {
                    sh "ssh -o StrictHostKeyChecking=no ec2-user@172.31.51.1 docker rm -f pyapp"
                    sh "ssh  ec2-user@172.31.51.1 docker run -d -p 8080:5000 --name pyapp kammana/pyapp:${DOCKER_TAG}"
                }
            }
        }
    }
}
