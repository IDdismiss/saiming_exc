import hashlib


def demo():
    data = "123456"
    # 创建一个MD5的哈希对象
    md5 = hashlib.md5()
    # 更新MD5对象
    md5.update(data.encode("utf-8"))
    new_data = md5.hexdigest()

    print(data)
    print(new_data)


if __name__ == "__main__":
    demo()
