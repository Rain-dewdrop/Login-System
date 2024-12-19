import wmi
def get_hwid():
     # 创建 WMI 客户端
    c = wmi.WMI()
    # 查询主板信息
    for board in c.Win32_BaseBoard():
        # 返回主板的序列号

        return board.SerialNumber
    return