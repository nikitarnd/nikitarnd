pipeline {
  agent any
  stages {
    stage('wait') {
      steps {
        waitForBuild(runId: '123', propagate: true)
      }
    }

  }
}