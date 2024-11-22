from uuid import uuid4


class uuid():
    @staticmethod
    def uuid() -> str:
        return str(uuid4()).replace("-", "")
