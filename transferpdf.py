import requests
import json
import time

print("please input you app_id, app_key and filename(of the pdf file in the same folder with the program;such as 'main.pdf'):\n")
print("app_id:")
app_id=input()
print("\napp_key:")
app_key=input()
print("\nfilename:")
filename=input()

options = {
    "conversion_formats": {"tex.zip": True},
    "math_inline_delimiters": ["$", "$"],
    "rm_spaces": True
}
r = requests.post("https://api.mathpix.com/v3/pdf",
    headers={
        "app_id": app_id,
        "app_key": app_key
    },
    data={
        "options_json": json.dumps(options)
    },
    files={
        "file": open("./" + filename,"rb")
    }
)
pdf_id=eval(r.text)['pdf_id']

headers={
    "app_id": app_key,
    "app_key": app_key,
    "Content-type": "application/json"
}

while(1):
    url = "https://api.mathpix.com/v3/pdf/" + pdf_id
    response = requests.get(url, headers=headers)
    response=eval(response.text)['status']
    print(response)
    if(response=="completed"):
        break
    time.sleep(2)

while(1):
    url = "https://api.mathpix.com/v3/converter/" + pdf_id
    response = requests.get(url, headers=headers)
    response=eval(response.text)["conversion_status"]["tex.zip"]['status']
    print(response)
    if(response=="completed"):
        break
    time.sleep(2)


# get LaTeX zip file
url = "https://api.mathpix.com/v3/pdf/" + pdf_id + ".tex"
response = requests.get(url, headers=headers)
with open(pdf_id + ".tex.zip", "wb") as f:
    f.write(response.content)