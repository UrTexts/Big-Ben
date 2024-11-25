import discord
from discord.ext import tasks
import asyncio
from datetime import datetime

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.messages = True
intents.message_content = True


class BigBenBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.hourly_chime_task = self.hourly_chime_loop

    async def setup_hook(self):
        self.hourly_chime_task.start()

    async def on_ready(self):
        print(f"{self.user.name} has connected to Discord!")

    @tasks.loop(seconds=1)
    async def hourly_chime_loop(self):
        """Check every second if it's the top of the hour and join a populated VC."""
        now = datetime.now()
        if now.minute == 0 and now.second == 0:  # Top of the hour
            print("It's the top of the hour!")
            for guild in self.guilds:
                for vc in guild.voice_channels:
                    if len(vc.members) > 0:  # Only join populated VCs
                        await self.play_chime(vc)
                        return

    async def play_chime(self, vc):
        """Connect to a voice channel and play chime.mp3."""
        try:
            print(f"Joining voice channel '{vc.name}' in guild '{vc.guild.name}'")
            voice_client = await vc.connect()
            
            # Load and play the MP3 file
            audio_source = discord.FFmpegPCMAudio("chime.mp3")
            voice_client.play(audio_source, after=lambda e: print("Finished playing chime."))
            
            # Wait for the audio to finish
            while voice_client.is_playing():
                await asyncio.sleep(1)
            
            # Disconnect after playing
            await voice_client.disconnect()
            print(f"Disconnected from voice channel '{vc.name}'")
        except discord.ClientException as e:
            print(f"Error connecting to VC: {e}")
        except Exception as e:
            print(f"Error: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Debug command to manually play chime
        if message.content.lower() == "!debug":
            for vc in message.guild.voice_channels:
                if len(vc.members) > 0:  # Only join populated VCs
                    await self.play_chime(vc)
                    await message.channel.send(f"Debug: Played chime in '{vc.name}'")
                    return
            await message.channel.send("No populated voice channels found!")


# Run the bot
bot = BigBenBot()
bot.run("YOUE_TOKEN_HERE")
