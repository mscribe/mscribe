from website.schema import Translation


class TranslationData:
    @staticmethod
    def get_translation(key: str) -> Translation:
        return Translation.query.filter_by(key=key).first()
