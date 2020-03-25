import requests
from requests.auth import HTTPBasicAuth
import json
import csv

url = "https://yourprojectname.atlassian.net/rest/api/2/search?jql=project='<project id>'"

auth = HTTPBasicAuth("<insert your email here>", "<insert the api access token here>")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

finn = (json.loads(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))))

uri = "https://yourprojectname.atlassian.net/browse/"

finn2 = (finn['issues'])
keys = []
creator = ""
reporter = ""
duedate = ""
keyurl = ""

f= open("issuelinks.csv","w+",newline='')
writer = csv.writer(f)
writer.writerow(["Issue URL Link", "Creator", "Reporter", "Due Date(M/DD/YYYY)"])

for i in finn2:
    creator = ((i['fields']['creator']['displayName']))
    reporter = ((i['fields']['reporter']['displayName']))
    duedate = ((i['fields']['duedate']))
    keyurl = (uri+(i['key']))
    writer.writerow([keyurl, creator, reporter, duedate])

f.close()
