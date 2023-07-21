# from typing import Dict

# import aiohttp
# import requests

# from martian import openai


# def get_api_key() -> str:
#     if openai.api_key_path:
#         with open(openai.api_key_path, "rt") as k:
#             api_key = k.read().strip()
#             if not api_key.startswith("sk-"):
#                 raise ValueError(f"Malformed API key in {openai.api_key_path}.")
#             return api_key
#     elif openai.api_key is not None:
#         return openai.api_key
#     else:
#         raise Exception(
#             "No API key provided. You can set your API key in code using 'openai.api_key = <API-KEY>', or you can set the environment variable OPENAI_API_KEY=<API-KEY>). If your API key is stored in a file, you can point the openai module at it with 'openai.api_key_path = <PATH>'. You can generate API keys in the OpenAI web interface. See https://platform.openai.com/account/api-keys for details."
#         )
