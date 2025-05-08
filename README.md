# 🤖 Discord x Ollama Chatbot

A local Discord bot powered by [Ollama](https://ollama.com) using the **llama2-uncensored7b-chat-q3_K_S** model for unfiltered, raw AI conversations.  
No OpenAI, no cloud. **Everything runs on your machine.**

---

## 🚀 Features

- Ask questions via Discord using `!ask`
- Generates replies through the uncensored LLaMA2 model on **localhost**
- Responses are sent as rich Discord embeds
- Fully local & offline-capable — no internet needed

---

## 📦 Setup

### 1. Clone the repo


git clone https://github.com/your-user/your-repo.git

>cd your-repo

### 2. Install Python dependencies

>pip install -r requirements.txt

### 3. Configure the bot
Edit llama2-bot.py and replace:

>TOKEN = 'YOUR_TOKEN_HERE'

with your real Discord bot token.

Also, make sure this line is correct:

>"model": "llama2-uncensored7b-chat-q3_K_S"

## 🧠 Ollama Setup
### 1. Install Ollama
Download and install Ollama from → https://ollama.com/download

### 2. Pull or load the model

>ollama pull llama2-uncensored7b-chat-q3_K_S

### ⚠️ If this model isn’t available online, you need to create it manually using a Modelfile.
Just make sure it’s available locally under the name above.

### 3. Run Ollama
Ollama should run automatically. If not:

>ollama run llama2-uncensored7b-chat-q3_K_S

## 💬 Discord Commands
### Command	Description

>!ask <message>	Ask something to the AI model

>!status	Check if the bot is online

>!help	Show available commands

## 🛠 Requirements
>Python 3.7+

>discord.py

>aiohttp

>colorama

>Ollama (installed & running locally)

⚠️ Warning
This project uses an uncensored LLaMA2 model for educational purposes.
Use at your own risk and responsibility.

# 👑 Credits
## Bot by [Blackeige]

Model: Uncensored LLaMA2 variant (q3_K_S)

Based on Ollama stack & local AI pipelines
