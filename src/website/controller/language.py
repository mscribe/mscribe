from typing import List

from website.data import LanguageData


class LanguageController:
    @staticmethod
    def get_languages() -> List[str]:
        languages = []
        for language in LanguageData.get_languages():
            languages.append(language.language_code)
        return languages
