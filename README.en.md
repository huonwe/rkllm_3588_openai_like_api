# Introduction

rkllm server code compatible with the OpenAI API format.

# Usage

```bash
git clone https://github.com/huonwe/rkllm_openai_like_api.git
cd rkllm_openai_like_api
```

Add the required dynamic libraries:

```bash
sudo cp lib/*.so /usr/lib
```

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install Python dependencies:

```bash
uv sync
```

Run:

```bash
uv run server.py
```

- By default, the target platform is rk3588, and the model path is models/deepseek-r1-1.5b-w8a8.rkllm, and the listening port is 8080.
- You can manually specify parameters, such as `uv run server.py --rkllm_model_path=path/to/model.rkllm ----target_platform=rk3576 --port=8080`

Then, you can access this server through `http://your.ip:8080/rkllm_chat/v1`.
Please note that the server only implemented `/v1/chat/completions`, so not all of the functions can work properly

You can use client.py to test:

```bash
uv run client.py
```

# Model

Here is the 1.5b distilled version of the deepseek-r1 rkllm model, you can download it if needed: [download](https://drive.google.com/drive/folders/1I4XHZeNcDQgm1A2BTzatmUWdNHIQSsMJ?usp=sharing)
