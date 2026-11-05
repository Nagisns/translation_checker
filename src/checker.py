# Copyright (c) 2026 Nagi(Nagisns)
# Licensed under the MIT License.
# See the LICENSE file for details.

import logging
import ast
from typing import Optional
from ast import Module

def check_translations(source: Optional[str]) -> None:
    if source is None:
        logging.warning("Source code is not set.")
        return

    tree: Module = ast.parse(source)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        if isinstance(node.func, ast.Name) and node.func.id == "translate":
            print(f"Line {node.lineno}: translate detected.")
