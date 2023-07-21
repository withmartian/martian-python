# Martian Python Library

## Installation

You can install this package by running

```bash
pip install martian-python
```

## Usage

See the Martian API documentation at [docs.withmartian.com](https://docs.withmartian.com).

### Example

```python
from martian import openai

openai.martian_api_key = ...

chat_completion = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)

print(chat_completion.choices[0].message.content)
```
