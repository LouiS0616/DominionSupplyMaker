import logging as logging_
import pathlib

_where = pathlib.Path(__file__).parent.resolve()


# noinspection SpellCheckingInspection
def get_file_logger(
        name, *, level=logging_.DEBUG,
        form='%(asctime)s|%(name)-30s|%(levelname)-5s|%(message)s'):

    logger = logging_.getLogger(name)
    logger.setLevel(level)

    log_dir = pathlib.Path('./dsm_out/log')
    log_dir.mkdir(parents=True, exist_ok=True)

    handler = logging_.FileHandler(
        log_dir / f'{name.split(".")[-1]}.log', encoding='utf-8', mode='w'
    )
    handler.setFormatter(logging_.Formatter(form))
    logger.addHandler(handler)

    return logger


def where():
    return _where
