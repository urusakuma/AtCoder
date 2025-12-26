import re
from pathlib import Path
from typing import List

BASE = Path(__file__).resolve().parent
SRC = Path("main.py")
LIB = BASE / "lib"


def resolve_imports(code: str) -> str:
    pattern = r"from lib\.([a-zA-Z0-9_]+) import \*"
    modules = re.findall(pattern, code)
    merged: List[str] = []
    print(modules)
    for m in modules:
        path = LIB / f"{m}.py"
        merged.append(path.read_text())

    # import 文を削除
    code = re.sub(pattern, "", code)

    return "\n".join(merged) + "\n" + code


if __name__ == "__main__":
    code = SRC.read_text()
    merged = resolve_imports(code)
    Path("submit.py").write_text(merged)
    print("submit.py を生成しました")
