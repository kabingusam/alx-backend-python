#!/usr/bin/python3
# 9-element_length.py
from typing import List, Tuple, Any

def element_length(lst: list)-> List[Tuple[Any, int]]:
    return [(i, len(i)) for i in lst]
