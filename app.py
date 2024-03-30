import os
import requests
import json

# file_path = "https://drive.google.com/file/d/1u1Z3GZAcDYiqCXVcgHEIKbKw7oPWeXWi/view?usp=sharing"
file_path = "https://drive.google.com/uc?export=download&id=1u1Z3GZAcDYiqCXVcgHEIKbKw7oPWeXWi"
print(file_path)
url = "https://www.youtube.com/watch?v=PNTCM7cbrsc"

r = requests.post('https://api-d7b62b.stack.tryrelevance.com/latest/studios/11ba109b-1844-47fc-860f-35c11f87437b/trigger_limited',
                  headers={"Content-Type": "application/json"},
                  data=json.dumps({"params": {"file_url": f"{file_path}", "options": "Only transcribe", "exclude_interviewee": "Keep all",
                                  "model_options": "Deepgram (Default)", "goal": "Provide a list of high-level analysis.  We automatically extract themes and categories. Note that you need to select **Transcribe and further analysis** under Analysis options above."}, "project": "2b146deafcc1-4db6-bed1-3dbefde8dcd3"})
                  )

response_data = json.loads(r.text)

# Print only the 'result' field
print(response_data)
print(response_data['output']['result'])
