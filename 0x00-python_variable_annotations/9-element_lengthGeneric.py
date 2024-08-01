#!/usr/bin/env python3
"""Type-annotated function element_length"""

from typing import List, Tuple, Sequence

def element_length(lst: Sequence[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]

# Example usage
print(element_length(["apple", "banana", "cherry"]))  # Output: [('apple', 5), ('banana', 6), ('cherry', 6)]

