pipeline {
  agent any
  stages {
    stage('wait0') {
      steps {
        waitForBuild(runId: '123', propagate: true)
      }
    }

    stage('wait') {
      parallel {
        stage('wait1') {
          steps {
            sleep 15
          }
        }

        stage('wait2') {
          steps {
            sleep 15
          }
        }

      }
    }

    stage('wait3') {
      steps {
        sleep 5
      }
    }

    stage('print') {
      steps {
        echo 'message_print'
      }
    }

  }
}