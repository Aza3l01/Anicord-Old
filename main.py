import hikari
import lightbulb
from mal import *

bot = lightbulb.BotApp(
    token="MTAwMzI0NzQ5OTkxMTM3Njk1Ng.G11CNI.ZJYKDeBL_Zy5oYnRjBWgsOjmlpB_EXJjhXpjI8",
    default_enabled_guilds=(857112618963566592)
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

@bot.command
@lightbulb.option("name", "Anime")
@lightbulb.command("anime", "Look up an anime.", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def anime(ctx: lightbulb.Context) -> None:
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

bot.run()