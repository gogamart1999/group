import json
import yaml
def read_json():
    try:
        with open("tas_urls.json") as f:
            file_1 = f.read()
            json_data = json.loads(file_1)
        
        with open('new.yaml','w') as file:
            yaml.dump(json_data, file)
    except FileNotFoundError:
        print("File does not exist.")
    except json.decoder.JSONDecodeError:
        print("This was a problem accessing the equipment data.")
    else:
        print("Successfully done")

     
read_json()
