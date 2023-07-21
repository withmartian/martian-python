import martian
from martian import openai


def default_api_key() -> str:
    api_key_path = martian.api_key_path or openai.martian_api_key_path
    if api_key_path:
        with open(api_key_path, "rt") as k:
            api_key = k.read().strip()
            if not api_key.startswith("sk-"):
                raise ValueError(f"Malformed Martian API key in {api_key_path}.")
            return api_key
    res = martian.api_key or openai.martian_api_key
    if res is None:
        raise ValueError("No Martian API key found.")
    return res
