# helper fuc: csv string -> list of dict
def _parse_csv_(csv_str):
    lines = csv_str.strip().split('\n')
    headers = lines[0].split(',')
    
    records = []
    for line in lines[1:]:
        line = line.strip()
        if line:  # 跳过空行
            values = line.split(',')
            record = {headers[i]: values[i] for i in range(len(headers))}
            records.append(record)
    return records

def kvc_par1(records_str):
    records = _parse_csv_(records_str)
    
    req = [
        "business_name",
        "business_profile_name",
        "full_statement_descriptor",
        "short_statement_descriptor",
        "url",
        "product_description",
    ]
    res = []
    for rec in records:
        name = rec.get("business_name","")
        ok = True
        for f in req:
            v = rec.get(f,"")
            if v is None or v.strip() == "":
                ok = False
                break
        res.append(f"{'VERIFIED' if ok else 'NOT VERIFIED'}: {name}")
    return res
        
    
if __name__ == "__main__":
    part1_input = """business_name,business_profile_name,full_statement_descriptor,short_statement_descriptor,url,product_description
    Pawsome Pets Inc.,Pawsome Pets,PAWSOME PETS,PAWSOME,https://pawsome.example,Pet accessories
    Bean Bliss Coffee Company,Bean Bliss,  ,BEAN,https://beanbliss.example,Coffee & snacks"""
    
    for line in kvc_par1(part1_input):
        print(line)