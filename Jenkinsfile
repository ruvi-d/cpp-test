pipeline {
	agent any
	stages {
		stage('Build') {
			steps {
				sh 'g++ src/main.cpp -o build/hello'
				archiveArtifacts artifacts: 'build/hello', fingerprint: true
			}
		}
		stage('Test') {
			steps {
				sh 'build/hello'
			}
		}
	}
}
