import hikari
import lightbulb
from mal import *

bot = lightbulb.BotApp(
    token="MTAwMzI0NzQ5OTkxMTM3Njk1Ng.G11CNI.ZJYKDeBL_Zy5oYnRjBWgsOjmlpB_EXJjhXpjI8"
)

#server count
@bot.listen()
async def on_starting(_: hikari.StartedEvent) -> None:
    await bot.update_presence(
        activity=hikari.Activity(
            name=f"{len([*await bot.rest.fetch_my_guilds()])} servers! | /help",
            type=hikari.ActivityType.WATCHING,
        )
    )

prem_users = [
    "364400063281102852"
]

#anime
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.option("name", "Anime")
@lightbulb.command("anime", "Look up an anime.", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def anime(ctx: lightbulb.Context) -> None:
    if any(word in str(ctx.author.id) for word in prem_users):
        await ctx.command.cooldown_manager.reset_cooldown(ctx)
        name = ctx.options.name
        search = AnimeSearch(name)
        anime = Anime(search.results[0].mal_id)
        embed = hikari.Embed(
            title=f"{anime.title_english} | {anime.title_japanese}",
            description=anime.synopsis,
            color=0x2f3136
        )
        embed.set_thumbnail(anime.image_url)
        embed.add_field(name="Premiered", value=anime.premiered, inline=True)
        embed.add_field(name="Status", value=anime.status, inline=True)
        embed.add_field(name="Type", value=anime.type, inline=True)
        embed.add_field(name="Score", value=anime.score, inline=True)
        embed.add_field(name="Episodes", value=anime.episodes, inline=True)
        embed.add_field(name="Broadcast Time", value=anime.broadcast, inline=True)
        embed.add_field(name="Ranking", value=anime.rank, inline=True)
        embed.add_field(name="Popularity", value=anime.popularity, inline=True)
        embed.add_field(name="Rating", value=anime.rating, inline=True)
        await ctx.respond(embed=embed)
    else:
        name = ctx.options.name
        search = AnimeSearch(name)
        anime = Anime(search.results[0].mal_id)
        embed = hikari.Embed(
            title=f"{anime.title_english} | {anime.title_japanese}",
            description=anime.synopsis,
            color=0x2f3136
        )
        embed.set_thumbnail(anime.image_url)
        embed.add_field(name="Premiered", value=anime.premiered, inline=True)
        embed.add_field(name="Status", value=anime.status, inline=True)
        embed.add_field(name="Type", value=anime.type, inline=True)
        embed.add_field(name="Score", value=anime.score, inline=True)
        embed.add_field(name="Episodes", value=anime.episodes, inline=True)
        embed.add_field(name="Broadcast Time", value=anime.broadcast, inline=True)
        embed.add_field(name="Ranking", value=anime.rank, inline=True)
        embed.add_field(name="Popularity", value=anime.popularity, inline=True)
        embed.add_field(name="Rating", value=anime.rating, inline=True)
        await ctx.respond(embed=embed)

#manga
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.option("name", "Manga")
@lightbulb.command("manga", "Look up a manga.", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def manga(ctx: lightbulb.Context) -> None:
    if any(word in str(ctx.author.id) for word in prem_users):
        await ctx.command.cooldown_manager.reset_cooldown(ctx)
        name = ctx.options.name
        search = MangaSearch(name)
        manga = Manga(search.results[0].mal_id)
        embed = hikari.Embed(
            title=f"{manga.title_english} | {manga.title_japanese}",
            description=manga.synopsis,
            color=0x2f3136
        )
        embed.set_thumbnail(manga.image_url)
        embed.add_field(name="Score", value=manga.score, inline=True)
        embed.add_field(name="Ranking", value=manga.rank, inline=True)
        embed.add_field(name="Popularity", value=manga.popularity, inline=True)
        embed.add_field(name="Status", value=manga.status, inline=True)
        embed.add_field(name="Chapters", value=manga.chapters, inline=True)
        embed.add_field(name="Volumes", value=manga.volumes, inline=True)
        await ctx.respond(embed=embed)
    else:
        name = ctx.options.name
        search = MangaSearch(name)
        manga = Manga(search.results[0].mal_id)
        embed = hikari.Embed(
            title=f"{manga.title_english} | {manga.title_japanese}",
            description=manga.synopsis,
            color=0x2f3136
        )
        embed.set_thumbnail(manga.image_url)
        embed.add_field(name="Score", value=manga.score, inline=True)
        embed.add_field(name="Ranking", value=manga.rank, inline=True)
        embed.add_field(name="Popularity", value=manga.popularity, inline=True)
        embed.add_field(name="Status", value=manga.status, inline=True)
        embed.add_field(name="Chapters", value=manga.chapters, inline=True)
        embed.add_field(name="Volumes", value=manga.volumes, inline=True)
        await ctx.respond(embed=embed)

#help command
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.command("help", "Get help")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
	if any(word in str(ctx.author.id) for word in prem_users):
		await ctx.command.cooldown_manager.reset_cooldown(ctx)
		embed = hikari.Embed(
			title="__**Commands**__",
			description="**__Main:__** \n **/anime:** Look up an anime. \n **/manga:** Look up a manga. \n \n **__Misc:__** \n **/invite:** Get the bot's invite link. \n **/vote:** Get the link to vote at top.gg. \n **/support:** Invite to join the support server. \n **/donate:** Donate to support Weeb Bot. \n **/more:** Check out more bots from me.",
			color = 0x2f3136
		)
		await ctx.respond(embed=embed)
	else:
		embed = hikari.Embed(
			title="__**Commands**__",
			description="**__Main:__** \n **/anime:** Look up an anime. \n **/manga:** Look up a manga. \n \n **__Misc:__** \n **/invite:** Get the bot's invite link. \n **/vote:** Get the link to vote at top.gg. \n **/support:** Invite to join the support server. \n **/donate:** Donate to support Weeb Bot. \n **/more:** Check out more bots from me.",
			color = 0x2f3136
		)
		await ctx.respond(embed=embed)

#invite command
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.command("invite", "Get the bot's invite link.")
@lightbulb.implements(lightbulb.SlashCommand)
async def invite(ctx):
	if any(word in str(ctx.author.id) for word in prem_users):
		await ctx.command.cooldown_manager.reset_cooldown(ctx)
		embed = hikari.Embed(
			title="Invite:",
			description="Get the bot's invite link [here](https://discord.com/api/oauth2/authorize?client_id=1003247499911376956&permissions=414464723008&scope=bot%20applications.commands).",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)
	else:
		embed = hikari.Embed(
			title="Invite:",
			description="Get the bot's invite link [here](https://discord.com/api/oauth2/authorize?client_id=1003247499911376956&permissions=414464723008&scope=bot%20applications.commands).",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)

#vote command
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.command("vote", "Get the link to vote at top.gg.")
@lightbulb.implements(lightbulb.SlashCommand)
async def vote(ctx):
	if any(word in str(ctx.author.id) for word in prem_users):
		await ctx.command.cooldown_manager.reset_cooldown(ctx)
		embed = hikari.Embed(
			title="Vote:",
			description="Click [here] to vote on top.gg. Thank you! \n (will work after it's on top.gg)",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)
	else:
		embed = hikari.Embed(
			title="Vote:",
			description="Click [here] to vote on top.gg. Thank you! \n (will work after it's on top.gg)",
			color = 0x2f3136
		)
		await ctx.respond(embed=embed)

#support command
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.command("support", "Invite to join the support server.")
@lightbulb.implements(lightbulb.SlashCommand)
async def support(ctx):
	if any(word in str(ctx.author.id) for word in prem_users):
		await ctx.command.cooldown_manager.reset_cooldown(ctx)
		embed = hikari.Embed(
			title="Support:",
			description="Click [here](https://discord.com/invite/RZsknj575x) to join the support server.",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)
	else:
		embed = hikari.Embed(
			title="Support:",
			description="Click [here](https://discord.com/invite/RZsknj575x) to join the support server.",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)

#donate command
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.command("donate", "Donate to support Weeb Bot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def donate(ctx):
	if any(word in str(ctx.author.id) for word in prem_users):
		await ctx.command.cooldown_manager.reset_cooldown(ctx)
		embed = hikari.Embed(
			title="Donate:",
			description="[Buy me a coffee](https://www.buymeacoffee.com/azael) to support me in making Weeb Bot. Thank you! :)",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)
	else:
		embed = hikari.Embed(
			title="Donate:",
			description="[Buy me a coffee](https://www.buymeacoffee.com/azael) to support me in making Weeb Bot. Thank you! :)",
			color=0x2f3136
		)
		await ctx.respond(embed=embed)

#more command
@bot.command
@lightbulb.add_cooldown(length = 20, uses = 1, bucket = lightbulb.UserBucket)
@lightbulb.command("more", "Check out more bots from me.")
@lightbulb.implements(lightbulb.SlashCommand)
async def more(ctx):
    if any(word in str(ctx.author.id) for word in prem_users):
        await ctx.command.cooldown_manager.reset_cooldown(ctx)
        embed = hikari.Embed(
            title="More:",
            description="Click [here](https://top.gg/user/67067136345571328) to check out more bots from me.",
            color=0x2f3136
        )
        await ctx.respond(embed=embed)
    else:
        embed = hikari.Embed(
            title="More:",
            description="Click [here](https://top.gg/user/67067136345571328) to check out more bots from me.",
            color=0x2f3136
        )
        await ctx.respond(embed=embed)

#error handling
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond("I couldn't find what you were looking for :( \nPlease use the first few words of the series in your query if you get this message.")
        raise event.exception

    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"`/{event.context.command.name}` is on cooldown. Retry in `{exception.retry_after:.0f}` seconds. ⏱️ \n To avoid cooldowns, become a member at https://www.buymeacoffee.com/azael. \n It helps keep the bot online. 👉👈")
    else:
        raise exception

bot.run()