pipeline {
	agent any
	stages {
		stage('Build') {
			steps {
				cmakeBuild 
					buildDir: 'build', 
					buildType: 'Release', 
					installation: 'InSearchPath', 
					steps: [
						[args: '-j', withCmake: true]
					]
			}
		}
	}
}
