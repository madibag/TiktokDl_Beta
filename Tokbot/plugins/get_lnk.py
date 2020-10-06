from TikTokApi import TikTokApi



def get_lnk(url):
    if url.lower().startswith('https://vm.tiktok.com'):
        r = get(url)
        r = r.url.split('.html')[0].replace('https://m.tiktok.com/v/', '')
    elif url.lower().startswith('https://m.tiktok.com/v/'):# or url.startswith('https://www.tiktok.com/video/'):
        r = url.split('.html')[0].replace('https://m.tiktok.com/v/', '')
    else:
        return
    a = api.getTikTokById(r)
    
    dlurl = a['itemInfo']['itemStruct']['video']['downloadAddr']
    return dlurl