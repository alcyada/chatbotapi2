import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from main.py import bot
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

@bot.on_message(~filters.command("start"))
async def getmessage(client, message):
        text= message.text
        new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')
        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        message.reply(response)
