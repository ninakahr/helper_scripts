from typing import List, Optional, Union

from typing_extensions import Literal

class PAPath:
    def __init__(self, path: str) -> None: ...
    def __repr__(self) -> str: ...
    def contents(self) -> Union[dict, str]: ...
    def delete(self) -> None: ...
    def upload(self, content: bytes) -> None: ...
