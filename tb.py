import discord 
from discord.ext import commands, tasks
import scraper
import Twitter
import sq
import json
import SecretPages
import leaderboard

token = 'MY_TOKEN'

something = commands.Bot(command_prefix='!')


@something.event
async def on_message_delete(message):
    chan = message.channel
    embed = discord.Embed(color=0x008000)
    me = something.get_user(647118494076370974)
    embed.add_field(name= f"Deleted message in {chan}", value= f"""Message Deleted = {message.content}
User = {message.author}""", inline = False)
    await me.send(embed = embed)

@something.command()
async def text(ctx, arg):
    msg = SecretPages.PageText(arg)
    if arg == "all":
        Pages = SecretPages.page()
        array = []
        for i in Pages:
            text_all = discord.Embed(color=0x6c0101)
            text_all.add_field(name = f"{i}", value = Pages[i], inline = False)
            array.append(text_all)

        message=await ctx.send(embed = array[0])
        await message.add_reaction('\u23ee')
        await message.add_reaction('\u25c0')
        await message.add_reaction('\u25b6')
        await message.add_reaction('\u23ed')

        i = 0
        emoji = ''
        while True:
            if emoji=='\u23ee':
                i=0
                await message.edit(embed = array[i])
            if emoji=='\u25c0':
                if i>0:
                    i-=1
                    await message.edit(embed = array[i])
            if emoji=='\u25b6':
                if i < (len(Pages) -1):
                    i+=1
                    await message.edit(embed = array[i])
            if emoji=='\u23ed':
                i = (len(Pages)-1)
                await message.edit(embed = array[i])

            res=await something.wait_for('reaction_add')
            if res==None:
                break
            if str(res[1])!='test_bot#0075':
                emoji=str(res[0].emoji)
                await message.remove_reaction(res[0].emoji,res[1])
        await message.clear_reactions()

@something.command()
async def find(ctx, * , arg):
	Pages = SecretPages.page()
	array = []
	for i in Pages:
		if arg.lower() in Pages[i].lower():
			array.append(i)
		else:
			pass
	if len(array) != 0:
		await ctx.send(f"The text is present in pages `{list(i for i in array)}`")
	else:
		await ctx.send("This text is not present")


something.run(token)
