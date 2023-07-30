import json

def get_payload_auth():
    f = open("")
    data = json.loads(file_data)
    file_data.close()
    return data