
import logging
import random as rd
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
pole = [["*","*","*"],["*","*","*"],["*","*","*"]]
history = {}

win = 0
def check_win(history=history):
    win = 0
    for k in history[user.id]:
        for j in history[user.id][k]:
            if history[user.id][k].count(j)==3:
                win = (k[0])
    if  len(set(history[user.id]["x-row"])) ==3 and len(set(history[user.id]["x-line"])) ==3:
        win= 'крестик'
    elif  len(set(history[user.id]["y-line"])) ==3 and len(set(history[user.id]["y-row"]))==3:
        win= 'нолик'
    else: win = 0
    return win



def show_pole(pole):
    print_show = "".join([" ".join(i)+'\n' for i in pole])
    return print_show

def ai_turn (pole=pole, history=history):
    turn_ai = [rd.randint(0,2) for i in range(2)]
    while not pole[turn_ai[0]][turn_ai[1]]=="*":
        turn_ai = [rd.randint(0,2) for i in range(2)]
    pole[turn_ai[0]][turn_ai[1]]="0"
    history[user.id]['y-row'].append(turn_ai[1])
    history[user.id]['y-line'].append(turn_ai[0])
async def add_pupil(update, context):

    await update.message.reply_text("Чтобы поставить знак - напишите место, например 0 2 через пробел.")
    return NAME


async def name (update, context, pole=pole, history=history, win = win, ):
    await update.message.reply_text("Чтобы поставить знак - напишите место, например 0 2 через пробел.")
    user = update.message.from_user
    if  user.id in history == False:
        history[user.id] = {"x-row":[], 'x-line':[], 'y-row':[], 'y-line':[]} 
        return NAME
    else:         
        input_num = (update.message.text).split()
        print (input_num)
        if pole[int(input_num[0])][int(input_num[1])]=="*":
            pole[int(input_num[0])][int(input_num[1])]="x"
            print(pole[int(input_num[0])][int(input_num[1])])
        else:
            print(pole)
            return NAME
        print(pole)
        print (input_num[1])
        history[user.id]['x-row'].append(input_num[1])
        history[user.id]['x-line'].append(input_num[0])
        if check_win()!=0:
            win = check_win()
            await update.message.reply_text( "Выиграл " + win )  
            
            return NAME
        
        
        ai_turn()
        t = show_pole(pole)
        await update.message.reply_text(t)
        if check_win()!=0:
            win = check_win()
            await update.bot.reply_text( "Выиграл " + win )   
            
        return NAME


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

    conv_handler = ConversationHandler(entry_points=[CommandHandler('add_pupil', add_pupil)], states={
        NAME: [MessageHandler(filters.TEXT & (~filters.COMMAND), name)]

        }, fallbacks=[CommandHandler('cancel', cancel)],
        )
    application.add_handler(start_handler)
    application.add_handler(conv_handler)
  
    # запускаем приложение    
    application.run_polling()
    print("Your telegram bot is running!")

    application.idle()

