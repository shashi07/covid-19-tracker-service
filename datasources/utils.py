def success(message):
    return {"success":True, "error":False, "message": message}


def error(message):
    return {"success":False, "error":True, "message": message}
