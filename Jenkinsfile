pipeline {
	agent { docker { image 'conanio/gcc10-armv7hf:latest' } }
	stages {		
		stage ('Conan configuration') {
            steps {
                rtConanClient (
                    id: "myConanClient"
                )
            }
        }
		stage('Build') {
			steps {
				sh 'echo "ruvi here"'
				sh 'ls'
				sh 'pwd'
				rtConanRun (
                    clientId: "myConanClient",
                    command: "create . -pr /home/conan/.conan/profiles/default --build missing"
                )
			}
		}
	}
}
