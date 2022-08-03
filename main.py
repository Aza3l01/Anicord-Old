import hikari
import lightbulb
from mal import *
import random

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
        embed.set_footer("Queries are served by an unoffical MAL API and Weeb Bot has no control over the content.")
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
        embed.set_footer("Queries are served by an unoffical MAL API and Weeb Bot has no control over the content.")
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
        embed.set_footer("Queries are served by an unoffical MAL API and Weeb Bot has no control over the content.")
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
        embed.set_footer("Queries are served by an unoffical MAL API and Weeb Bot has no control over the content.")
        await ctx.respond(embed=embed)

#rp help command
@bot.command
@lightbulb.command("roleplay", "Look up all the roleplay commands.")
@lightbulb.implements(lightbulb.SlashCommand)
async def roleplay(ctx):
    embed = hikari.Embed(
        title="Roleplay:",
        description="**Affection:** \n /kiss, /cuddle, /lick, /pat, /shy \n \n **Negative Passive:** \n /pout, /shrug, /run, /die, /cry \n \n **Negative Offensive:** \n /bite, /slap, /shoot, /glare",
        color=0x2f3136
    )
    embed.set_footer("Roleplay commands are still in development and may not always work.")
    await ctx.respond(embed=embed)

kiss = [
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385531167260683/1.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385531469254716/2.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385531817369670/3.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385532199059456/4.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385532526219284/5.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385554118492201/6.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385529632129086/7.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385530022203453/8.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385530357755954/9.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004385530768793711/10.gif"
]

#rp_kiss
@bot.command
@lightbulb.option("member", "The member you want to kiss.", type=hikari.User)
@lightbulb.command("kiss", "Kiss someone.")
@lightbulb.implements(lightbulb.SlashCommand)
async def kiss(ctx):
    embed = hikari.Embed(
        title="",
        description=f"**{ctx.author} kisses {ctx.options.member.mention}**",
        color=0x2f3136
    )
    embed.set_image(random.choice(kiss))
    await ctx.respond(embed=embed)

cuddle = [
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402208600760422/1.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402232139206676/2.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402241953857546/3.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402251726598265/4.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402267979513936/5.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402488482484314/6.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402486662152342/7.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402487106744441/8.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402487475851324/9.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004402487991742585/10.gif"
]

