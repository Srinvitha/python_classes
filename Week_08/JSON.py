# JSON = "JavaScript Object Notation"

import json

x = '{"Name":"John", "Age":24, "City": "New York"}'
print(type(x))

y = json.loads(x)
print(type(y))        # The result is a Python Dictionary...

print(y["Age"])


# json to dict ???

