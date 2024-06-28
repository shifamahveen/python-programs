# dictionary - collection in the form keys and value
          #  - mutable
users = {10: "adam", 30: "Sam"}
lang = {
        "html": "hyper text markup language",
        "css": "cascading style sheets",
        "js": "javascript"
        }
print(type(users))
print(lang['js'])
print(lang.keys())
print(lang.values())
print(lang)

lang['js'] = "java"
print(lang)