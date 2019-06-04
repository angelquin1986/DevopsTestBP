//author aquingaluisa copia del file  pipeline_venv_workarounds.groovy en github

node {
    stage 'Checkout and Build'

    createVirtualEnv 'env'
    executeIn 'env', 'pip install -r requirements.txt'
    executeIn 'env', './manage.py test'
    //executeIn 'env', './manage.py integration-test'

    virtualEnv('true')
    runCmd('pip install -r requirements.txt')

}

// crear del ambiente virtual  con python 3
def createVirtualEnv(String name) {
    sh "virtualenv -p python3 ${name}"
}

//encargado de ejecutar los escripts en el env
def executeIn(String environment, String script) {
    sh ". ${environment}/bin/activate && " + script
}

// alternative workaround
env.VENV_PATH = "${JENKINS_HOME}/.virtualenv/${JOB_NAME}/venv"

def virtualEnv(String rebuild){
    withEnv(["PATH+VEX=~/.local/bin"]){
        if(rebuild == "true") {
            sh "rm -rf ${env.VENV_PATH}"
            sh "echo 'rebuild is true'"
        }
        sh returnStatus: true, script: "virtualenv ${env.VENV_PATH}"
    }
}

def runCmd(String pyCmd){
    withEnv(["PATH+VEX=~/.local/bin"]){
        sh returnStatus: true, script: "vex --path=${env.VENV_PATH} ${pyCmd}"
    }
}