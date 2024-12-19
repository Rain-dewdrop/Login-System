import hashlib
from timetips import *
def HEX(t):
    if t == "":
        sha256_hash = hashlib.sha256()
        timetips("创建 SHA-256 对象成功！")

        timetips("哈希值计算失败 : 内容空")

    else:
        sha256_hash = hashlib.sha256()
        timetips("创建 SHA-256 对象成功！")

        data = t.encode()
        sha256_hash.update(data)
        hex_digest = sha256_hash.hexdigest()
        timetips("哈希值计算成功！")

        return hex_digest
    
    return