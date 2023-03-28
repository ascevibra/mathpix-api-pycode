import requests
import json

options = {
    "conversion_formats": {"tex.zip": True},
    "math_inline_delimiters": ["$", "$"],
    "rm_spaces": True
}
r = requests.post("https://api.mathpix.com/v3/pdf",
    headers={
        "app_id": "app_id",
        "app_key": "app_key"
    },
    data={
        "options_json": json.dumps(options)
    },
    files={
        "file": open("/path/to/you/pdf/file","rb")
    }
)
print(r.text.encode("utf8"))