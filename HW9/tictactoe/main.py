
import logging
import random as rd
import pandas as pd
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters
from dotenv import load_dotenv
load_dotenv()

import os

load_dotenv()
TOKEN = os.getenv('TOKEN')



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


print('test')
async def start(update, context):
    # ожидание отправки сообщения по сети - нужен `await`
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="""Доступные команды
                                   /start_play - начало игры в крестики нолики
                                   
                                   /cancel - выход в главное меню
                                   
                                   
                                   """)


NAME, GAME_OVER = range(1,3)
pole = [["*","*","*"],["*","*","*"],["*","*","*"]]
history = {1:{"x-row":[], 'x-line':[], 'y-row':[], 'y-line':[]}}


win = 0
def check_win(id, history=history, win = win):
    temp = 0
    for k in history[id]:
        for j in history[id][k]:
            if history[id][k].count(j)==3:
                temp= (k[0])
    if  len(set(history[id]["x-row"])) ==3 and len(set(history[id]["x-line"])) ==3 and 1 in history[id]["x-line"] and 1 in history[id]["x-row"]:
        win= 'крестик'
    elif  len(set(history[id]["y-line"])) ==3 and len(set(history[id]["y-row"]))==3 and 1 in history[id]["y-line"] and 1 in history[id]["y-row"]:
        win= 'нолик'
    elif temp == 'x':
        win= 'крестик'
    elif temp == 'y':
        win= 'нолик'
    else: win = 0
    return win



def show_pole(pole):
    print_show = "".join([" ".join(i)+'\n' for i in pole])
    return print_show

def ai_turn (id, pole=pole, history=history):
    turn_ai = [rd.randint(0,2) for i in range(2)]
    while not pole[turn_ai[0]][turn_ai[1]]=="*":
        turn_ai = [rd.randint(0,2) for i in range(2)]
    pole[turn_ai[0]][turn_ai[1]]="0"
    history[id]['y-row'].append(turn_ai[1])
    history[id]['y-line'].append(turn_ai[0])
async def start_play(update, context, history=history, pole=pole):

    await update.message.reply_text("Поиграем? набери стартовую комбинацию, например 0 1")
    user = update.message.from_user
    id = int(user.id)
    if  id in history:
        return NAME
    else:
        history[id] = {"x-row":[], 'x-line':[], 'y-row':[], 'y-line':[]} 
        
        return NAME

async def game_over(update, context, win= win):
    
    return ConversationHandler.END

async def name (update, context, pole=pole, history=history, win = win, ):
    print(history)
    await update.message.reply_text("Чтобы поставить знак - напишите место, например 0 2 через пробел.")
    user = update.message.from_user
    
    input_num = (update.message.text).split()
    print (input_num)
    if pole[int(input_num[0])][int(input_num[1])]=="*":
        pole[int(input_num[0])][int(input_num[1])]="x"
        
    else:
        print(pole)
        return NAME
    print(pole)
    
    history[int(user.id)]['x-row'].append(input_num[1])
    history[int(user.id)]['x-line'].append(input_num[0])
    win = check_win(int(user.id))
    print(win)
    
    if win!=0:
        await update.message.reply_text(show_pole(pole),reply_markup=ReplyKeyboardRemove() )
        await update.message.reply_text( "Выиграл "+ str(win), reply_markup=ReplyKeyboardRemove() )
        history[int(user.id)] = {"x-row":[], 'x-line':[], 'y-row':[], 'y-line':[]}
        return ConversationHandler.END

      
    ai_turn(int(user.id))
    t = show_pole(pole)
    await update.message.reply_text(t)
    win = check_win(int(user.id))
    print(win)
    print(history)
    if win!=0:
        await update.message.reply_text( "Выиграл "+ str(win)+". Нажми /start чтобы продолжить", reply_markup=ReplyKeyboardRemove())
        history[int(user.id)] = {"x-row":[], 'x-line':[], 'y-row':[], 'y-line':[]}
        return ConversationHandler.END 
        
    return NAME


async def cancel(update, context):
    # определяем пользователя
    user = update.message.from_user

    await update.message.reply_text( 'Мое дело предложить - Ваше отказаться' )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    
    application = ApplicationBuilder().token(TOKEN).build()

   
    start_handler = CommandHandler('start', start)

    conv_handler = ConversationHandler(entry_points=[CommandHandler('start_play', start_play)], states={
        NAME: [MessageHandler(filters.TEXT & (~filters.COMMAND), name)],
        GAME_OVER: [MessageHandler(filters.TEXT & (~filters.COMMAND), game_over)]
        }, fallbacks=[CommandHandler('cancel', cancel)],
        )
    application.add_handler(start_handler)
    application.add_handler(conv_handler)
  
    # запускаем приложение    
    application.run_polling()
    print("Your telegram bot is running!")

    application.idle()

