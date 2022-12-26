node {

        
    stage('Build image') {
       dockerImage = docker.build("nezimov/prakt4:latest")
    }
    
    stage('Pushing Image'){
        environment{
            registryCredential = 'DOCKERHUB_LOGIN'
        }
        steps{
            script{
                docker.withRegistry( 'http://registry.hub.docker.com', registryCredential ){
                    dockerImage.push("latest")
                }
            }
        }
    }
}

pipeline {

  environment {
    dockerimagename = "nezimov/prakt4"
    dockerImage = ""
  }

  agent any

  stages {

    stage('Git Clone'){
    	git branch: 'main', credentialsId: 'GIT_HUB_CREDENTIALS', url: 'https://github.com/Andrey-Mefimov/git-test'
        }

    stage('Build Docker Image') {  
    steps{                     
    sh 'docker-compose build'     
    echo 'Docker-compose-build Build Image Completed'                
    }           
}

    stage('Pushing Image') {
      environment {
               registryCredential = 'dockerhublogin'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Deploying App to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "deploymentservice.yml", kubeconfigId: "kubernetes")
        }
      }
    }

  }

}
