# LCAE gap log

| date | objective | why I missed it | doc link |
|---|---|---|---|
| 2026-10-08 | Build: what makes a function a tool | Picked "only the `@tool` decorator". A tool is defined by the function's **name, docstring and type hints** (they become name, description, input schema). `@tool` is the simplest wrapper, not a requirement: `create_agent` took my plain `get_weather` and it worked. Watch absolute words ("only"). | [Tools: Basic tool definition](https://docs.langchain.com/oss/python/langchain/tools#basic-tool-definition) |
