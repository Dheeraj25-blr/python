employee = {
    "emp1":{
        "name":"chirag",
        "role":"Instructor",
        "domain":"Cisco"
    },
    "emp2":{
        "name":"Abhijit",
        "role":"Instructor",
        "domain":"Juniper"
    },
    "emp3":{
        "name":"Sagar",
        "role":"Lab Manager",
        "domain":"Vmware"
    }
}

employee.update({"emp4":{"name":"Nithish","role":"Sales Head","Domain":"Sales"}})   
    
#employee["emp1"].update({"domain":"Paloalto"})
#print(employee)
 
employee["emp1"].update({"location":"Delhi"})
print(employee)

employee["emp4"].pop("role")
print(employee)
employee["emp1"].update({"courses":["CCNA","CCNP","Devnet"]})
print(employee)
print(employee["emp3"]["role"])