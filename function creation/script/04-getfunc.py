import os
import json
import subprocess

if __name__ == "__main__":
    TEMPNAME = "$demo$"
    SCRIPTDIR = os.path.dirname(__file__)
    with open(os.path.join(SCRIPTDIR, "00-config.json"), "r") as f:
        CONFIG = json.load(f)
        FunctionName = CONFIG.get('FunctionName')
        ExecutionArgs = CONFIG.get('ExecutionArgs')

    TEMPLATEDIR = os.path.join(SCRIPTDIR, "template")
    FUNCDIR = os.path.join(SCRIPTDIR, FunctionName)

    subprocess.call(['kubectl', 'get', 'deployment', '-n', 'function'])
