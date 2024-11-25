# Big Ben Bot ⏰
Big Ben Bot is a Discord bot that joins a populated voice channel every hour, plays a chime (like the famous Big Ben clock in London), and then leaves. It ensures the chime plays at the top of the hour in real-time.
# Features
  -Hourly Chime: Joins a voice channel with at least one user and plays the chime.mp3 file every hour.
  -Customizable: Replace chime.mp3 with your own audio file to personalize the hourly chime.
  -Manual Debug Command: Use the !debug command to trigger the chime manually.
# Prerequisites
  Python 3.8+
Required Python libraries:
  discord.py
  pydub (if ffmpeg isn't used)
  ffmpeg installed on your system (used for audio playback).
#Installation
  Clone the repository,
Copy code
  `git clone https://github.com/UrTexts/Big-Ben.git`
  `cd BigBenBot`
# Ensure ffmpeg is installed:

  Linux: Install via your package manager:
    `sudo apt install ffmpeg`
  Windows: Download and install FFmpeg.
  
  Mac: Install with Homebrew:

    `brew install ffmpeg`
# Setup
  Place your audio file named chime.mp3 in the same directory as the bot script.
  Open bigben.py and replace "YOUR_BOT_TOKEN" with your bot token from the Discord Developer Portal.
# Usage
  Run the bot:
  `python bigben.py`
  Add your bot to a Discord server using its OAuth2 URL.
  The bot will automatically join a populated voice channel and play the chime every hour.
  Debug manually with the !debug command in a text channel.

# Customization
  Replace chime.mp3 with any MP3 file for a custom chime.
  Modify the hourly logic in hourly_chime_loop if you'd like different behavior.

# Troubleshooting
  Bot not joining a channel: Ensure there’s at least one user in the voice channel.
  Audio issues: Verify ffmpeg is installed and working. Test by running:
    `ffmpeg -version`
