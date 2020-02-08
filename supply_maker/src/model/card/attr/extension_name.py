from ....translation import RawName


class ExtensionName(RawName):
    def _t(self, lang):
        raise NotImplementedError

