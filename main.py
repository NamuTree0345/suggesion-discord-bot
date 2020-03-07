import discord

# 정보
# 개발자: 마른생선(redwikitv@gmail.com 또는 johanbag290@naver.com)
# 
# 절대로 소스를 바꾸지 마세요!
# 
# 바꿔도 되는 분들은 제가 따로 알려드립니다.
# 바꿔도 되는 분들:
# 초코큐브님
# 레도님
# 그리고 discord.py와 파이썬을 좀 아시는 분들
# 
# 바꿔도 되는 분들이여도 핵심 부분은 건들지 않았으면 합니다.
#
# 소스를 바꿔야 되는 부분
# 
# 아래의 설정
# 70번째 줄(관리자 다 수정하시면 ..... 지워주세요)
#
# 감사하신 분들:
#
# Discord(Discord 개발자)
# Rapptz(discord.py 개발자)
#
# 서포터 홍보:
#
# 초신마
# https://discord.gg/zjHpxbb


# 설정
special_send_guild_id = 숫자 # 특별하게 관리자에게 보내는 서버 아이디
special_administrator = 숫자 # special_send_guild_id의 길드의 건의에 건의를 보낼 사람

suggesion_channel = '건의' # 건의 채널 이름
bot_token = '토큰' # 봇토큰

noarg_text = '뒤쪽을 입력하지 않아 처리되지 않습니다.' # 꼭 해야하는 매개변수 입력 하지 않을 시 print 되는 텍스트
noperm_text = '권한이 없습니다.' # 권한이 없을 때 사용자에게 보내는 DM

emb_title = '건의' # 건의 임베드 타이틀
emb_sug_user_nim = '님의 건의' # 유저네임 다음 오늘 글자들
emb_sug_user_text = '유저 이름' # 유저네임 오기 전 글자

ans_title = '건의 답변!' # 답변 임베드 타이틀
ans_nim = '님의 건의' # 건의한 사람 뒤에 오는 글자
ans_sug_text_title = '건의 내용' # 그 사람이 건의한 내용 타이틀
ans_text_title = '건의' # 건의 타이틀





client = discord.Client()

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_message(msg):
    if msg.author.id == client.user.id:
        return

    if msg.channel.name == suggesion_channel: # suggestion channel
        if msg.content.startswith('!답변'):  # answer

            if msg.author.id == 아이디 or msg.author.id == 아이디 ..... : ### 관리자 아이디 적어주시면 됩니다. 곧 역할 이름으로 바꿀수 있는것이 옵니다!







                try:
                    print('답변') # answer
                    print(msg.content.split('/')[1])
                    print('유저아이디: ' + msg.content.split('/')[2]) # userid: 
                    print('그 유저가 건의한 내용: ' + msg.content.split('/')[3]) # the user suggested
                    embed = discord.Embed()
                    embed.title = ans_title # Q&A
                    embed.description = '<@{}> {}'.format(msg.content.split('/')[2], ans_nim) # @<{}>'s suggetion
                    embed.add_field(name=ans_sug_text_title,value=msg.content.split('/')[3], inline=True) # Suggetion context
                    embed.add_field(name=ans_text_title,value=msg.content.split('/')[1]) # Answer


                    await msg.channel.send(embed=embed)
                    await msg.delete()
                except:
                    await msg.delete()
                    await msg.author.send('명령어의 사용법: !답변/<답변내용>/<유저 아이디(맨션용)>/그 유저가 건의한 내용') # how to use this command: !Answer/<answer context>/<user id(for manshion the user)>/<suggestion context>
                    print(noarg_text)
            else:
                await msg.delete()
                await msg.author.send(noperm_text)
            
        elif msg.guild.id == special_send_guild_id:
            embed = discord.Embed()
            embed.title = emb_title
            embed.description = msg.author.name + emb_sug_user_nim
            embed.add_field(name=emb_sug_user_text,value=msg.content,inline=True)
            usr = client.get_user(special_administrator)

            await usr.send(embed=embed)

            await msg.channel.send(embed=embed)
            await msg.delete()

        else:
            embed = discord.Embed()
            embed.title = emb_title
            embed.description = msg.author.name + emb_sug_user_nim
            embed.add_field(name=emb_sug_user_text,value=msg.content,inline=True)

            await msg.channel.send(embed=embed)
            await msg.delete()

client.run(bot_token)