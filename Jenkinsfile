pipeline {
    agent {
        label 'ubuntu'
        }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/Amittyagivats/selenium_pytest_automation_framework.git']]])
                    }
                }
            }

        stage('Debug') {
            steps {
                // Set up any dependencies, virtual environment, etc.
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run pytest for Selenium tests
                script {
                    sh 'chmod +x run_smoke_suite.sh'
                    sh './run_smoke_suite.sh'
                }
            }
        }
    }

    post {
        always {
            // Clean up or perform any post-build actions here
            script {
                sh 'deactivate'
            }
        }
    }
}

