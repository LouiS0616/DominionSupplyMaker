from ....translation import RawName


class CardName(RawName):
    def _t(self, lang):
        raise NotImplementedError
