pipeline {
    agent {
        docker {
            image 'docker' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'docker stop test1'
                sh 'docker swarm leave -f'
                sh 'docker build -t jesusdiaz24/test1 .'
                sh 'docker swarm init'
                sh 'docker stack deploy -c docker-compose.yml test1'
            }
        }
        stage('Test'){
            agent{
                docker{
                    image 'python:3-alpine'
                }
            }
            steps{
                sh 'python3 -m pip install requests'
                sh 'python3 ./test.py'
                sh 'python3 ./commandlinetest.py'
            }
        }
        stage('Deploy'){
            steps{
                sh 'docker login -u jesusdiaz24 -p TempP4ssword!'
                sh 'docker push jesusdiaz24/test1'
            }
        }

    }
}
