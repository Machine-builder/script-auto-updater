import urllib.request
import json

def downloadGitFile(filename, repo = "https://raw.githubusercontent.com/Machine-builder/script-auto-updater/master/"):
    response = urllib.request.urlopen(str(repo)+str(filename))
    html = response.read().decode()
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
