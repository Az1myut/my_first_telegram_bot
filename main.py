import telebot

bot=telebot.TeleBot('5410838332:AAFSo1MFJsIZZgzP7YXyQbxp_fgEycgSdJ0')

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
family={}
status=''
details=[]
def parcing(family):
	main_info=''
	for key,value in family.items():
		print(family[key])
		s = ''
		value=' '.join(value)
		s=s+key+' '+value

		main_info=main_info+s+'\n'

	return main_info



@bot.message_handler(commands=['add'])
def register_family(message):
		bot.send_message(message.from_user.id,'Кем ты приходишься семье?')
		bot.register_next_step_handler(message,get_status)

def get_status(message):
	global status,family,details
	status=message.text
	family[status]=details
	bot.send_message(message.from_user.id,'Как тебя зовут?')
	bot.register_next_step_handler(message,get_name)

def get_name(message):
	global status,family,details
	name=message.text
	details.append(name)
	family[status]=details
	bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
	bot.register_next_step_handler(message, get_surname)

def get_surname(message):
	global status,family,details
	surname=message.text
	details.append(surname)
	family[status]=details
	bot.send_message(message.from_user.id, 'Сколько тебе лет ?')
	bot.register_next_step_handler(message, get_age)
def get_age(message):
	global status,family,details
	age=message.text
	details.append(age)
	family[status]=details
	bot.send_message(message.from_user.id,'Данные сохранены')
	details=[]
@bot.message_handler(commands=['show'])
def show_info(message):
	bot.send_message(message.from_user.id,parcing(family))


bot.infinity_polling()