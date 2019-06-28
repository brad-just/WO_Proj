import json

data = [{"Item ID": "111-111", "Work Order": 123456, "Sales Order": 654321, "Quantity": 5,
                "Short Description": "Undermount", "Long Description": "...", "Start Date": "6/24/19",
                "End Date": "7/1/19"},
        {"Item ID": "452-475", "Work Order": 417919, "Sales Order": 950918, "Quantity": 3,
                "Short Description": "Drop-In", "Long Description": "...", "Start Date": "6/24/19",
                "End Date": "6/29/19"},
        {"Item ID": "301-256", "Work Order": 697449, "Sales Order": 950918, "Quantity": 2,
                "Short Description": "Undermount", "Long Description": "...", "Start Date": "6/25/19",
                "End Date": "7/2/19"},
        {"Item ID": "476-414", "Work Order": 681263, "Sales Order": 950918, "Quantity": 4,
                "Short Description": "Drop-In", "Long Description": "...", "Start Date": "6/25/19",
                "End Date": "7/1/19"},
        {"Item ID": "244-463", "Work Order": 324065, "Sales Order": 95018, "Quantity": 1,
                "Short Description": "Drop-In", "Long Description": "...", "Start Date": "6/26/19",
                "End Date": "7/5/19"},
        {"Item ID": "476-414", "Work Order": 681263, "Sales Order": 950918, "Quantity": 4,
                "Short Description": "Drop-In", "Long Description": "...", "Start Date": "6/25/19",
                "End Date": "7/1/19"},
                ]

with open("jsondump.json", "w") as write_file:
    json.dump(data, write_file)
