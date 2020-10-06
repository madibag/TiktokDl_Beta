from pyrogram import Client, Filters
from TikTokApi import TikTokApi
from requests import get
from subprocess import call,PIPE
from upload import Upload

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    name = message.chat.first_name
    await message.reply_text('''HI {} This is Tiktok Video 
                                Downloader 
                                Made with ❤️ in 🇪🇹
                                By <a href="https://t.me/nahom_d">Nahom</a>
                        
                                Type /help To get more Info'''.format(name),
                                parse_mode="html")
@Client.on_message(Filters.command(["help"]))
async def help(client,message):
    await message.reply_text('''To Use This bot
                                Simply Paste the
                                link''')

@Client.on_message(pyrogram.Filters.regex(pattern=".*http.*"))
async def download(client,message):
    api = TikTokApi()
    url = message.text
    if url.lower().startswith('https://vm.tiktok.com'):
        r = get(url)
        r = r.url.split('.html')[0].replace('https://m.tiktok.com/v/', '')
    elif url.lower().startswith('https://m.tiktok.com/v/'):# or url.startswith('https://www.tiktok.com/video/'):
        r = url.split('.html')[0].replace('https://m.tiktok.com/v/', '')
    else:
        return
    a = api.getTikTokById(r)
    
    dlurl = a['itemInfo']['itemStruct']['video']['downloadAddr']
    
    capt = a["itemInfo"]["shareMeta"]["desc"]
    captn = a['itemInfo']['itemStruct']['music']['title']
    
    file = a["itemInfo"]["itemStruct"]["author"]["signature"]
    a = await client.send_message(chat_id = message.chat.id,
                            text="Downloading...",
                            reply_to_message_id = message.message_id)
    
    file_name = file+"mp4"
    cmd = []
    cmd.append('wget')
    cmd.append('-o')
    cmd.append(file_name)
    cmd.append(dlurl)
    
    
    s = call(cmd, stdout=PIPE, stderr=PIPE)

    stdout, stderr = s.communicate()
    print(stdout)
    if stderr:
        await client.edit_message_text(clat_id = message.chat.id,
                                       text='An Error  Occured',
                                       message_id = a.message_id)
    else:
        return Upload(client,message,file_name,capt,captn)
    