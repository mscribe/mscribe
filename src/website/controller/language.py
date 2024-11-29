from typing import List

from website.data import LanguageData
from website.objects.models import LanguageModel


class LanguageController:
    @staticmethod
    def get_languages() -> List[LanguageModel]:
        languages = []

        for language in LanguageData.get_languages():
            languages.append(
                LanguageModel(id=language.id,
                              language_code=language.language_code)
            )

        return languages
