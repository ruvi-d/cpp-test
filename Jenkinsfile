pipeline {
	agent { docker { image 'conanio/gcc10-armv7hf:latest' } }
	environment {
		CONAN_REVISIONS_ENABLED = 1
	}
	stages {		
		stage('Conan Build') {
			steps {
				rtConanClient (
                    id: "myConanClient"
                )
				rtConanRemote (
                    name: "myRemoteName",
                    serverId: "ruvijfrog",
                    repo: "ruvi-conan",
                    clientId: "myConanClient"
                )
				rtConanRun (
                    clientId: "myConanClient",
                    command: "create . -pr ./conan-profiles/arm_gcc_gnueabihf --build missing"
                )			
			}
		}
		stage ('Exec Conan upload and publish') {
			steps {
				rtConanRun (
					clientId: "myConanClient",
					command: "upload mylib* --all -r myRemoteName --confirm"
				)
				rtPublishBuildInfo (
					serverId: "ruvijfrog"
				)
			}
		}
	}
}
