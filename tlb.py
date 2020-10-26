import googlesearch
import discord
import infinity
from discord.ext import commands, tasks
import tweepy
import scraper
import Twitter
import SecretPages
import urbandict as ud
import leaderboard
import json
import asyncio

token = 'MY_TOKEN' 

something = commands.Bot(command_prefix='$', case_insensitive=True)
something.remove_command('help')


@something.event
async def on_ready():
    game = discord.Game("The12Rings ($help)")
    await something.change_presence(activity = game)

@something.event
async def on_message_delete(message):
    chan = message.channel
    embed = discord.Embed(color=0x008000)
    me = something.get_user(647118494076370974)
    embed.add_field(name= f"Deleted message in {chan}", value= f"""Message Deleted = {message.content}
User = {message.author}""", inline = False)
    await me.send(embed = embed)

@something.command()
async def help(ctx):
    page1 = discord.Embed(title= "Help Section",color=0x6c0101)
    page1.set_footer(text = "page 1/6")
    page1.add_field(name="My Info", value=" Hello, I am the Lazy bot. My purpose is to assist humans in their small tasks. Whether it be a simple google search or whether it be looking through twitter. I am here for you, just like any human.", inline=False)
    page2 = discord.Embed(title= "Web Commands",color=0x6c0101)
    page2.set_footer(text = "page 2/6")
    page2.add_field(name="1. $search", value="This command can be used to search google, it can search anything you want it to search on google, and it will give you the same results as google does.This command will return you the top 5 links from google.", inline=False)
    page2.add_field(name="Example", value= "<$search 'elon musk'>", inline=False)
    page2.add_field(name="2. $webpage", value="This command is used to look up a particular website, you can just paste any link and get your required number of information from it. NOTE: PLEASE SPECIFY THE NUMBER OF PARAGRAPHS YOU WANT TO READ",inline=False)
    page2.add_field(name="Example", value="<$webpage http://www.the12rings.com 4>", inline=False)
    page3 = discord.Embed(title= "Twitter Commands",color=0x6c0101)
    page3.set_footer(text="page 3/6")
    page3.add_field(name="1. $twitter", value="This command will give you a number of latest tweets from any person you desire. To use this command, just paste the twitter handle and the number of tweets you want", inline= False)
    page3.add_field(name="Example", value="<$twitter elonmusk 5>", inline=False)
    page4 = discord.Embed(title= "The12Rings Commands",color=0x6c0101)
    page4.set_footer(text = "page 4/6")
    page4.add_field(name="1. $secrets", value="This command will give you a Picture of the desired from the secrets, Quite handy as you won't have to look up secrets again and again... Just give Me the page number ", inline=False)
    page4.add_field(name="Example", value="<$secrets 13>", inline=False)
    page4.add_field(name="2. $text", value="This command will give you the text from any page of the secrets you desire...Again, Just give me the page number", inline=False)
    page4.add_field(name="Example", value="<$text 4>", inline=False)
    page4.add_field(name = "3. $text all", value = "This command will give you a menu that you can nanvigate through to get all the text from the book 'The secrets of the 12 rings'. You can move through pages and read the text for each page through one single command", inline = False)
    page4.add_field(name = "Example", value = "<$text all>", inline = False)
    page4.add_field(name = "$find", value = "This command can be used to search some text in secrets. This command will give you the page number(s) on which this text would be present", inline = False)
    page4.add_field(name = "Example", value = "<$find genius>", inline = False)
    page5 = discord.Embed(title= "Dictionary Commands",color=0x6c0101)
    page5.set_footer(text="page 5/6")
    page5.add_field(name="1. $urban", value="This command will give you the meaning of any word you want from the urban dictionary...Yes, that useless dictionary..idk why I made this command", inline=False)
    page5.add_field(name="Example", value="<$urban 'Boy'>", inline=False)
    page6 = discord.Embed(title= "Leaderboard Commands",color=0x6c0101)
    page6.set_footer(text= "page 6/6")
    page6.add_field(name="2. $top", value= "Returns a number of top players from the Leaderboard of the12rings. Pass a number after the command")
    page6.add_field(name="Example", value="<$top 5>", inline=False)


    pages = [page1, page2, page3, page4, page5, page6]


    message=await ctx.send(embed=pages[0])
    await message.add_reaction('\u23ee')
    await message.add_reaction('\u25c0')
    await message.add_reaction('\u25b6')
    await message.add_reaction('\u23ed')

    i = 0
    emoji = ''
    while True:
        if emoji=='\u23ee':
            i=0
            await message.edit(embed=pages[i])
        if emoji=='\u25c0':
            if i>0:
                i-=1
                await message.edit(embed=pages[i])
        if emoji=='\u25b6':
            if i < 5:
                i+=1
                await message.edit(embed=pages[i])
        if emoji=='\u23ed':
            i = 5
            await message.edit(embed=pages[i])  
        try:
            def check(reaction,user):
                return reaction.message.id == message.id and reaction.message.guild.id == message.guild.id
            res=await something.wait_for('reaction_add', timeout = 60.0, check = check)
            if res==None:
                    break
            if str(res[1])!='The_Lazy_Bot#4241':
                emoji=str(res[0].emoji)
                await message.remove_reaction(res[0].emoji,res[1])
        except asyncio.TimeoutError:
            break
    

@something.command()
async def search(ctx, * , arg):
    try:
        query = arg
        embedVar = discord.Embed(color=0x6c0101)
        for j in googlesearch.search(query, tld="co.in", lang= 'en', num= 5 , stop= 5, pause=2):
            embedVar.add_field(name = "link:", value=f"{j}", inline=False)
        await ctx.channel.send(embed=embedVar)
    except:
        await ctx.send("Some problem occured, try again or contact the developer")


