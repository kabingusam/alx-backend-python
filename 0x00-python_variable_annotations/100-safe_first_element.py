#!/usr/bin/python3
# 100-safe_first_element.py
from typing import List, Any, Tuple

def safe_first_element(lst: List[Any]) -> Tuple[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
