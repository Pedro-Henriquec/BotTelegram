
import telebot
from telebot import types

CHAVE_API = "6106450681:AAElLtGMcb9lm8AzlRaDjK9JzzqCVKpcV80"
bot = telebot.TeleBot(CHAVE_API)

# Função para enviar o link do grupo
@bot.message_handler(commands=['link'])
def send_link(message):
    # Crie um botão com link
    keyboard = types.InlineKeyboardButton(text="Tips", url="https://t.me/+BcQjBTRaKTI4NzI5")

    # Crie uma teclado de teclas inline
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(keyboard)

    # Envie a mensagem com o botão de link
    bot.send_message(message.chat.id, "Entre no grupo:", reply_markup=inline_keyboard)

# Função para enviar a opção 1 com um botão de link
@bot.message_handler(commands=["1"])
def Opcao1(mensagem):
    # Crie um botão com link
    keyboard = types.InlineKeyboardButton(text="Entrar no grupo", url="https://t.me/+BcQjBTRaKTI4NzI5")

    # Crie uma teclado de teclas inline
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(keyboard)

    # Envie a mensagem com o botão de link
    bot.send_message(mensagem.chat.id, "Clique no botão abaixo para entrar no grupo:", reply_markup=inline_keyboard)

# Função para enviar a opção 2
@bot.message_handler(commands=["2"])
def Opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para falar com o suporte envie um e-mail para: suporte@blabla.com")

# Função para enviar a opção 3
@bot.message_handler(commands=["3"])
def Opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu! Um abraço de volta.")

# Função para verificar as mensagens
def verificar(mensagem):
    return True

# Função para responder as mensagens
@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, "Olá")
    texto = """
        Escolha uma opção para continuar (Clique no item):
        /1 Entrar no grupo
        /2 Falar com o suporte
        /3 Mandar um abraço"""
    bot.send_message(mensagem.chat.id, texto)

bot.polling()
