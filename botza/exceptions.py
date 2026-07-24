class TelegramError(Exception):
    def __init__(self, payload):
        self.error_code = payload.get("error_code")
        self.description = payload.get("description")
        super().__init__(self.description)
