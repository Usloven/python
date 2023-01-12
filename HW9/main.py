
import logging
import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


print('test')
async def start(update, context):
    # ожидание отправки сообщения по сети - нужен `await`
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="""Доступные команды
                                   /add_pupil - добавление ученика в xls таблицу
                                   /show_pupils  - присылает таблицу в чат
                                   /cancel - выход в главное меню
                                   
                                   
                                   """)

NAME, SURNAME, EXPORT = range(1,4)



async def add_pupil(update, context):
    await update.message.reply_text(
        "Введите имя ученика"
    )
    return NAME


async def name (update, context):
    text = update.message.text
    if len(text.split())<2:
        with open ('pupil.txt', 'a') as f:
            f.writelines('\n'+(text)+ " ")
    else:    
        await update.message.reply_text(
        "запустите программу еще раз- вы ввели больше слов чем нужно"
        )
        return ConversationHandler.END
    await update.message.reply_text(
        "Введите фамилию ученика"
    )
    
    return SURNAME

async def surname (update, context):
    text = update.message.text
    if len(text.split())<2:
        with open ('pupil.txt', 'a') as f:
            f.writelines((text)+ " ")
    else:    
        await update.message.reply_text(
        "запустите программу еще раз- вы ввели больше слов чем нужно"
        )
        return ConversationHandler.END
    
    
    return EXPORT

async def export_excel (update, context):
    with open ('pupil.txt', 'r') as f:
            pupils = f.readlines()
            pupils_list = [i.split() for i in pupils]
            print(pupils_list)
    df= pd.DataFrame(pupils_list, columns=['name', 'first_name'])
    df.to_excel('./test.xlsx', index=False)
    await context.bot.send_document(update.effective_message.chat_id, 
    document=open("./test.xlsx", "rb"),
    filename="text.xlsx",
    caption="вот файл со списком учеников, который вы заказывали")
    return ConversationHandler.END



async def cancel(update, context):
    # определяем пользователя
    user = update.message.from_user

    update.message.reply_text( 'Мое дело предложить - Ваше отказаться' )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    TOKEN = '5826260933:AAFx5xwYZNfMd12hfk9q43B0uDhAsBXuVR8'
    application = ApplicationBuilder().token(TOKEN).build()

   
    start_handler = CommandHandler('start', start)
    show_handler = CommandHandler('show_pupils', export_excel)
    conv_handler = ConversationHandler(entry_points=[CommandHandler('add_pupil', add_pupil)], states={
        NAME: [MessageHandler(filters.TEXT & (~filters.COMMAND), name)],
        SURNAME : [MessageHandler(filters.TEXT & (~filters.COMMAND), surname)],
        EXPORT : [MessageHandler(filters.TEXT & (~filters.COMMAND), export_excel)]
        }, fallbacks=[CommandHandler('cancel', cancel)],
        )
    application.add_handler(start_handler)
    application.add_handler(conv_handler)
    application.add_handler(show_handler)
    # запускаем приложение    
    application.run_polling()
    print("Your telegram bot is running!")

    application.idle()