@something.command()
async def webpage(ctx, arg1, arg2):
    if scraper.page(arg1, int(arg2)) is False:
        await ctx.send("Too much info asked")
    else:
        array = []
        info_list = scraper.page(arg1, int(arg2))
        for pages in range(0,int(arg2)):
            pageX = discord.Embed(color=0x6c0101)
            p = pages + 1
            pageX.add_field(name = f"Paragraph{p}", value = info_list[pages], inline = False)
            array.append(pageX)
        try:
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
                    if i < (int(arg2) -1):
                        i+=1
                        await message.edit(embed = array[i])
                if emoji=='\u23ed':
                    i = (int(arg2)-1)
                    await message.edit(embed = array[i])
                try:
                    def check(reaction,user):
                        return reaction.message.id == message.id and reaction.message.guild.id == message.guild.id
                    res=await something.wait_for('reaction_add', timeout = 60.0, check = check)
                    if res==None:
                        break
                    if str(res[1])!='The_Lazy_Bot#4241':
                        emoji=str(res[0].emoji)
                        await message.remove_reaction(res[0].emoji,res[1])
                except asyncio.TimeoutError:
                    break
        except discord.HTTPException:
            await ctx.send("Sorry, Couldn't retrieve the webpage")


@something.command()
async def twitter(ctx, arg1, arg2):
    if Twitter.tweets(arg1, arg2) is not False:
        array = []
        tweet = Twitter.tweets(arg1,arg2)
        for message in range(0,int(arg2)):
            pageX = discord.Embed(color=0x6c0101)
            m = message+1
            pageX.add_field(name = f"Tweet{m}", value = tweet[message], inline = False)
            array.append(pageX)
        message=await ctx.send(embed=array[0])
        await message.add_reaction('\u23ee')
        await message.add_reaction('\u25c0')
        await message.add_reaction('\u25b6')
        await message.add_reaction('\u23ed')

        i = 0
        emoji = ''
        while True:
            if emoji=='\u23ee':
                i=0
                await message.edit(embed=array[i])
            if emoji=='\u25c0':
                if i>0:
                    i-=1
                    await message.edit(embed=array[i])
            if emoji=='\u25b6':
                if i < (int(arg2) -1):
                    i+=1
                    await message.edit(embed=array[i])
            if emoji=='\u23ed':
                i = (int(arg2)-1)
                await message.edit(embed=array[i])  
            try:
                def check(reaction,user):
                    return reaction.message.id == message.id and reaction.message.guild.id == message.guild.id
                res=await something.wait_for('reaction_add', timeout = 60.0, check = check)
                if res==None:
                    break
                if str(res[1])!='The_Lazy_Bot#4241':
                    emoji=str(res[0].emoji)
                    await message.remove_reaction(res[0].emoji,res[1])
            except asyncio.TimeoutError:
                break
        await message.clear_reactions()


@tasks.loop(hours = 24.0)
async def tweet_each_day():
    message_channel = something.get_channel(744906753296302142)
    text = Twitter.tweets("the12rings", 1)
    await message_channel.send(text[0])


@tweet_each_day.before_loop
async def before():
    await something.wait_until_ready()

tweet_each_day.start()


@something.command()
async def secrets(ctx, arg):
    if (int(arg) < 47) and (int(arg) > 0):
        await ctx.send(file=discord.File(f'{arg}.jpg'))
    else:
        await ctx.send("This page does not exist")

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

            try:
                def check(reaction,user):
                    return reaction.message.id == message.id and reaction.message.guild.id == message.guild.id
                res=await something.wait_for('reaction_add', timeout = 60.0, check = check)
                if res==None:
                    break
                if str(res[1])!='The_Lazy_Bot#4241':
                    emoji=str(res[0].emoji)
                    await message.remove_reaction(res[0].emoji,res[1])
            except asyncio.TimeoutError:
                break
        await message.clear_reactions()

    else:
        msg = SecretPages.PageText(arg)
        if msg is not None:
            embedVar = discord.Embed(color=0x6c0101)
            embedVar.add_field(name = f"Info  for Page {arg}", value= msg, inline=False)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("This page does not contain any text ;-;")


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


@something.command()
async def urban(ctx,*,arg):
    try:
        word_list = ud.define(arg)
        definition = word_list[0]
        embedVar = discord.Embed(color=0x6c0101)
        embedVar.add_field(name = "Word", value= definition.get("word"), inline=False)
        embedVar.add_field(name = "Definition", value= definition.get("def"), inline=False)
        embedVar.add_field(name = "Example", value= definition.get("example"), inline=False)
        await ctx.send(embed=embedVar)
    except:
        await ctx.send("An error occured, try again later, or contact the developer")

@something.command()
async def top(ctx, arg):
    embedVar = discord.Embed(color=0x6c0101)
    topper = leaderboard.lead_webcr(int(arg))
    i = 1
    for top in topper:
        leaders = json.loads(top)
        player = leaders.get("id")
        lev = leaders.get("in_level")
        pos = leaders.get("rank")
        since = leaders.get("in_level_since")
        embedVar.add_field(name = f"Top Player {i}", value = f"The player {player} is on the level {lev} since `{since}` and has a rank {pos}", inline= False)
        i += 1
    await ctx.send(embed=embedVar)



@something.command()
async def talk(ctx,*args):
    msg = ctx.message
    if ctx.author.discriminator == '6826':
        await msg.delete()
        await ctx.send(f"{' '.join(args)}")


something.run(token)


#fs@c1ety
#app name- the-very-lazy-bot
