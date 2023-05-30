import datetime

now = datetime.datetime.now().strftime("%H:%M:%S")


async def send(message, prefix=""):
    print(f"{prefix}[INFO] - {now} - " + message)
