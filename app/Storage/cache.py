from pathlib import Path

from diskcache import Cache


cache = Cache(str(Path(__file__).resolve().parent / ".cache" / "NextLee"))
