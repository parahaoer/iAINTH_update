import json
from elasticsearch import Elasticsearch

es = Elasticsearch('10.25.23.161:9200')

doc ={
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\msdt.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\installutil.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\regsvcs.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\regasm.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\msbuild.exe*"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "*\\\\ieexec.exe*"
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
tactic = "Execution"
technique = "Trusted Developer Utilities"
procedure = "MSBuild Bypass Using Inline Tasks"
tech_code = "T1127"

action ={
            "Tactic": tactic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "EventCount": count,
        }

es.index(index="represent_5",body = action, id = 92)

json_str = json.dumps(doc)
with open("dst_procedures/MSBuild Bypass Using Inline Tasks.py", "w", encoding="gbk") as f:
	f.write(json_str+"\n")
	f.write('tactic = "Execution"\n')
	f.write('technique = "Trusted Developer Utilities"\n')
	f.write('procedure = "MSBuild Bypass Using Inline Tasks"\n')
	f.write('tech_code = "T1127"\n')
