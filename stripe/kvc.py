def kyc_verify_p1(records_str):
    # 解析 CSV 字符串
    lines = records_str.strip().split('\n')
    headers = lines[0].split(',')
    
    records = []
    for line in lines[1:]:
        values = line.split(',')
        record = {headers[i]: values[i] for i in range(len(headers))}
        records.append(record)
    
    req = [
        "business_name",
        "business_profile_name",
        "full_statement_descriptor",
        "short_statement_descriptor",
        "url",
        "product_description",
    ]

    # part 3: blocklist
    # 用 set（查找快 O(1)）
    blocklist = {
        "ONLINE STORE",
        "ECOMMERCE",
        "RETAIL",
        "SHOP",
        "GENERAL MERCHANDISE",
    }
    res = []
    for rec in records:
        name = rec.get("business_name", "").strip()
        ok = True # 默认通过
        # 检查所有字段
        for field in req:
            value = rec.get(field, "") # 获取值（不存在返回""）
            if value is None or str(value).strip() == "": # 空或只有空格
                ok = False
                break
        # Part 2: check length
        if ok:
            # full statement descriptors 
            fsd = str(rec.get("full_statement_descriptor", "")).strip()
            if not (5 <= len(fsd) <= 31):
                ok = False
            # Part 3
            if ok and fsd.upper() in blocklist:
                ok = False
        res.append(f"{'VERIFIED' if ok else 'NOT VERIFIED'}: {name}")
    return res

# Test
if __name__ == "__main__":
    part1_input = """business_name,business_profile_name,full_statement_descriptor,short_statement_descriptor,url,product_description
Pawsome Pets Inc.,Pawsome Pets,PAWSOME PETS,PAWSOME,https://pawsome.example,Pet accessories
Bean Bliss Coffee Company,Bean Bliss,  ,BEAN,https://beanbliss.example,Coffee & snacks"""
    
    print("=== Part 1 ===")
    for line in kyc_verify_p1(part1_input):
        print(line)

    # VERIFIED: Pawsome Pets Inc.
    # NOT VERIFIED: Bean Bliss Coffee Company

    part2_input = """business_name,business_profile_name,full_statement_descriptor,short_statement_descriptor,url,product_description
Oakridge Furniture Crafters LLC,Oakridge Furniture,OAKRIDGE CUSTOM WOODWORKING AND FURNITURE EMPORIUM,OAK,https://oakridge.example,Custom furniture
Information Technology Consulting Solutions Inc.,ITCS,ITCS,ITCS,https://itcs.example,Consulting
Om Yoga and Wellness Center,Om Yoga,OM YOGA,OM,https://omyoga.example,Yoga studio"""
    
    print("\n=== Part 2 ===")
    for line in kyc_verify_p1(part2_input):
        print(line)
    # NOT VERIFIED: Oakridge Furniture Crafters LLC
    # NOT VERIFIED: Information Technology Consulting Solutions Inc.
    # VERIFIED: Om Yoga and Wellness Center

    part3_input = """business_name,business_profile_name,full_statement_descriptor,short_statement_descriptor,url,product_description
Pawsome Pets Inc.,Pawsome Pets,PAWSOME PETS,PAWSOME,https://pawsome.example,Pet accessories
Bean Bliss Coffee Company,Bean Bliss,  ,BEAN,https://beanbliss.example,Coffee & snacks
Oakridge Furniture Crafters LLC,Oakridge Furniture,OAKRIDGE CUSTOM WOODWORKING AND FURNITURE EMPORIUM,OAK,https://oakridge.example,Custom furniture
Om Yoga and Wellness Center,Om Yoga,OM YOGA,OM,https://omyoga.example,Yoga studio
Information Technology Consulting Solutions Inc.,ITCS,ITCS,ITCS,https://itcs.example,Consulting
Global Goods Marketplace Inc.,Global Goods,Retail,GG,https://globalgoods.example,Marketplace
Evergreen Digital Strategies LLC,Evergreen Digital,EVERGREEN DIGITAL,EG,https://evergreen.example,Digital consulting
Sweet Dreams Creamery LLC,Sweet Dreams,SWEET DREAMS,SD,https://sweetdreams.example,Ice cream shop
Global Financial Advisory Services Inc.,GFAS,Online Store,GFAS,https://gfas.example,Advisory
Northwest Innovation Technologies Corporation,Northwest Innovation,GENERAL MERCHANDISE,NWIT,https://nwit.example,Tech solutions"""
    
    print("\n=== Part 3 ===")
    for line in kyc_verify_p1(part3_input):
        print(line)

    # VERIFIED: Pawsome Pets Inc.
    # NOT VERIFIED: Bean Bliss Coffee Company
    # NOT VERIFIED: Oakridge Furniture Crafters LLC
    # VERIFIED: Om Yoga and Wellness Center
    # NOT VERIFIED: Information Technology Consulting Solutions Inc.
    # NOT VERIFIED: Global Goods Marketplace Inc.
    # VERIFIED: Evergreen Digital Strategies LLC
    # VERIFIED: Sweet Dreams Creamery LLC
    # NOT VERIFIED: Global Financial Advisory Services Inc.
    # NOT VERIFIED: Northwest Innovation Technologies Corporation