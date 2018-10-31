import re


class Parser:
    def Parse(self, product_code):
        is_match = bool(re.match(r"[\w|\d]+-\d+\(\d+.\d+\)$", product_code))
        if not is_match:
            return None
        rgx = re.compile(r"[\w|\d]+")
        result = rgx.findall(product_code)
        return result[0], result[1], result[2], str(int(result[3])/10)
