import discord
import aiohttp
import asyncio
import json  # Pour parser le NDJSON

TOKEN = 'YOUR_TOKEN_HERE'  # ⚠️ Remplace avec ton vrai token, ne le partage pas !

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def get_ollama_response(query):
    print(f"[Ollama] Requête envoyée via API: {query}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama2-uncensored:7b-chat-q3_K_S", "prompt": query},  # Modèle à utiliser
            ) as resp:
                if resp.status == 200:
                    full_response = ""
                    async for line in resp.content:
                        if not line:
                            continue
                        try:
                            json_line = line.decode('utf-8').strip()
                            if json_line:
                                data = json.loads(json_line)
                                if "response" in data:
                                    full_response += data["response"]
                        except json.JSONDecodeError as decode_error:
                            print(f"[Ollama] Erreur JSON: {decode_error}")
                    return full_response.strip() or "Erreur: aucune réponse."
                else:
                    return f"Erreur HTTP {resp.status}"
    except Exception as e:
        print(f"[Ollama] Exception API: {e}")
        return f"Erreur API Ollama: {e}"

@client.event
async def on_ready():
    print(f"[Bot] Connecté en tant que {client.user}")

def create_embed(title, description, color=discord.Color.blue()):
    return discord.Embed(title=title, description=description, color=color)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"[Message] Reçu: {message.content} de {message.author}")

    if message.content.startswith('!ask'):
        query = message.content[len('!ask '):]
        print(f"[Bot] Traitement de la requête: {query}")
        response = await get_ollama_response(query)
        embed = create_embed("Réponse d'Ollama", response, discord.Color.green())
        await message.channel.send(embed=embed)

    elif message.content.startswith('!status'):
        print("[Bot] Commande !status reçue.")
        embed = create_embed("Statut du Bot", "Bot est en ligne et connecté à Ollama ! 🚀", discord.Color.purple())
        await message.channel.send(embed=embed)

client.run(TOKEN)
