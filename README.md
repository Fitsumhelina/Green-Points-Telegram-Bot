Green Point Telegram Bot
This repository contains the source code for the Green Point Telegram Bot, a chatbot designed to collect agricultural data and provide analysis and recommendations to users. The bot is built using the Telegram Bot API and integrates with Firebase Firestore for data storage.

Features
User authentication: Users can sign up and log in to the bot using their email and password.
Data collection: Users can input agricultural data such as soil composition, temperature, humidity, and crop type.
Analysis: The bot provides both individual and general analysis of agricultural data, including crop suggestions and fertilizer recommendations.
Integration with Firebase Firestore: User data is securely stored in a Firestore database.
Conversational interface: The bot uses a conversational interface to guide users through data collection and analysis.
Installation
To run the bot locally, follow these steps:

Clone this repository to your local machine.
Install the required dependencies listed in requirements.txt.
Create a Firebase project and obtain the necessary credentials (service account key).
Update the reboot.json file with your Firebase credentials.
Set up a Telegram bot using the BotFather and obtain your bot token.
Update the bot token in the green_points.py file.
Run the bot using python green_points.py.
Usage
Once the bot is running, users can interact with it using the following commands:

/start: Start the conversation and display the main menu.
Collect Data: Begin the data collection process.
Analyze Data: Initiate the data analysis process.
Copyright
This project is licensed under the MIT License.

(c) 2024 fitsum helina


```
MIT License

Copyright (c) [2024] [fitsum helina]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

