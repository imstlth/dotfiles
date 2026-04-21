import discord
from discord import app_commands
import time

# TODO
# Enregistrer le numéro des tickets dans le fichier database principal
# Continuer à faire les commandes

GUILD_ID = 1103606361914351656
TOKEN = "MTIxNDYxODA3NDI1NTMyNzMwNA.GHxePK.TyRZLaUelEOgf11rOINfK9A8KqGctddyoO_1I0"
TICKET_CATEGORY_ID = ""
ID_TO_SEE_TICKETS = ""
TICKET_TIME_DELTA = 300 # On peut faire /ticket toutes les 5 minutes

latest_ticket_time = time.time()
ticket_n = 1

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents)
tree = app_commands.CommandTree(client)

def is_ticket_category(category):
    return category.id == TICKET_CATEGORY_ID

@tree.command(
    name="ticket",
    description="Create a ticket to report something to the staff",
    guild=discord.Object(id=GUILD_ID)
)
async def ticket(interaction):
    global ticket_n, latest_ticket_time
    if time.time() - latest_ticket_time < TICKET_TIME_DELTA:
        await interaction.response.send_message("Last ticket was created less than 5 minutes, please wait.")
    else:
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.guild.me: discord.PermissionOverwrite(read_messages=True),
            interaction.user: discord.PermissionOverwrite(read_messages=True),
            interaction.guild.get_role(ID_TO_SEE_TICKETS): discord.PermissionOverwrite(read_messages=True)
        }
        category = filter(is_ticket_category, interaction.guild.categories)
        await interaction.guild.create_text_channel("ticket " + str(ticket_n), overwrites, category)
        ticket_n += 1
        latest_ticket_time = time.time()

@tree.command(
    name="delete ticket",
    description="Delete the channel created for a ticket - STAFF ONLY",
    guild=discord.Object(id=GUILD_ID)
)
async def delete_ticket(interaction):
    if interaction.user.get_role(ID_TO_SEE_TICKETS) is not None:
        await interaction.channel.delete()


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Ready!")

client.run(TOKEN)
