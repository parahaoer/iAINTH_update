import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "wildcard": {
                "process_path.keyword": "*\\\\reg.exe"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*save*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*export*"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*hklm*"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*hkey_local_machine*"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*\\system"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*\\sam"
                    }
                  },
                  {
                    "wildcard": {
                      "process_command_line.keyword": "*\\security"
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    }
  }
}


res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tactic = "Credential Access"
technique = "Credential Dumping"
procedure = "Grabbing Sensitive Hives via Reg Utility"
tech_code = "T1003"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 7)

json_str = json.dumps(doc)
with open("dst_procedures/Grabbing Sensitive Hives via Reg Utility.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Credential Access"\n')
	f.write('technique = "Credential Dumping"\n')
	f.write('procedure = "Grabbing Sensitive Hives via Reg Utility"\n')
	f.write('tech_code = "T1003"\n')
