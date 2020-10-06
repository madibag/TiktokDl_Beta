from pyrogram import (
    Client,
    Filters
)
import asyncio
from get_lnk import get_lnk
from upload import Upload


@Client.on_message(Filters.command(["live"]))
async def live(client, message):
    url = message.text.split("/live")[0]
    link ,name = get_lnk(url)
    name = name+"mkv"
    cmd = ["ffmpeg1","-i",link,"-o",name]
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stdout:
        return Upload(client,message,name)
	
