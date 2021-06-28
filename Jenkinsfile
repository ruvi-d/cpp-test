pipeline {
	agent { docker { image 'gcc:latest' } }
	stages {
		stage('Build') {
			steps {
				cmakeBuild buildDir: 'build', buildType: 'Release', generator: 'Unix Makefiles', installation: 'InSearchPath', sourceDir: '.'
			}
		}
	}
}
