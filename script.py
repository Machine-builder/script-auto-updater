import urllib.request
import json, shutil

PYTHONEXTENSION = ".py3"

def downloadGitFile(filename, repo = "https://raw.githubusercontent.com/Machine-builder/script-auto-updater/master/"):
    response = urllib.request.urlopen(str(repo)+str(filename))
    html = response.read().decode()

    if filename.endswith(".py"):
        filename = filename.replace(".py", PYTHONEXTENSION, 1)

    open("downloads\\"+filename,"w").write(html)

downloadGitFile("data.json")

newver = (json.loads(open("downloads\\data.json","r").read()))["VERSION"]
curver = (json.loads(open("downloads\\curver.json","r").read()))["VERSION"]

print("The current version is %s" % curver)
print("The newest version is %s" % newver)

if not newver > curver:
    print("We're up to date!")

else:
    print("There's an update we need")
    input("press enter to download the update ...")
    downloadGitFile("script.py")
    LOCATION = "downloads\\%s" % ( "script.py".replace(".py",PYTHONEXTENSION))
    DESTINATION = "script.py".replace(".py",PYTHONEXTENSION)
    shutil.move( LOCATION , DESTINATION )
    print("'RunMe' has been updated!")
    open("downloads\\curver.json","w").write(json.dumps({"VERSION":newver}))
