#!/usr/bin/python3
#7-to_kv.py
from typing import Tuple, Union

def to_kv(k: str, v: Union[int , float]) -> Tuple[str, float]:
    return (k, v** 2)

