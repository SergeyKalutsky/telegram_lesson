from telebot import TeleBot
from apis import ask_chat_gpt
from text_to_speech import text_to_speech, speech_to_text

bot = TeleBot('5725792179:AAHIAlFVHfb5cBfCs6IIvwAwAlyJnQlhlfw')


@bot.message_handler(commands=['GPT'])
def duck(message):
    bot.send_message(message.chat.id, text='Подождите, генерирую ответ...')
    answer = ask_chat_gpt(message.text[4:])
    bot.send_message(message.chat.id, text=answer)


@bot.message_handler(commands=['speech'])
def duck(message):
    text = ' '.join(message.text.split(' ')[1:])
    text_to_speech(text)
    with open('text_to_speech.mp3', 'rb') as f:
        bot.send_audio(message.chat.id, f)


@bot.message_handler(content_types=['voice'])
def duck(message):
    file = bot.get_file(message.voice.file_id)
    bytes = bot.download_file(file.file_path)
    with open('voice.ogg', 'wb') as f:
        f.write(bytes)
    text = speech_to_text()
    bot.send_message(message.chat.id, text=text)


if __name__ == '__main__':
    bot.polling(non_stop=True)