#rp_cuddle
@bot.command
@lightbulb.option("cuddle", "The member you want to cuddle with.", type=hikari.User)
@lightbulb.command("cuddle", "Cuddle someone.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cuddle(ctx):
    embed = hikari.Embed(
        title="",
        description=f"**{ctx.author} cuddles with {ctx.options.member.mention}**",
        color=0x2f3136
    )
    embed.set_image(random.choice(cuddle))
    await ctx.respond(embed=embed)

lick = [
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409253026611360/1.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409253693489272/2.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409254368776372/3.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409255199252520/4.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409255635451964/5.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409256075866263/6.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409256482701352/7.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409257225113740/8.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409257791336629/9.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004409258248503347/10.gif"
]

#rp_lick
@bot.command
@lightbulb.option("member", "The member you want to lick.", type=hikari.User)
@lightbulb.command("lick", "Lick someone.")
@lightbulb.implements(lightbulb.SlashCommand)
async def lick(ctx):
    embed = hikari.Embed(
        title="",
        description=f"**{ctx.author} licks {ctx.options.member.mention}**",
        color=0x2f3136
    )
    embed.set_image(random.choice(lick))
    await ctx.respond(embed=embed)

bite = [
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133801959637002/bc3f5037-b30f-4f26-989f-12461c31da71.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133802983030814/cb233dd9-5875-44c1-9c05-6287ad4cccb9.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133803406663700/cfe3479f-f589-4048-884b-24c7bde2a684.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133803733823609/1b0e22a5-0141-4a9f-8dc4-42613503d9c8.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133804144869506/4cdffd7c-4a52-4d32-9d9b-f9beef46f2fc.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133804685930576/67decd1b-fb4f-48bb-8215-7068c3f3661a.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133805222793307/550a3070-187b-44fd-8987-0bd3cdff567c.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133805575131198/8183e5b4-e820-4d76-9c8f-f634b06f9d7b.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133806028095508/b9b20a3b-4e2e-4989-8460-1d35430b0803.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133807298973861/22b00501-940b-4bb5-bd7b-19c3e48380f1.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133807798104214/d9023388-c46c-4976-9856-e0e166c3c901.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133811396812811/de6cf869-916c-4fc2-876d-4b2fabb75cf9.gif",
    "https://cdn.discordapp.com/attachments/924728966739279882/1004133806917308496/uV7u_csFIiE.gif"
]

#rp_bite
@bot.command
@lightbulb.option("member", "The member you want to bite.", type=hikari.User)
@lightbulb.command("bite", "Bite someone.")
@lightbulb.implements(lightbulb.SlashCommand)
async def bite(ctx):
    embed = hikari.Embed(
        title="",
        description=f"**{ctx.author} bites {ctx.options.member.mention}**",
        color=0x2f3136
    )
    embed.set_image(random.choice(bite))
    await ctx.respond(embed=embed)

#help command
@bot.command
@lightbulb.command("help", "Get help")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    embed = hikari.Embed(
		title="__**Commands**__",
		description="**__Main:__** \n **/anime:** Look up an anime. \n **/manga:** Look up a manga. \n **/roleplay:** Look up all the roleplay commands. \n \n **__Misc:__** \n **/invite:** Get the bot's invite link. \n **/vote:** Get the link to vote at top.gg. \n **/support:** Invite to join the support server. \n **/donate:** Donate to support Weeb Bot. \n **/more:** Check out more bots from me.",
		color = 0x2f3136
	)
    await ctx.respond(embed=embed)

#invite command
@bot.command
@lightbulb.command("invite", "Get the bot's invite link.")
@lightbulb.implements(lightbulb.SlashCommand)
async def invite(ctx):
    embed = hikari.Embed(
        title="Invite:",
		description="Get the bot's invite link [here](https://discord.com/api/oauth2/authorize?client_id=1003247499911376956&permissions=414464723008&scope=bot%20applications.commands).",
		color=0x2f3136
	)
    await ctx.respond(embed=embed)

#vote command
@bot.command
@lightbulb.command("vote", "Get the link to vote at top.gg.")
@lightbulb.implements(lightbulb.SlashCommand)
async def vote(ctx):
    embed = hikari.Embed(
		title="Vote:",
		description="Click [here](https://top.gg/bot/1003247499911376956/vote) to vote on top.gg. Thank you!",
		color=0x2f3136
    )
    await ctx.respond(embed=embed)

#support command
@bot.command
@lightbulb.command("support", "Invite to join the support server.")
@lightbulb.implements(lightbulb.SlashCommand)
async def support(ctx):
    embed = hikari.Embed(
        title="Support:",
		description="Click [here](https://discord.com/invite/RZsknj575x) to join the support server.",
		color=0x2f3136
	)
    await ctx.respond(embed=embed)

#donate command
@bot.command
@lightbulb.command("donate", "Donate to support Weeb Bot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def donate(ctx):
    embed = hikari.Embed(
        title="Donate:",
        description="[Buy me a coffee](https://www.buymeacoffee.com/azael) to support me in making Weeb Bot. Thank you! :)",
		color=0x2f3136
	)
    await ctx.respond(embed=embed)

#more command
@bot.command
@lightbulb.command("more", "Check out more bots from me.")
@lightbulb.implements(lightbulb.SlashCommand)
async def more(ctx):
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
        if event.context.command.name == anime or event.context.command.name == manga:
            await event.context.respond("I couldn't find what you were looking for :( \nPlease use the first few words of the series in your query if you get this message.")
            raise event.exception
        else:
            await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`. Please fill in all necessary arguments.")
            raise event.exception


    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"`/{event.context.command.name}` is on cooldown. Retry in `{exception.retry_after:.0f}` seconds. ⏱️ \n To avoid cooldowns, become a member at https://www.buymeacoffee.com/azael. \n It helps keep the bot online.")
    else:
        raise exception

bot.run()