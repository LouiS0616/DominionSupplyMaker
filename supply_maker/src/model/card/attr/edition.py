class Edition:
    _editions_available = ['1st', '2nd', ]

    def __init__(self, raw: str):
        assert raw in {*self.editions_available, '***', }

        if raw == '***':
            self._editions = self.editions_available
        else:
            self._editions = {raw}

    def included_at(self, edition: int) -> bool:
        return self.editions_available[edition-1] in self._editions

    @property
    def is_newest(self) -> bool:
        return self.editions_available[-1] in self._editions

    @property
    def editions_available(self) -> list:
        return self._editions_available.copy()

    def __str__(self):
        return '/'.join(self._editions)
