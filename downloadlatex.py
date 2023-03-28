import requests

pdf_id = "pdf_id"

headers={
    "app_id": "app_key",
    "app_key": "app_key"
    "Content-type': 'application/json"
}

# get LaTeX zip file
url = "https://api.mathpix.com/v3/pdf/" + pdf_id + ".tex"
response = requests.get(url, headers=headers)
with open(pdf_id + ".tex.zip", "wb") as f:
    f.write(response.content)