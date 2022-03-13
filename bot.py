import config
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


def hello(update: Update, context):
    message = update.effective_message.text
    CL = {'а': 'a', 'ә': 'ä', 'б': 'b', 'в': 'v', 'г': 'g', 'ғ': 'ğ', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'қ': 'q', 'л': 'l',
      'м': 'm', 'н': 'n', 'ң': 'ŋ', 'о': 'o', 'ө': 'ö', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ұ': 'ū', 'ү': 'ü', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch',
      'h': 'h', 'ш': 'ş', 'щ': 'ş', 'ъ': '', 'ы': 'y', 'i': 'ı', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia',
      'А': 'A', 'Ә': 'Ä', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ғ': 'Ğ', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Қ': 'Q', 'Л': 'L',
      'М': 'M', 'Н': 'N', 'Ң': 'Ŋ', 'О': 'O', 'Ө': 'Ö', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ұ': 'Ū', 'Ү': 'Ü', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch',
      'Н': 'H', 'Ш': 'Ş', 'Щ': 'Ş', 'Ъ': '', 'Ы': 'Y', 'I': 'I', 'Ь': '', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'}
     
    res = ''
    for i in range(len(message)):
        if CL.get(message[i]) == None:
            res += message[i]
        else:
            res += CL[message[i]]
    message = res


    context.bot.send_message(
        chat_id = update.effective_message.chat_id, 
        text = message
        
    )

def start(update: Update, context):
    user_name = update.effective_user.first_name
    context.bot.send_message(
        chat_id = update.effective_message.chat_id,
        text = f"Salem, {user_name}!"
    )

def main():
    my_update = Updater(
        token = config.TOKEN,
        #base_url = config.PROXY, 
        use_context = True
    )

    my_handler = MessageHandler(Filters.all, hello)
    start_handler = CommandHandler("start", start) 
    
    my_update.dispatcher.add_handler(start_handler)
    my_update.dispatcher.add_handler(my_handler)

    my_update.start_polling()
    my_update.idle()

if __name__ == "__main__":
    main()
