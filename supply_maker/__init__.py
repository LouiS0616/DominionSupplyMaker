import logging as logging_
from . import top


# noinspection SpellCheckingInspection
def get_file_logger(
        name, *, level=logging_.DEBUG,
        form='%(asctime)s|%(name)-30s|%(levelname)-5s|%(message)s'):

    assert '/' not in name

    logger = logging_.getLogger(name)
    logger.setLevel(level)

    handler = logging_.FileHandler(
        top.where / f'out/log/{name}.log', encoding='utf-8', mode='w'
    )
    handler.setFormatter(logging_.Formatter(form))
    logger.addHandler(handler)

    return logger

