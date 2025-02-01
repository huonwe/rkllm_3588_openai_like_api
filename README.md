# 介绍
兼容OpenAI API格式的rkllm server代码

# 使用
添加需要用到的动态库:
```bash
sudo cp lib/*.so /usr/lib
```
安装uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
安装python依赖:
```bash
uv sync
```
运行:
```bash
uv run server.py
```
- 默认情况下，参数为rk3588，模型路径为models/deepseek-r1-1.5b-w8a8.rkllm
- 你可以手动指定参数，如uv run server.py --rkllm_model_path=path/to/model.rkllm ----target_platform=rk3576

你可以用client.py测试:
```bash
uv run client.py
```

# 模型
这里有deepseek-r1的1.5b蒸馏版的rkllm模型，如果需要可自行[下载](https://drive.google.com/drive/folders/1I4XHZeNcDQgm1A2BTzatmUWdNHIQSsMJ?usp=drive_link)