
from website.data import TranslationData


class TranslationController:
    @staticmethod
    def get_translation(language: str, key: str) -> str:
        translation = TranslationData.get_translation(language=language,
                                                      key=key)
        if translation:
            return translation.value
        return ""
