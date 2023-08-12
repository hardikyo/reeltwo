import telebot
import pytube

BOT_TOKEN = '6492183468:AAHid4rh3QL8Bbc-JMoR65v2rqY8_315bCI'

def download_reel(reel_url):
    reel = pytube.YouTube(reel_url)
    video = reel.streams.get_highest_resolution()
    video.download('reel.mp4')

    return 'reel.mp4'

def download_reel_command(message):
    reel_url = message.text[8:]
    video_file = download_reel(reel_url)

    bot.send_message(message.chat.id, 'Video downloaded successfully!')
    bot.send_document(message.chat.id, video_file)

def handle_message(message):
    if message.text.startswith('/start'):
        bot.send_message(message.chat.id, 'Welcome to the reel download bot!')
        bot.send_message(message.chat.id, 'To download a reel, send me a message with the following format: /download https://www.instagram.com/reel/<reel_id>/')
    else:
        if message.text.startswith('/download'):
            reel_url = message.text[8:]
            video_file = download_reel(reel_url)

            bot.send_message(message.chat.id, 'Video downloaded successfully!')
            bot.send_document(message.chat.id, video_file)
        else:
            bot.send_message(message.chat.id, 'I don\'t understand what you mean.')

bot = telebot.TeleBot(BOT_TOKEN)

while True:
    bot.polling()
