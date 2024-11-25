import mysql.connector
import logging
import random
import signal
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# MySQL database setup
db = mysql.connector.connect(
    host="localhost",
    user="@MINESHACK24HR",
    password="your_new_password",
    database="telegram_bot",
    charset="utf8mb4",
    collation="utf8mb4_general_ci"
)

cursor = db.cursor()

# Add the is_blocked column if it doesn't already exist
cursor.execute("""
    ALTER TABLE users
    ADD COLUMN IF NOT EXISTS is_blocked BOOLEAN DEFAULT FALSE;
""")
db.commit()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Correct activation key
CORRECT_KEY = "4598"
ADMIN_USER_ID = 5401696006  # Replace with your actual admin user ID
CHANNEL_USERNAME = "Mineshack24hrs"  # Your channel username

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    telegram_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username

    # Check if the user is a member of the channel
    try:
        member = await context.bot.get_chat_member(f"@{CHANNEL_USERNAME}", telegram_id)
        if member.status not in ['member', 'administrator', 'creator']:
            await update.message.reply_text(
                "🚫 You must join our official Telegram channel first:\n"
                "👉 [Join here](https://t.me/Mineshack24hrs)"
            )
            return
    except Exception as e:
        logger.error(f"Failed to check channel membership: {e}")
        await update.message.reply_text(
            "🚫 There was an issue checking your membership. Please make sure you're a member of our official channel."
        )
        return

    # Check if user already exists in the database
    cursor.execute("SELECT COUNT(*) FROM users WHERE telegram_id = %s", (telegram_id,))
    (user_exists,) = cursor.fetchone()

    # Store user data only if they don't already exist
    if user_exists == 0:
        cursor.execute("""
            INSERT INTO users (telegram_id, first_name, last_name, username, is_blocked)
            VALUES (%s, %s, %s, %s, FALSE)
        """, (telegram_id, first_name, last_name, username))
        db.commit()
        await update.message.reply_text("Welcome! Your are one step away from earning.")
    else:
        await update.message.reply_text("Welcome back! You are already doing great.")

    welcome_message = (
        "✅ New bot developed this year is already available for you 🚀\n\n"
        "1️⃣ The bot will allow you to consistently earn every day on the MINES game\n\n"
        "2️⃣ Real earnings from $50-100 every day!💰\n\n"
        "3️⃣ The bot gives signals with a 90% success rate using artificial intelligence!\n\n"
        "🎁 Now PRESS NEXT"
    )
    keyboard = [[InlineKeyboardButton("Next", callback_data='next')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Broadcast message function
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Only allow the admin user to send broadcasts
    if update.message.from_user.id != ADMIN_USER_ID:
        await update.message.reply_text("You are not authorized to send broadcast messages.")
        return

    message = ' '.join(context.args)
    if not message:
        await update.message.reply_text("Please provide a message to broadcast.")
        return

    # Fetch all active users from the database (those not blocked)
    cursor.execute("SELECT telegram_id FROM users WHERE is_blocked = FALSE")
    users = cursor.fetchall()

    for (telegram_id,) in users:
        try:
            await context.bot.send_message(chat_id=telegram_id, text=message)
        except Exception as e:
            logger.error(f"Failed to send message to user {telegram_id}: {e}")

    await update.message.reply_text("Broadcast message sent to all active users.")

# Function to get the count of users and blocked users
async def get_user_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cursor.execute("SELECT COUNT(*) FROM users WHERE is_blocked = FALSE")
    (active_users,) = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM users WHERE is_blocked = TRUE")
    (blocked_users,) = cursor.fetchone()

    await update.message.reply_text(
        f"Total active users: {active_users}\n"
        f"Total blocked users: {blocked_users}"
    )

# Callback handler for the 'next' button
async def next_step(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    next_message = (
        "The bot only works on new 1WIN accounts. Complete 2 conditions and earn from 50-100$🎁\n\n"
        "Activate the bot ☑️\n"
        "1. Register using this link ⤵️\n"
        "➡️ https://1wfqtr.life/?open=register&p=9dcq\n\n"
        "2. After registration, click the CHECK ID button\n\n"
        "📲 If you don't have an extra number to create an account, you can use social networks."
    )

    keyboard = [[InlineKeyboardButton("CHECK ID", callback_data='check_id')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(next_message, reply_markup=reply_markup)

# Callback handler for 'check id' button
async def check_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    check_id_message = (
        "REGISTRATION COMPLETED ✅\n\n"
        "Now top up your balance by $5-10 (use any currency).\n\n"
        "This amount is needed to work with the bot. After replenishing the balance, the BOT is activated❗️\n\n"
        "You can earn from $50-$100 every day 💰"
    )

    keyboard = [
        [InlineKeyboardButton("TOP UP YOUR WALLET", url='https://1wfqtr.life/?open=register&p=9dcq')],
        [InlineKeyboardButton("TOPPED UP? PRESS HERE", callback_data='topped_up')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(check_id_message, reply_markup=reply_markup)

# Callback handler for 'topped up' button
async def topped_up(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    topped_up_message = (
        "Great! Please enter the 4-digit activation key:\n"
        "Send a screenshot of your 1WIN account to @MINESHACK24HR to receive an activation key for the bot 🔑"
 )

    keyboard = [
        [InlineKeyboardButton("Get Activation 🔑", url='https://t.me/MINESHACK24HR')],
        [InlineKeyboardButton("Enter Activation Key", callback_data='enter_key')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(topped_up_message, reply_markup=reply_markup)

# Callback handler for entering the activation key
async def enter_key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    key_message = "Please enter your 4-digit key:"
    await query.edit_message_text(key_message)

    context.user_data['awaiting_key'] = True

# Message handler to capture the activation key entered by the user
async def capture_key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get('awaiting_key', False):
        user_input = update.message.text.strip()

        if user_input == CORRECT_KEY:
            await update.message.reply_text("✅ Correct key! Proceeding to the next step.")
            await web_app_message(update, context)
        else:
            await update.message.reply_text("❌ Incorrect key. Please try again.")

        context.user_data['awaiting_key'] = False
    else:
        await update.message.reply_text("Please click the 'Enter Activation Key' button first.")


# Function to send the web app message after correct activation key
async def web_app_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Construct the message and button to open the web app
    web_app_message = (
        "✅ Your activation is successful!\n\n"
        "Click the button below to open the Web Mini App and start earning."
    )

    # Web app URL to open within Telegram
    web_app_url = "https://mineshac45.github.io/Web.mini.app/"

    # Inline button to open the web app
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=web_app_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the web app link message to the user
    await query.edit_message_text(web_app_message, reply_markup=reply_markup)

# Register handlers
def main() -> None:
    app = ApplicationBuilder().token("7342036273:AAHq0QmeACzYAX0wCyuYRejVfzaslS01cqM").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("userstats", get_user_stats))
    app.add_handler(CallbackQueryHandler(next_step, pattern='next'))
    app.add_handler(CallbackQueryHandler(check_id, pattern='check_id'))
    app.add_handler(CallbackQueryHandler(topped_up, pattern='topped_up'))
    app.add_handler(CallbackQueryHandler(enter_key, pattern='enter_key'))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, capture_key))

    # Graceful shutdown
    def graceful_exit(sig, frame):
        cursor.close()
        db.close()
        app.stop()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, graceful_exit)

    app.run_polling()

if __name__ == "__main__":
    main()


 

