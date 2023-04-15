from fastapi import FastAPI, status, HTTPException
import subprocess
from pydantic import BaseModel
import os
from typing import (Optional)
import json
import time

# Get environment varialbes
ENVARGS = json.loads(os.getenv('ARGS')) if os.getenv('ARGS') else ["date"]


class FuncReqData(BaseModel):
    args: list

app = FastAPI()


def runprocess(args,
               reqtxt=""):
    pipline = subprocess.run(args, 
                             capture_output=True, 
                             text=True,
                             timeout=30)
    
    if pipline.returncode != 0:
        return "Error", pipline.returncode, pipline.stderr
    else:
        return "OK", pipline.returncode, pipline.stdout


@app.post("/")
@app.get("/")
async def root(req:FuncReqData|None=None):
    if req == None:
        req = FuncReqData(args=ENVARGS)

    try:
        start = time.time()
        returnmsg, returncode, responsetxt = runprocess(req.args)
        end = time.time()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='No Args'
        )

    return {"args": req.args, 
            "returnmsg": returnmsg,
            "returncode": returncode,
            "responsetxt": responsetxt,
            "elapsedtimeinsecond": end - start}


@app.post('/helloworld')
async def hello():
    return "helloworld"
