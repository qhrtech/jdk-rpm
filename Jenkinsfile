node('medeo-rpm') {
sshagent(['8cc4d453-e66f-40f4-870e-30f31aeb8603']) {

   stage('Checkout Source') {
        checkout scm
    }
    
    stage('Build') {
        sh 'mock --init'
        sh 'make'

        archiveArtifacts artifacts: '*.rpm', excludes: '*.src.rpm', fingerprint: true, onlyIfSuccessful: true
    }
}
}
