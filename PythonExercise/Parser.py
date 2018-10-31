import re


class ProductInfo:
    def __init__(self, model_name, date_code, major_version, minor_version):
        self.model_name = model_name
        self.date_code = date_code
        self.major_version = major_version
        self.minor_version = minor_version


class Parser:
    def Parse(self, product_code):
        is_match = bool(re.match(r"[\w|\d]+-\d+\(\d+.\d+\)$", product_code))
        if not is_match:
            return None
        rgx = re.compile(r"[\w|\d]+")
        result = rgx.findall(product_code)
        minor_verison = str(int(result[3])/10)
        return ProductInfo(result[0], result[1], result[2], minor_verison)
