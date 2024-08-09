import discord
from discord.ext import commands
import random
from datetime import timezone, timedelta

# token of your app / bot
TOKEN = ''

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="v", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

def get_random_color():
    return discord.Color(random.randint(0x000000, 0xFFFFFF))

def format_timestamp(timestamp):
    gmt2 = timezone(timedelta(hours=2))
    return timestamp.replace(tzinfo=timezone.utc).astimezone(gmt2).strftime("%d/%m/%Y %H:%M GMT+2")

@bot.command()
async def whois(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)

        embed = discord.Embed(title=f"Who is {user}?", color=get_random_color())

        if user.avatar:
            embed.set_thumbnail(url=user.avatar.url)
        
        if user.banner:
            embed.set_image(url=user.banner.url)
        
        embed.add_field(name="Name", value=f"*{user.name}*", inline=True)
        embed.add_field(name="Discriminator", value=f"`{user.discriminator}`", inline=True)
        embed.add_field(name="ID", value=f"`{user.id}`", inline=True)
        embed.add_field(name="Bot", value=f"`{user.bot}`", inline=True)
        embed.add_field(name="Created At", value=f"`{format_timestamp(user.created_at)}`", inline=True)

        if user.accent_color:
            embed.add_field(name="Profile Color", value=f"`#{user.accent_color.value:06X}`", inline=True)

        await ctx.send(embed=embed)
    except discord.NotFound:
        await ctx.send("User not found.")
    except discord.HTTPException as e:
        await ctx.send(f"Error fetching user: {e}")

bot.run(TOKEN)
