from .card_evaluater import CardEvaluator


def has_attr(**kwargs) -> CardEvaluator:
    """
    p = has_attr(ex=ExtensionName('Sample'), cost=Cost(3))
    means -> if card c is from ex 'Sample' AND costs just 3, p(c) returns True.

    p = has_attr(cost=Cost(2)) | has_attr(cost=Cost(3))
    means -> if card c costs just 2 OR 3, p(c) returns True.
    """
    if not kwargs:
        return CardEvaluator(lambda _: True)

    (attr, value), *kvs = kwargs.items()

    #
    def _inner(card: 'Card') -> bool:
        return getattr(card, attr) == value

    return CardEvaluator(_inner) & has_attr(**dict(kvs))
