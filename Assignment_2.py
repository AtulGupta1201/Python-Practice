Indian_state_Capital=[
    {
        "state": "Maharashtra",
        "capital": "Mumbai "
    },
    {
        "state": "Andhra Pradesh",
        "capital": "Amaravati" 
    },
    {
        "state": "Assam",
        "capital": "Dispur"
    },
    {
        "state": "Goa",
        "capital": "Punaji"
    },
    {
        "state": "Bihar",
        "capital": "Patna"
    }
]    
import json

with open("Python\Ds_Assignments\country.json", "w") as outfile:
    json.dump(Indian_state_Capital, outfile)
json_string = json.dumps(Indian_state_Capital)  
print(json_string)
