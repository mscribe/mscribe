
from website.data import TranslationData
from website.objects.models import TranslationModel


class TranslationController:
    @staticmethod
    def get_translation(key: str) -> TranslationModel:
        translation = TranslationData.get_translation(key=key)
        return TranslationModel(key=key,
                                value=translation.value)
