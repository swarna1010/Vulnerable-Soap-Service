pipeline{
  agent any 
  stages{
    stage('CICD'){
      steps{
         sh 'pip install -i https://test.pypi.org/simple/ boman-cli-uat==0.22'
         sh '~/.local/bin/boman-cli -a run -cicd jenkins -u https://dashboard.boman.ai/v2/'
      }
    }
  }
}
