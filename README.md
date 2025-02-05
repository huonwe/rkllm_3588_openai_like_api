# rkllm openai like api server
[English](https://github.com/huonwe/rkllm_openai_like_api/blob/main/README.en.md)

## 介绍
兼容OpenAI API格式的rkllm server代码

## 使用
```bash
git clone https://github.com/huonwe/rkllm_openai_like_api.git
cd rkllm_openai_like_api
```
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
- 默认情况下，平台设置为rk3588，模型路径为models/deepseek-r1-1.5b-w8a8.rkllm，监听端口为8080
- 你可以手动指定参数，如`uv run server.py --rkllm_model_path=path/to/model.rkllm --target_platform=rk3588 --port=8080`

之后，你可以通过`http://your.ip:8080/rkllm_chat/v1`来连接到本服务。由于只实现了`/v1/chat/completions`, 所以并不是所有功能都可以正常使用。

你可以用client.py测试:
```bash
uv run client.py
```

## 注意事项
不要使用rkllm本地运行的模型来进行自动生成标题、标签等任务。在进行此类任务时，用户将无法与模型聊天，因为受限于性能，同一时刻server只会处理一条对话。若当前存在对话未处理完成，则不会接受任何其他对话。

## 更新记录
- [x] 实现了/v1/models，现在无需手动添加模型ID。 --20250205

## 模型
这里有deepseek-r1的1.5b蒸馏版的rkllm模型，如果需要可自行[下载](https://drive.google.com/drive/folders/1I4XHZeNcDQgm1A2BTzatmUWdNHIQSsMJ?usp=sharing)