import os
from hachoir.metadata import extractMetadata

async def Upload(update,context,file,capt=None,captn=None):
    await context.reply_text('Uploading...')
    #I'M Tired To Look For Other way To send Video So
    #https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#post-a-file-from-disk

    await update.send_video(chat_id = chat_id,
                                video= open(file, 'rb'),
                                caption = capt+'\n'+'🎵:'+captn
                                )
    metadata = extractMetadata(createParser(thumb_image_path))
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await update.send_video(
                chat_id=context.chat.id,
                video=open(file, 'rb'),
                caption=capt+'\n'+'🎵:'+captn,
                width=width,
                height=height,
                supports_streaming=True,
    os.remove(file)
    
    
    



