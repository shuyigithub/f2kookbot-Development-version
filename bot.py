#本机器人需您同意f2botEULA协议(https://gitee.com/shuyisuibian/Cooperative-Accession-Agreement/blob/master/F2bot_EULA.md)才可使用

#获取所需要的库(如果报错，请您自己pip)
import asyncio
from khl import Bot, Cert,Message,Channel
import traceback
from khl.card import Card, CardMessage, Module, Types, Element, Struct

# 重试次数
MAX_RETRY = 5

# 机器人token
config = '你的机器人token'

bot = Bot(config)

# 配置kook头链接
kook_base_url = "https://www.kookapp.cn"
kook_headers = {f'Authorization': f"Bot {config}"}
CmdLock = asyncio.Lock()
"""配置命令上锁"""

# 查看bot状态
@bot.command(name='在线检测',case_sensitive=False)
async def alive_check(msg:Message,*arg):
    try:
        await msg.reply(f"机器人在线")# 回复
    except:
        print("bot链接失败")

#群发，谨慎使用
@bot.command('群发', aliases=['群发'],case_sensitive=False)
async def private_chat(msg: Message, *args: str):
    message = ' '.join(args)

    user_list = await msg.ctx.guild.fetch_user_list()
    bot_user = await bot.client.fetch_me()
        
        # 发送消息
    try:
        await msg.reply(f"群发成功")# 回复
    except:
        print("bot链接失败")
    
    for user in user_list:
        # 当为机器人自己时跳过
        if user.id == bot_user.id:
            continue

        for _ in range(MAX_RETRY):
            try:
                await user.send(message)
                await asyncio.sleep(0.6)
                break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    print("F2开源版机器人启动成功！")
    bot.run() 