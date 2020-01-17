from pathlib import Path
from typing import List


class Virtualenv:
    domain: str = ...
    python_version: str = ...
    path: Path = ...
    def __init__(self, domain: str, python_version: str) -> None: ...
    def __eq__(self, other: Virtualenv) -> bool: ...
    def create(self, nuke: bool) -> None: ...
    def pip_install(self, packages: List[str]) -> None: ...
