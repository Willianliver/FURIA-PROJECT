import logging
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configurações iniciais
TELEGRAM_TOKEN = '7937689301:AAFB_VM7IzJrOkUiLX-Sponto_8wZ_ULefk'
TWITCH_CLIENT_ID = 'g0a6hxzhzx72ojxtbkehh368y60pia'
TWITCH_ACCESS_TOKEN = 'etks66zn2hjvy2hvsx4tkidnfr113x'
CHANNEL_NAME = 'furiatv'# Nome do canal da FURIA na Twitch

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Funções dos comandos

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mensagem de boas-vindas e menu principal"""
    menu = (
        "🎮 *Bem-vindo ao Bot Oficial da FURIA!*\n\n"
        "Escolha o que você quer fazer:\n\n"
        "• 🔴 /status — Verificar se estamos AO VIVO na Twitch\n"
        "• 🗓️ /proximosjogos — Ver agenda dos próximos jogos\n"
        "• 🧑‍🤝‍🧑 /elenco — Conhecer os jogadores atuais\n"
        "• 🏆 /titulos — Ver nossos títulos conquistados\n"
        "• ℹ️ /sobre — Conhecer a história da FURIA\n\n"
        "#GoFURIA 🐺🔥"
    )
    await update.message.reply_text(menu, parse_mode='Markdown')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Exibe o menu principal"""
    await start(update, context)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Verifica se o canal da FURIA está ao vivo"""
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {TWITCH_ACCESS_TOKEN}'
    }
    url = f"https://api.twitch.tv/helix/streams?user_login={CHANNEL_NAME}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['data']:
            stream = data['data'][0]
            title = stream['title']
            viewer_count = stream['viewer_count']
            message = f"🚨 A FURIA está *AO VIVO* agora!\n\n🎯 *{title}*\n👀 {viewer_count} espectadores assistindo!\n\n👉 https://www.twitch.tv/{CHANNEL_NAME}"
        else:
            message = "⚡ A FURIA *não está ao vivo* no momento."
    else:
        message = "❌ Erro ao consultar o status. Tente novamente em breve."

    await update.message.reply_text(message, parse_mode='Markdown')

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra o elenco atual"""
    message = (
        "🧑‍🤝‍🧑 *Elenco Atual da FURIA (CS2)*:\n\n"
        "• 🧠 KSCERATO\n"
        "• 🔥 yuurih\n"
        "• 🎯 arT\n"
        "• 🧱 chelo\n"
        "• 💣 FalleN\n\n"
        "#GoFURIA 🐺🔥"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def proximosjogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra os próximos jogos (fake por enquanto)"""
    message = (
        "🗓️ *Próximos Jogos da FURIA*:\n\n"
        "• 28/04 - FURIA vs Team Liquid (ESL Pro League)\n"
        "• 05/05 - FURIA vs G2 Esports (IEM Dallas)\n\n"
        "Agenda sujeita a alterações! 🎮"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def titulos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra os títulos da FURIA"""
    message = (
        "🏆 *Títulos Recentes da FURIA*:\n\n"
        "• CBCS Elite League Season 1 🥇\n"
        "• DreamHack Open Summer 🥇\n"
        "• ESL Pro League Season 12 🥇\n"
        "• IEM New York 🥇\n\n"
        "Mais conquistas virão! 🔥"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def sobre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra a história da FURIA"""
    message = (
        "ℹ️ *Sobre a FURIA*:\n\n"
        "Fundada em 2017, a FURIA é uma organização brasileira de eSports conhecida mundialmente, "
        "especialmente no CS:GO. Com uma filosofia agressiva dentro e fora dos servidores, conquistou "
        "milhares de fãs e grandes títulos ao redor do mundo.\n\n"
        "#GoFURIA 🐺🔥"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

# Função principal
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Registrando os comandos
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('menu', menu))
    app.add_handler(CommandHandler('status', status))
    app.add_handler(CommandHandler('elenco', elenco))
    app.add_handler(CommandHandler('proximosjogos', proximosjogos))
    app.add_handler(CommandHandler('titulos', titulos))
    app.add_handler(CommandHandler('sobre', sobre))

    print("🤖 Bot da FURIA rodando...")
    app.run_polling()
    print("🤖 Bot encerrado.")