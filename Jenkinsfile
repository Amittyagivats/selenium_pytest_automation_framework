pipeline {
    agent {
        label 'Linux (amd64)'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from GitHub
                git 'https://github.com/Amittyagivats/selenium_pytest_automation_framework.git'
            }
        }

        stage('Setup') {
            steps {
                // Set up any dependencies, virtual environment, etc.
                script {
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run pytest for Selenium tests
                script {
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

