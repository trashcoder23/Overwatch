import json
import re

def extract_json(text):

    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)

        if match:
            return json.loads(match.group())

    except Exception:
        pass

    return None