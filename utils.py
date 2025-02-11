import re

def apply_chat_template(messages):
    """
    该格式只针对deepseek-r1-distill-qwen-1.5b进行过测试.
    如果使用的是其它模型，请自行修改此处逻辑.

    You will need to modify this function if you use some other models except deepseek-r1-distill-qwen-1.5b.
    """
    begin_of_sentence = "<｜begin▁of▁sentence｜>"
    end_of_sentence = "<｜end▁of▁sentence｜>"
    user_position = "<｜User｜>"
    assistant_position = "<｜Assistant｜>"
    think_content = re.compile('<think>.*</think>')

    sentence = ""
    sentence += begin_of_sentence
    for msg in messages:
        if msg['role'] == 'system':
            sentence += msg['content']
        if msg['role'] == 'user':
            sentence += user_position
            sentence += msg['content']
        if msg['role'] == "assistant":
            sentence += assistant_position
            sentence += msg['content']
            sentence += end_of_sentence

        # 送给模型的对话记录中删除think标签内的内容
        sentence = think_content.sub('', sentence)
    return sentence