file_name = ""
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
columns = next(list_line)
company_dicts = (dict(zip(columns, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)

print(f"Total series A fundraising ${total_series_a}")