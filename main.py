# DATA
from telegram.ext import Updater,Dispatcher,InlineQueryHandler,CallbackContext
from telegram.update import Update
from telegram import InlineQueryResultArticle,InputTextMessageContent
# ISHLATUVCHILAR

updater=Updater(token='5044358541:AAH0h4R1UWMNiaXn-RjMmzY3Lb5m6EuTVd8')
dispatcher:Dispatcher=updater.dispatcher


#ASOSIY_QISM
def inline_query(update:Update,context:CallbackContext) -> None:
    query=update.inline_query.query
    update.inline_query.answer([
        InlineQueryResultArticle(id="x",title='X',input_message_content=InputTextMessageContent('X')),
        InlineQueryResultArticle(id="o",title='O',input_message_content=InputTextMessageContent('O')),
    ])


# HANDLERLAR
dispatcher.add_handler(InlineQueryHandler(inline_query))

# ISHLATUVCHILAR
updater.start_polling()
updater.idle()