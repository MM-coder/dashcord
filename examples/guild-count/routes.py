# This file will contain all of our website's routes

# Route method formating is shown below:

# If your route function is named "index", it's url will be `url/`
async def index(bot, request):
    """The function name is what the URL path will be, e.g url/route_name"""
    # request.method returns either GET or POST
    if request.method == "GET":
        # We have a GET request.
        
        # As this is an example of a guild counter, we want to pass the bot guilds
        # to the template formatter.
        guilds = len(bot.guilds)
        
        return await bot.dashboard.render_html("index.html", guilds=guilds)
        # bot.dashboard.render_html will format the html file for you.
    
    else:
        # We have a post request.
        # If the post request is a form, the request json will return the data within
        # the form.
        
        json = await request.json()
        
        channel = bot.get_channel(ID)
        await channel.send("We just made a POST request with the data: `{}`".format(str(json)))
        
        return await bot.dashboard.render_html("index.html", guilds=guilds)