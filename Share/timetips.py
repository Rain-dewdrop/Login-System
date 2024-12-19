import arrow
def timetips(message):

    print(f"[{arrow.now().format('HH:mm:ss')}] {message}")

    return