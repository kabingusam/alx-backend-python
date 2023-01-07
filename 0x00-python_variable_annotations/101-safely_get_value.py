#!/usr/bin/python3
# 101-safely_get_value.py
from typing import TypeVar, Dict, Union

K = TypeVar('K')
V = TypeVar('V')

def safely_get_value(dct: Dict[K, V], key: K, default: V = None) -> Union[V, None]:
    if key in dct:
        return dct[key]
    else:
        return default
