from plyer import notification
from Share.timetips import *
def send_notification(__title5__, __message5__):
    timetips(f"已发送消息 内容:{__message5__}")
    notification.notify(
        title=__title5__,
        message=__message5__,
        app_icon=None,
        timeout=2,
    )
    return