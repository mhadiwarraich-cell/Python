student_data = {
    "idl1": {"name": "Hadi", "class": "V", "subject_integration": "english, math, reading"},
    "idl2": {"name": "Tony", "class": "V", "subject_integration": "english, math, reading"},
    "idl3": {"name": "Ahmad", "class": "V", "subject_integration": "english, math, reading"},

     "idl4": {"name": "Ahmad", "class": "V", "subject_integration": "english, math, reading"},
}

result= {}
seen_keys = [] 

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
        
    
for k, v in result.items():
    print(k, ":", v)