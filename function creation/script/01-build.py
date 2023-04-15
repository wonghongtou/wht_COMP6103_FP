import os
import shutil
import json

if __name__=="__main__":
    VARNAME = "$demo$"
    VARARGS = "$ExecutionArgs$"
    VARIMAGE = "$image$"
    SCRIPTDIR = os.path.dirname(__file__)
    with open(os.path.join(SCRIPTDIR, "00-config.json"), "r") as f:
        CONFIG = json.load(f)
        FunctionName = CONFIG.get('FunctionName')
        ExecutionArgs = CONFIG.get('ExecutionArgs')
        Image = CONFIG.get('Image')

    TEMPLATEDIR = os.path.join(SCRIPTDIR, "template")
    FUNCDIR = os.path.join(SCRIPTDIR, FunctionName)

    # COPY from Template Folder
    try:
        shutil.copytree(TEMPLATEDIR, FUNCDIR, dirs_exist_ok=True)
    except:
        print("Delete same name function folder")

    for (root,dirs,files) in os.walk(FUNCDIR, topdown=True):
        for file in files:
            if file.find(".DS_Store") >= 0:
                continue
            TMPFILEPATH = os.path.join(root, file)
            print(TMPFILEPATH)
            with open(TMPFILEPATH, "r",encoding='utf-8') as fin:
                tmp = fin.read().replace(VARNAME, FunctionName)
                tmp = tmp.replace(VARARGS, f"'{json.dumps(ExecutionArgs)}'")
                tmp = tmp.replace(VARIMAGE, Image)
            with open(TMPFILEPATH, "w",encoding='utf-8') as fout:
                fout.write(tmp)