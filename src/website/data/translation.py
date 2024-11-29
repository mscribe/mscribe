from website.schema import Language
from website.schema import Translation


class TranslationData:
    @staticmethod
    def get_translation(language: str, key: str) -> Translation:
        return Translation.query\
            .join(Language, Language.id == Translation.language_id)\
            .with_entities(Translation.key, Translation.value)\
            .filter(Language.language_code == language)\
            .filter(Translation.key == key)\
            .filter(Language.id == Translation.language_id)\
            .first()
