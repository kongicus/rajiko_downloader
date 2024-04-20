from typing import TypedDict, Callable, List


class ConfigDict(TypedDict, total=False):
    url_template: str
    renamer: Callable[[str], str]
    src_dir: str
    dst_dir: str
    radiko_extension_path: str
    mouse_positions: dict[str, List[int]]
