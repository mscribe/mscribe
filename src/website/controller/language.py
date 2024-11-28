from typing import List

from website.model import Language


class LanguageController:
    @staticmethod
    def get_languages() -> List[Language]:
        return Language.query.all()
