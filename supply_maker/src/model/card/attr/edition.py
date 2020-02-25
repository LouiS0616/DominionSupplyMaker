class _EditionMeta(type):
    _editions_available = ['1st', '2nd', ]

    @property
    def editions_available(cls):
        return cls._editions_available

    @property
    def newest_edition(cls):
        return cls.editions_available[-1]


class Edition(metaclass=_EditionMeta):
    def __init__(self, raw: str):
        cls = type(self)
        assert raw in {*cls.editions_available, '***', }

        if raw == '***':
            self._editions = cls.editions_available
        else:
            self._editions = {raw}

    def included_at(self, edition: str) -> bool:
        return edition in self._editions

    def is_newest(self) -> bool:
        cls = type(self)
        return cls.newest_edition in self._editions

    def __str__(self):
        return '/'.join(self._editions)
