from diskcache import Cache
from pathlib import Path

cache = Cache(str(Path(__file__).resolve().parent / ".cache" / "NextLee"))
