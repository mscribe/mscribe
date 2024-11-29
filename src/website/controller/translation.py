
from website.data import TranslationData
from website.objects.models import TranslationModel


class TranslationController:
    @staticmethod
    def get_translation(language: str, key: str) -> TranslationModel:
        translation = TranslationData.get_translation(language=language,
                                                      key=key)
        return TranslationModel(key=translation.key,
                                value=translation.value)
