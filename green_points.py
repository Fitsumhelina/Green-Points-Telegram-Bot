import firebase_admin
from firebase_admin import credentials, firestore
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler


# Initialize Firebase
cred = credentials.Certificate("./../reboot.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize bot with your token
application = ApplicationBuilder().token("7032042459:AAHLSgx5OXicJvrdML5T9g6QfdMnB0YNWkA").build()

# Define states
LOGIN, SIGNUP, REGISTER_CONTACT, REGISTER_EMAIL, REGISTER_PASSWORD, LOGIN_EMAIL, LOGIN_PASSWORD, ADD_PROFILE, PROFILE_NAME, PROFILE_SEX, PROFILE_REGION, PROFILE_NITROGEN, PROFILE_PHOSPHORUS, PROFILE_POTASSIUM, PROFILE_TEMPERATURE, PROFILE_HUMIDITY, PROFILE_PH, PROFILE_RAINFALL, PROFILE_MOISTURE, PROFILE_CROP_TYPE, PROFILE_SOIL_TYPE = range(21)

# Define PROFILE_INDIVIDUAL_ANALYSIS globally
PROFILE_INDIVIDUAL_ANALYSIS = range(22, 25)  # Choose appropriate index range
PROFILE_FARMER_NAME = 25  # Define the state for awaiting farmer's name input



# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Clear user data
    context.user_data.clear()
    buttons = [
        [KeyboardButton("Collect Data"), KeyboardButton("Analyze Data")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons)
    await update.message.reply_text("Welcome to Green Point! Choose an option:", reply_markup=keyboard)
    
    # End the conversation so a new one can start fresh
    return ConversationHandler.END

# Collect Data Handler
async def collect_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Clear user data
    context.user_data.clear()
    
    buttons = [
        [KeyboardButton("Login"), KeyboardButton("Sign Up")],
        [KeyboardButton("Main")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons)
    await update.message.reply_text("Please choose an option:", reply_markup=keyboard)
    return LOGIN

# Login Handler
async def login(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please enter your email:")
    return LOGIN_EMAIL

async def login_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['email'] = update.message.text
    await update.message.reply_text("Please enter your password:")
    return LOGIN_PASSWORD

async def login_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    email = context.user_data['email']
    password = update.message.text
    user_ref = db.collection('agents').document(email)
    user = user_ref.get()
    if user.exists and user.to_dict()['password'] == password:
        context.user_data['agent_id'] = email
        await update.message.reply_text("Login successful!", reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Add Profile")], [KeyboardButton("Main")]]))
        return ADD_PROFILE
    else:
        await update.message.reply_text("Invalid email or password. Please try again or sign up.")
        return LOGIN

# Sign Up Handler
async def sign_up(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please share your contact information:", reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Share Contact", request_contact=True)]], one_time_keyboard=True))
    return REGISTER_CONTACT

# Register Contact Handler
async def register_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['contact'] = update.message.contact.phone_number
    await update.message.reply_text("Please enter your email:", reply_markup=ReplyKeyboardRemove())
    return REGISTER_EMAIL

# Register Email Handler
async def register_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['email'] = update.message.text
    await update.message.reply_text("Please enter your password:")
    return REGISTER_PASSWORD

# Register Password Handler
async def register_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    email = context.user_data['email']
    contact = context.user_data['contact']
    password = update.message.text
    db.collection('agents').document(email).set({
        'contact': contact,
        'password': password
    })
    context.user_data['agent_id'] = email
    await update.message.reply_text("Registration successful!", reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Add Profile")], [KeyboardButton("Main")]]))
    return ADD_PROFILE

# Add Profile Handler
async def add_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please enter the farmer's name:")
    return PROFILE_NAME

async def profile_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['farmer_name'] = update.message.text
    await update.message.reply_text("Please enter the farmer's sex (Male/Female):")
    return PROFILE_SEX

async def profile_sex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['sex'] = update.message.text
    await update.message.reply_text("Please enter the farmer's region:")
    return PROFILE_REGION
async def profile_region(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['region'] = update.message.text
    await update.message.reply_text("Please enter the nitrogen level:")
    return PROFILE_NITROGEN

async def profile_nitrogen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['nitrogen'] = update.message.text
    await update.message.reply_text("Please enter the phosphorus level:")
    return PROFILE_PHOSPHORUS

async def profile_phosphorus(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['phosphorus'] = update.message.text
    await update.message.reply_text("Please enter the potassium level:")
    return PROFILE_POTASSIUM

async def profile_potassium(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['potassium'] = update.message.text
    await update.message.reply_text("Please enter the temperature:")
    return PROFILE_TEMPERATURE

async def profile_temperature(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['temperature'] = update.message.text
    await update.message.reply_text("Please enter the humidity:")
    return PROFILE_HUMIDITY

async def profile_humidity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['humidity'] = update.message.text
    await update.message.reply_text("Please enter the pH level:")
    return PROFILE_PH

async def profile_ph(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['ph'] = update.message.text
    await update.message.reply_text("Please enter the rainfall:")
    return PROFILE_RAINFALL

async def profile_rainfall(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['rainfall'] = update.message.text
    await update.message.reply_text("Please enter the moisture level:")
    return PROFILE_MOISTURE


async def profile_moisture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['moisture'] = update.message.text
    await update.message.reply_text("Please enter the crop type:")
    return PROFILE_CROP_TYPE

async def profile_crop_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['crop_type'] = update.message.text
    await update.message.reply_text("Please enter the soil type:")
    return PROFILE_SOIL_TYPE

async def profile_soil_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['soil_type'] = update.message.text
    
    # Save profile data to Firestore
    farmer_id = db.collection('farmers').document().id
    agent_id = context.user_data['agent_id']
    db.collection('farmers').document(farmer_id).set({
        'agent_id': agent_id,
        'farmer_name': context.user_data['farmer_name'],
        'sex': context.user_data['sex'],
        'region': context.user_data['region'],
        'nitrogen': context.user_data['nitrogen'],
        'phosphorus': context.user_data['phosphorus'],
        'potassium': context.user_data['potassium'],
        'temperature': context.user_data['temperature'],
        'humidity': context.user_data['humidity'],
        'ph': context.user_data['ph'],
        'rainfall': context.user_data['rainfall'],
        'moisture': context.user_data['moisture'],
        'crop_type': context.user_data['crop_type'],
        'soil_type': context.user_data['soil_type']
    })
    
    await update.message.reply_text("Farmer profile added successfully!", reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Add Profile")], [KeyboardButton("Main")]]))
    return ADD_PROFILE

# Analyze Data Handler
async def analyze_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.clear()
    
    buttons = [
        [KeyboardButton("Individual Analysis"), KeyboardButton("General Analysis")],
        [KeyboardButton("Main")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons)
    await update.message.reply_text("Choose the type of analysis:", reply_markup=keyboard)

async def individual_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = [
        [KeyboardButton("Crop Suggestions"), KeyboardButton("Fertilizer Suggestions")],
        [KeyboardButton("Main")]
    ]
    keyboard = ReplyKeyboardMarkup(buttons)
    await update.message.reply_text("Choose an option for individual analysis:", reply_markup=keyboard)
    return PROFILE_INDIVIDUAL_ANALYSIS

async def crop_suggestions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    crop_suggestions_ref = db.collection('product_suggested')
    crop_suggestions_docs = crop_suggestions_ref.get()
    if crop_suggestions_docs:
        suggestions_text = "Crop Suggestions:\n"
        for doc in crop_suggestions_docs:
            crop_data = doc.to_dict()
            suggestions_text += f"- Farmer Name: {crop_data.get('name')}, Crop: {crop_data.get('crop')}, \n"
    else:
        suggestions_text = "No crop suggestions available."
    await update.message.reply_text(suggestions_text)
    return ConversationHandler.END

async def fertilizer_suggestions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    crop_suggestions_ref = db.collection('Fertilizer_suggested')
    crop_suggestions_docs = crop_suggestions_ref.get()
    if crop_suggestions_docs:
        suggestions_text = "fertilizer Suggestions:\n"
        for doc in crop_suggestions_docs:
            crop_data = doc.to_dict()
            suggestions_text += f"- Farmer Name: {crop_data.get('name')}, fertilizer: {crop_data.get('fertilizer')}, \n"
    else:
        suggestions_text = "No fertilizer suggestions available."
    await update.message.reply_text(suggestions_text)
    return ConversationHandler.END

async def profile_individual_analysis(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    choice = update.message.text
    if choice == "Crop Suggestions":
        await crop_suggestions(update, context)
    elif choice == "Fertilizer Suggestions":
        await fertilizer_suggestions(update, context)
    else:
        await start(update, context)
    return ConversationHandler.END


# Conversation handler for individual analysis choice
conv_individual_analysis_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex('^Individual Analysis$'), individual_analysis)],
    states={
        PROFILE_INDIVIDUAL_ANALYSIS : [
            MessageHandler(filters.Regex('^(Crop Suggestions|Fertilizer Suggestions)$'), profile_individual_analysis),
            MessageHandler(filters.Regex('^Main$'), start)
        ]
    },
    fallbacks=[CommandHandler('start', start)],
)
# Define the conversation handler for collecting data
conv_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex('^Collect Data$'), collect_data)],
    states={
        LOGIN: [
            MessageHandler(filters.Regex('^(Login|Sign Up|Main)$'), login),
            MessageHandler(filters.Regex('^Main$'), start)
        ],
        LOGIN_EMAIL: [MessageHandler(filters.Regex('.+'), login_email)],
        LOGIN_PASSWORD: [MessageHandler(filters.Regex('.+'), login_password)],
        SIGNUP: [
            MessageHandler(filters.Regex('^(Login|Sign Up|Main)$'), sign_up),
            MessageHandler(filters.Regex('^Main$'), start)
        ],
        REGISTER_CONTACT: [MessageHandler(filters._Contact, register_contact)],
        REGISTER_EMAIL: [MessageHandler(filters.Regex('.+'), register_email)],
        REGISTER_PASSWORD: [MessageHandler(filters.Regex('.+'), register_password)],
        ADD_PROFILE: [
            MessageHandler(filters.Regex('^(Add Profile|Main)$'), add_profile),
            MessageHandler(filters.Regex('^Main$'), start)
        ],
        PROFILE_NAME: [MessageHandler(filters.Regex('.+'), profile_name)],
        PROFILE_SEX: [MessageHandler(filters.Regex('.+'), profile_sex)],
        PROFILE_REGION: [MessageHandler(filters.Regex('.+'), profile_region)],
        PROFILE_NITROGEN: [MessageHandler(filters.Regex('.+'), profile_nitrogen)],
        PROFILE_PHOSPHORUS: [MessageHandler(filters.Regex('.+'), profile_phosphorus)],
        PROFILE_POTASSIUM: [MessageHandler(filters.Regex('.+'), profile_potassium)],
        PROFILE_TEMPERATURE: [MessageHandler(filters.Regex('.+'), profile_temperature)],
        PROFILE_HUMIDITY: [MessageHandler(filters.Regex('.+'), profile_humidity)],
        PROFILE_PH: [MessageHandler(filters.Regex('.+'), profile_ph)],
        PROFILE_RAINFALL: [MessageHandler(filters.Regex('.+'), profile_rainfall)],
        PROFILE_MOISTURE: [MessageHandler(filters.Regex('.+'), profile_moisture)],
        PROFILE_CROP_TYPE: [MessageHandler(filters.Regex('.+'), profile_crop_type)],
        PROFILE_SOIL_TYPE: [MessageHandler(filters.Regex('.+'), profile_soil_type)],
    },
    fallbacks=[CommandHandler('start', start)],
)


application.add_handler(CommandHandler('start', start))
# Add conv_individual_analysis_handler before conv_handler
application.add_handler(conv_individual_analysis_handler)
application.add_handler(conv_handler)
application.add_handler(MessageHandler(filters.Regex('^Analyze Data$'), analyze_data))
application.add_handler(MessageHandler(filters.Regex('^Main$'), start))


if __name__ == '__main__':
    application.run_polling()

