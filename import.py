import asyncio
import discord

app = discord.Client()

token = "NzE2NzEyODk3MzY3MTEzNzYw.XxFEgA.Fr56UymMj0hsEZuf-DUHts4uWlM"
calcResult = 0

@app.event
async def on_message(message):
    if message.content == "!알려 명령어":
        await message.channel.send("```[명령어]\n\n!알려 게임명령어, !알려 홈페이지, !알려 돈페트\n!알려 환포퀘스트, !알려 페트이름\n!알려 탑승 캐릭터종류``````[남자캐릭터 종류]\n남꼬맹이, 석기미남, 불량소년, 어리버리, 돌쇠, 곰아저씨\n[여자캐릭터 종류]\n여꼬맹이, 내숭소녀, 물개소녀, 귀염둥이, 터프소녀, 몸짱아줌마\n[신규 캐릭터]\n울보천사, 사자소년, 바람소년, 정글소녀, 툰가, 산적```")
    if message.content == "!알려 탑승 남꼬맹이":
        embed=discord.Embed(color=0xf02, title="꼬맹이(남) 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726679905378631691/feb7b5667036ec9c.PNG")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 석기미남":
        embed=discord.Embed(color=0xf02, title="석기미남 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726679916032294972/994bb60bba1b6c7d.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 어리버리":
        embed=discord.Embed(color=0xf02, title="어리버리 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726679921765646416/59d262209a288200.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 불량소년":
        embed=discord.Embed(color=0xf02, title="불량소년 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726679927885398076/bb1300dd1de5f832.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 곰아저씨":
        embed=discord.Embed(color=0xf02, title="곰아저씨 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726679938781937674/f5c3eb159c481444.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 돌쇠":
        embed=discord.Embed(color=0xf02, title="돌쇠 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726679933270753310/c8edfa71cb565786.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 여꼬맹이":
        embed=discord.Embed(color=0xf02, title="여꼬맹이 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726803596888506458/dea5ec1c6ec81fd3.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 내숭소녀":
        embed=discord.Embed(color=0xf02, title="내숭소녀 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726803607239786506/6d84bf8efdd9f128.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 귀염둥이":
        embed=discord.Embed(color=0xf02, title="귀염둥이 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726803634473664513/071e42545a48963d.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 물개소녀":
        embed=discord.Embed(color=0xf02, title="물개소녀 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726803625153658880/72c3547c84fc8697.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 터프소녀":
        embed=discord.Embed(color=0xf02, title="터프소녀 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726803650026012672/8eb95a1a55d1d7ee.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 몸짱아줌마":
        embed=discord.Embed(color=0xf02, title="몸짱아줌마 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726803663988981850/eb401762bfcd542c.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 사자소년":
        embed=discord.Embed(color=0xf02, title="사자소년 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726875760777756682/8778f8dfb975a00d.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 바람소년":
        embed=discord.Embed(color=0xf02, title="바람소년 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726876151175446628/de689aabb677d4ae.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 울보천사":
        embed=discord.Embed(color=0xf02, title="울보천사 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726875452563783760/85d9afc1cda53792.PNG")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 정글소녀":
        embed=discord.Embed(color=0xf02, title="정글소녀 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726876506051182702/c5fe34f5776e0790.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 툰가":
        embed=discord.Embed(color=0xf02, title="툰가 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726876685382713364/86cac5957e9c7305.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 탑승 산적":
        embed=discord.Embed(color=0xf02, title="산적 탑승 페트목록", timestamp=message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726876898151628800/fb3544cead7b6af5.png")
        await message.channel.send(embed=embed)    
    if message.content == "!알려 게임명령어": 
        await message.channel.send("```\n유저명령어\n\n[캐릭터 관련]\n/완력, /str : 완력에 레벨업 스탯을 분배합니다.\n/순발력, /스피드, /dex : 순발력에 레벨업 스탯을 분배합니다.\n/건강, /def : 건강에 레벨업 스탯을 분배합니다.\n/체력, /hp : 체력에 레벨업 스탯을 분배합니다.\n/환포 : 현재 상태에서 환생 시 받는 환생 포인트를 출력합니다.``````\n[전투]\n/1 : 자동전투를 ON/OFF 설정합니다.``````\n[파티]\n/초대, /invite (닉네임) : 파티에 상대방을 초대합니다.\n/탈퇴, /out : 파티에서 탈퇴합니다.\n/리더 (1~5) : 파티 내 지정 플레이어에게 리더를 위임합니다. 위임당시 자동전투 상태였다면 같게 적용됩니다.\n/강퇴, /kick (닉네임) : 파티에서 해당 플레이어를 제외시킵니다.``````\n[경험치]\n/경구온 : 경험치 구슬 사용\n/경구오프 : 경험치 구슬 사용중지``````\n[벽청의 소라]\n/벽청온 : 벽청의 소라 사용\n/벽청오프 : 벽청의 소라 사용중지``````\n[기타]\n/정보, /info : 캐릭터의 간단한 정보를 표시합니다.\n/찾기, /find (닉네임) : 해당플레이어의 위치 및 정보를 확인합니다.\n/검색, /search (페트명) : 해당페트의 정보를 출력합니다.\n/랭킹 (페트명) : 100레벨 이상 대상페트의 랭킹을 확인합니다.\n/경험치, /exp : 사용시 캐릭터 + 소지한 페트들의 경험치를 출력합니다.\n/정리 : 인벤토리의 중첩이 가능한 아이템을 모두 중첩,정리 합니다 [최대200개]```")
    if message.content == "!알려 홈페이지":
        if message.author.dm_channel:
            await message.author.dm_channel.send("위드서버 홈페이지 : http://stonewith.com/")
        elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("홈페이지 : http://stonewith.com/")
    if message.content == "!알려 돈페트":
        await message.channel.send("```[환생포인트] 쿠오산 박사 = 쿠보\n[환생포인트] 퀴즈마스터 = 얼룩부이비, 골드부비\n[환생포인트] 부의 부탁 = 크루거, 타이혼[1등급], 알테로스\n[환생포인트] 채석장의 비밀 = 모나시프\n[환생포인트] 마쥬의 미로 = 불그리, 황금복덩이\n[환생포인트] 카난퀘스트 = 휴보\n[일반퀘스트] 초보자 퀘스트 = 실버우리\n[복권페트] 테르가, 테이토스, 노르노르, 노르곤\n[환생보상페트] 골로스[1등급], 환생얼룩우리[1등급], 투이\n[필드레이드] 복우리```")
    if message.content == "!알려 환포퀘스트":
        await message.channel.send("```환생포인트 퀘스트목록\n[1]성인식\n[2]친구의 우정\n[3]먀쥬의 미로\n[4]야무야무 도끼\n[5]리푸섬 진입퀘스트\n[6]하늘섬 진입퀘스트\n[7]퀴즈 마스터\n[8]오형제의 시험\n[9]채석장의 비밀\n[10]채굴권 다툼\n[11]공룡박사 (루니)\n[12]공룡박사 (베르가)\n[13]카난 이벤트\n[14]자연의 균형\n[15]4개의 보물\n[16]딸을 찾아주세요\n[17]우리스케의 고백\n[18]한의 도끼\n[19]몽환 이벤트 (3회)\n[20]부의 부탁```")
    if message.content == "!알려 두리":
        embed=discord.Embed(color=0xff00, title="두리[수4/화6]", description="획득방법 : 샴기르마을 초기지원 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 4, 5, 36', value = '성장률 : 공 1.96, 방 1.26, 순 1.64, 내구력 10.24 (전체 4.85)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716894913765310474/0d7406cae331e3a8.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 얼룩우리":
        embed=discord.Embed(color=0xff00, title="얼룩우리[지10]", description="획득방법 : 마리너스 마을 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 5, 3, 27', value = '성장률 : 공 1.68, 방 1.88, 순 1.30, 내구력 10.24 (전체 4.85)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716896504345919498/8f26dabf92e686c5.gif")
        await message.channel.send(embed=embed)        
    if message.content == "!알려 환생얼룩우리":
        embed=discord.Embed(color=0xff00, title="환생얼룩우리[지5/풍5] (1등급)", description="획득방법 : 환생 보상 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 9, 7, 56', value = '성장률 : 공 1.74, 방 1.86, 순 1.35, 내구력 10.76 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716896504345919498/8f26dabf92e686c5.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 우리":
        embed=discord.Embed(color=0xff00, title="우리[지8/수2]", description="획득방법 : 마리너스 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 2, 2, 3, 16', value = '성장률 : 공 1.36, 방 1.56, 순 1.75, 내구력 9.63 (전체 4.68)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716900184793153596/1add3335504999c3.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 불그리":
        embed=discord.Embed(color=0xff00, title="불그리[화7/풍3] (2등급)", description="획득방법 : 마쥬의 미로 랜덤보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 3, 3, 3, 20', value = '성장률 : 공 1.65, 방 1.48, 순 1.78, 내구력 9.81 (전체 4.90)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716902179268591626/-X.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 실버우리":
        embed=discord.Embed(color=0xff00, title="실버우리[지5/풍5] (2등급)", description="획득방법 : 초보자 이벤트 (초기지원 페트 80레벨 보상)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 7, 6, 38', value = '성장률 : 공 1.66, 방 1.75, 순 1.56, 내구력 9.53 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716902536682143744/8829e096e18447d3.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 우리스타":
        embed=discord.Embed(color=0xff00, title="우리스타[지4/수6]", description="획득방법 : 복우리 레이드", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 6, 4, 48', value = '성장률 : 공 1.94, 방 1.47, 순 1.07, 내구력 11.42 (전체 4.49)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716902944456441866/9a950d5431823fb3.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 킹우리":
        embed=discord.Embed(color=0xff00, title="킹우리[수3/화7]", description="획득방법 : 복우리 레이드", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 5, 4, 39', value = '성장률 : 공 2.10, 방 1.50, 순 1.16, 내구력 10.12 (전체 4.75)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716904090512130048/e220963dbe3f4e23.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 복우리":
        embed=discord.Embed(color=0xff00, title="복우리[풍10] (2등급)", description="획득방법 : 복우리 레이드", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 5, 4, 35', value = '성장률 : 공 2.05, 방 1.50, 순 1.42, 내구력 10.12 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716904761466683492/49a8b9c856d9f3b6.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 푸우리":
        embed=discord.Embed(color=0xff00, title="푸우리[수8/화2]", description="획득방법 : 얼룩우리 포획지역 (요리-꿀꿀이 죽)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 6, 6, 48', value = '성장률 : 공 1.86, 방 1.56, 순 1.45, 내구력 11.04 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717641251528114186/273c6d5adbb385c7.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 녹우리":
        embed=discord.Embed(color=0xff00, title="녹우리[지6/풍4]", description="획득방법 : 얼룩우리 포획지역 (요리-꿀꿀이 죽)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 7, 6, 41', value = '성장률 : 공 1.62, 방 1.75, 순 1.59, 내구력 9.86 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717641261674135632/89561a9919f7593f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 황금복덩이":
        embed=discord.Embed(color=0xff00, title="황금복덩이[풍10] (2등급)", description="획득방법 : 마쥬의 미로 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 6, 52', value = '성장률 : 공 2.18, 방 1.51, 순 1.26, 내구력 10.07 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717085712649945138/92d4baf24477a772.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 골드부비":
        embed=discord.Embed(color=0xff00, title="골드부비[화3/풍7] (2등급)", description="획득방법 : 퀴즈마스터 랜덤보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 11, 4, 55', value = '성장률 : 공 1.72, 방 2.25, 순 0.82, 내구력 11.06 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716909048917917716/91d6135d00e87876.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 얼룩부이비":
        embed=discord.Embed(color=0xff00, title="얼룩부이비[지10] (2등급)", description="획득방법 : 퀴즈마스터 랜덤보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 5, 50', value = '성장률 : 공 2.02, 방 1.42, 순 1.26, 내구력 11.25 (전체 4.70)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716909734124453938/63bc600f7b7dae2b.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 부비":
        embed=discord.Embed(color=0xff00, title="부비[지8/수2]", description="획득방법 : 사이너스 섬 (동608, 남208) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 4, 2, 38', value = '성장률 : 공 1.72, 방 1.53, 순 0.85, 내구력 13.26 (전체 4.10)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716911578234224751/29678ae9f23e8f54.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 부이":
        embed=discord.Embed(color=0xff00, title="부이[지6/수4]", description="획득방법 : 사이너스 섬 (동608, 남208) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 6, 3, 59', value = '성장률 : 공 1.77, 방 1.54, 순 0.77, 내구력 13.44 (전체 4.08)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716912038147915836/a0afaa35ea35805a.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 부이비":
        embed=discord.Embed(color=0xff00, title="부이비[수4/화6]", description="획득방법 : 쟈루 섬 (동357, 남183) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 4, 3, 35', value = '성장률 : 공 1.98, 방 1.42, 순 1.21, 내구력 11.56 (전체 4.61)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716912762013614180/7abb23f8562c03d5.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 꼬비오":
        embed=discord.Embed(color=0xff00, title="꼬비오[풍10]", description="획득방법 : 라토토 동굴 3층 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 5, 6, 36', value = '성장률 : 공 1.75, 방 1.52, 순 1.73, 내구력 9.76 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716915224309137470/acf642ac682169b3.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 꼬꼬비":
        embed=discord.Embed(color=0xff00, title="꼬꼬비[화3/풍7]", description="획득방법 : 라토토 동굴 3층 (동8, 남19) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 4, 4, 28', value = '성장률 : 공 1.75, 방 1.56, 순 1.58, 내구력 9.66 (전체 4.89)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716915745350483968/9ef16cdb48565635.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 꼬미":
        embed=discord.Embed(color=0xff00, title="꼬미[화6/풍4]", description="획득방법 : 라토토 복도 (동196, 남123) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 7, 6, 44', value = '성장률 : 공 1.81, 방 1.62, 순 1.47, 내구력 9.87 (전체 4.90)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716916296029175900/ba114504424f6d0f.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 꼬비":
        embed=discord.Embed(color=0xff00, title="꼬비[지5/풍5]", description="획득방법 : 라토토 복도 (동147, 남42) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 6, 7, 40', value = '성장률 : 공 1.71, 방 1.56, 순 1.74, 내구력 9.76 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716916705993031700/c9c61cd8227bc3be.gif")
        await message.channel.send(embed=embed)   
    if message.content == "!알려 우푸":
        embed=discord.Embed(color=0xff00, title="우푸[화6/풍4]", description="획득방법 : 쟈쟈마을 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 2, 6, 26', value = '성장률 : 공 1.77, 방 1.04, 순 2.16, 내구력 9.46 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716918506893082664/3effdd910409c1e2.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 푸푸":
        embed=discord.Embed(color=0xff00, title="푸푸[지3/풍7]", description="획득방법 : 쟈쟈마을 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 2, 5, 22', value = '성장률 : 공 1.72, 방 1.15, 순 2.16, 내구력 9.29 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716919315131269155/a47668c047d30884.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 투투":
        embed=discord.Embed(color=0xff00, title="투투[지3/수7]", description="획득방법 : 쟈루 섬 (동295, 남368) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 4, 7, 33', value = '성장률 : 공 1.65, 방 1.24, 순 2.14, 내구력 10.17 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716919818183508049/91630ea0b170098d.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 오투투":
        embed=discord.Embed(color=0xff00, title="오투투[지6/풍4]", description="획득방법 : 카루타나 마을 초기지원 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 5, 7, 35', value = '성장률 : 공 1.63, 방 1.47, 순 1.93, 내구력 9.29 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716920155782905876/676859bfad8d9472.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 베론":
        embed=discord.Embed(color=0xff00, title="베론[수10]", description="획득방법 : 쿠링으로 가는 길 1층 (동12, 남21) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 10, 4, 55', value = '성장률 : 공 1.39, 방 2.19, 순 1.01, 내구력 11.46 (전체 4.60)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716927399585120276/e1a65376db759984.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 베로로크":
        embed=discord.Embed(color=0xff00, title="베로로크[지7/수3]", description="획득방법 : 쿠링으로 가는 길 1층 (동9, 남12) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 8, 3, 44', value = '성장률 : 공 1.70, 방 2.09, 순 0.93, 내구력 11.09 (전체 4.72)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716990595351969862/4ae152cbfc6330c4.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 베로포리":
        embed=discord.Embed(color=0xff00, title="베로포리[수3/화7]", description="획득방법 : 속임수의 동굴(3) (동22, 남21) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 10, 4, 50', value = '성장률 : 공 1.34, 방 2.20, 순 1.02, 내구력 10.95 (전체 4.56)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716991116259623084/de32bba14b012714.gif")
        await message.channel.send(embed=embed)  
    if message.content == "!알려 베로보크":
        embed=discord.Embed(color=0xff00, title="베로보크[지3/수7]", description="획득방법 : 아름산의 동굴 지하 7층 (동42, 남21) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 9, 4, 51', value = '성장률 : 공 1.87, 방 2.04, 순 0.88, 내구력 10.62 (전체 4.80)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716992942820032542/04e11f98f4e87d91.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 노북이":
        embed=discord.Embed(color=0xff00, title="노북이[지3/풍7]", description="획득방법 : 사이너스 섬 (동545, 남389) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 6, 1, 24', value = '성장률 : 공 1.64, 방 2.44, 순 0.75, 내구력 9.57 (전체 4.82)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716994266135527455/17f385c5d37a022e.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 깡북이":
        embed=discord.Embed(color=0xff00, title="깡북이[화2/풍2]", description="획득방법 : 쿠오산 소동굴 3층 (동15, 남20) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 5, 1, 21', value = '성장률 : 공 1.84, 방 2.35, 순 0.60, 내구력 9.52 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716995475764674631/c52cb06ec99a1fca.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 북이":
        embed=discord.Embed(color=0xff00, title="북이[지6/풍4]", description="획득방법 : 사이너스 섬 (동570, 남416) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 6, 1, 23', value = '성장률 : 공 1.69, 방 2.49, 순 0.69, 내구력 9.41 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716996743371292742/da2b1b9170371237.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 돌북이":
        embed=discord.Embed(color=0xff00, title="돌북이[지9/풍1]", description="획득방법 : 쿠오산 소동굴 4층 (동23, 남38) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 10, 1, 38', value = '성장률 : 공 1.66, 방 2.75, 순 0.47, 내구력 9.63 (전체 4.88)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/716997922239283200/131071441b9adad4.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 자라북":
        embed=discord.Embed(color=0xff00, title="자라북[지4/수6]", description="획득방법 : 돌북이 포획지역 (요리-모듬 꼬치)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 7, 2, 32', value = '성장률 : 공 1.67, 방 2.48, 순 0.72, 내구력 10.57 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717443201958543480/4a00b401f5f3a989.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 아고아":
        embed=discord.Embed(color=0xff00, title="아고아[수3/화7]", description="획득방법 : 진홍의 동굴(나) 6층 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 5, 43', value = '성장률 : 공 2.21, 방 1.48, 순 1.20, 내구력 9.66 (전체 4.89)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717000287247663214/3ab632d111ce7331.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 네고스":
        embed=discord.Embed(color=0xff00, title="네고스[지4/수6]", description="획득방법 : 쟈루 섬 (동275, 남495) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 5, 48', value = '성장률 : 공 2.13, 방 1.50, 순 1.15, 내구력 10.78 (전체 4.78)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717004550095110154/a9bdf23627780248.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 보크곤":
        embed=discord.Embed(color=0xff00, title="보크곤[화2/풍8]", description="획득방법 : 몽환의 동굴(낮) 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 6, 41', value = '성장률 : 공 2.11, 방 1.36, 순 1.53, 내구력 9.52 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717057615867281539/38065f25a0942d7b.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 다고스":
        embed=discord.Embed(color=0xff00, title="다고스[수8/화2]", description="획득방법 : 사이너스 섬 (동186, 남153) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 7, 4, 45', value = '성장률 : 공 2.18, 방 1.65, 순 1.04, 내구력 10.24 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717058060165840976/75d9900a51376e99.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 타로곤":
        embed=discord.Embed(color=0xff00, title="타로곤[지7/풍3]", description="획득방법 : 사이너스 섬 (동186, 남153) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 7, 5, 45', value = '성장률 : 공 2.10, 방 1.59, 순 1.21, 내구력 9.86 (전체 4.90)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717058400785268757/ca071281bcf93c19.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 라고고":
        embed=discord.Embed(color=0xff00, title="라고고[화10]", description="획득방법 : 가우린 섬 (동461, 남523) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 6, 7, 43', value = '성장률 : 공 2.00, 방 1.49, 순 1.57, 내구력 9.81 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717058918815236186/73edae0ea4a6c70a.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 루니":
        embed=discord.Embed(color=0xff00, title="루니[지10]", description="획득방법 : 사이너스 섬 (동526, 남144) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 8, 5, 43', value = '성장률 : 공 1.78, 방 1.88, 순 1.36, 내구력 10.17 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717059176030797955/c7bf4970eaba429b.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 후바바":
        embed=discord.Embed(color=0xff00, title="후바바[화6/풍4]", description="획득방법 : 사이너스 섬 (동526, 남144) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 7, 7, 45', value = '성장률 : 공 1.86, 방 1.58, 순 1.62, 내구력 9.81 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717059511411539988/556f875499267797.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 토루루":
        embed=discord.Embed(color=0xff00, title="토루루[지6/풍4]", description="획득방법 : D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 6, 5, 38', value = '성장률 : 공 1.86, 방 1.73, 순 1.46, 내구력 9.97 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717059917521092778/a39860c43f333e77.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 라비루":
        embed=discord.Embed(color=0xff00, title="라비루[화10]", description="획득방법 : 라비루 레이드", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 8, 53', value = '성장률 : 공 2.18, 방 1.24, 순 1.64, 내구력 9.76 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717060243942539334/c6003678f5a30d18.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 푸루바":
        embed=discord.Embed(color=0xff00, title="푸루바[지7/풍3]", description="획득방법 : 라비루 레이드", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 8, 53', value = '성장률 : 공 2.07, 방 1.27, 순 1.66, 내구력 10.12 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717060612752146502/79551cd4eb2513a2.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 쿠로로":
        embed=discord.Embed(color=0xff00, title="쿠로로[지4/수6]", description="획득방법 : 초기지원 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 6, 7, 50', value = '성장률 : 공 1.80, 방 1.40, 순 1.56, 내구력 10.47 (전체 4.76)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717060902884474880/d43eda286f60c44c.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 기바바":
        embed=discord.Embed(color=0xff00, title="기바바[지8/수2]", description="획득방법 : 후바바 포획지역 (요리-생선꼬치)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 8, 5, 47', value = '성장률 : 공 2.01, 방 1.79, 순 1.21, 내구력 10.32 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728628875562582016/e69a5ca6e70fa4f3.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 카타르카스":
        embed=discord.Embed(color=0xff00, title="카타르카스[지10]", description="획득방법 : 동쿠링 광산 1층 (동30, 남45) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 11, 2, 44', value = '성장률 : 공 1.82, 방 2.61, 순 0.54, 내구력 10.33 (전체 4.98)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717061513134866583/19525460816aba29.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 쿠카스":
        embed=discord.Embed(color=0xff00, title="쿠카스[지8/수2]", description="획득방법 : 동쿠링 광산 2층 (동5, 남7) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 10, 2, 46', value = '성장률 : 공 1.73, 방 2.57, 순 0.54, 내구력 10.79 (전체 4.84)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717061848142184498/48205c436287692d.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 카르기안":
        embed=discord.Embed(color=0xff00, title="카르기안[지2/풍8]", description="획득방법 : 칠흑의 동굴 5층 (동13, 남56) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 9, 3, 40', value = '성장률 : 공 1.67, 방 2.41, 순 0.85, 내구력 10.48 (전체 4.93)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717063878881837076/0b949c3db9439cb7.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 쿠타스":
        embed=discord.Embed(color=0xff00, title="쿠타스[수6/화4]", description="획득방법 : 칠흑의 동굴 11층 (동56, 남38) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 9, 2, 47', value = '성장률 : 공 1.92, 방 2.25, 순 0.56, 내구력 10.94 (전체 4.73)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717064214513975316/958d4dc99fafdd23.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 로기안":
        embed=discord.Embed(color=0xff00, title="로기안[지8/풍2]", description="획득방법 : 유리의 동굴 11층 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 9, 1, 36', value = '성장률 : 공 1.81, 방 2.50, 순 0.49, 내구력 9.96 (전체 4.80)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717064544312098846/64cc5500fa528435.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 램가스":
        embed=discord.Embed(color=0xff00, title="램가스[지5/풍5]", description="획득방법 : D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 11, 2, 41', value = '성장률 : 공 1.85, 방 2.62, 순 0.46, 내구력 9.28 (전체 4.93)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717065227358699560/a5c28e5e7270ac5d.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 아이카스":
        embed=discord.Embed(color=0xff00, title="아이카스[지5/수5]", description="획득방법 : 칠흑의 동굴 9층 (동40, 남42) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 11, 2, 48', value = '성장률 : 공 1.73, 방 2.57, 순 0.54, 내구력 10.79 (전체 4.84)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717065735461011536/f7e4c03e37560957.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 코로카스":
        embed=discord.Embed(color=0xff00, title="코로카스[수4/화6]", description="획득방법 : 도둑의 동굴 지하 4층 (동15, 남4) 포획, A코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 8, 2, 36', value = '성장률 : 공 1.89, 방 2.33, 순 0.57, 내구력 10.12 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717066028303253584/bbea63346927495f.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 리비노":
        embed=discord.Embed(color=0xff00, title="리비노[지10]", description="획득방법 : 유리의 동굴 13층 (동29, 남19) 포획, 오형제의 시험", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 7, 4, 46', value = '성장률 : 공 2.28, 방 1.51, 순 1.02, 내구력 10.09 (전체 4.82)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717066655850561567/b3695eb9f98548fe.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 반보로":
        embed=discord.Embed(color=0xff00, title="반보로[화5/풍5]", description="획득방법 : 가우린 섬 (동397, 남275) 포획, 오형제의 시험", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 6, 55', value = '성장률 : 공 2.37, 방 1.43, 순 1.26, 내구력 10.17 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717067005177364902/7022bceeda2ff974.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 얀기로":
        embed=discord.Embed(color=0xff00, title="얀기로[수3/화7]", description="획득방법 : 가우린 섬 (동526, 남101) 포획, 오형제의 시험", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 13, 8, 7, 61', value = '성장률 : 공 2.32, 방 1.43, 순 1.21, 내구력 10.47 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717067400683454504/6abe827e5b1d32d4.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 반기노":
        embed=discord.Embed(color=0xff00, title="반기노[화10]", description="획득방법 : 가우린 섬 (동441, 남104) 포획, 오형제의 시험", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 6, 52', value = '성장률 : 공 2.41, 방 1.43, 순 1.21, 내구력 9.97 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717067716313481266/37955d6e628c5add.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 부르돈":
        embed=discord.Embed(color=0xff00, title="부르돈[화2/풍8]", description="획득방법 : 가우린 섬 (동410, 남354) 포획, 오형제의 시험", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 7, 51', value = '성장률 : 공 2.26, 방 1.33, 순 1.41, 내구력 10.12 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717068101010587718/6ffe3a213e1cee32.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 프로돈":
        embed=discord.Embed(color=0xff00, title="프로돈[지2/수8]", description="획득방법 : 얀기로 포획지역 (요리-푸짐한 고기세트)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 13, 8, 6, 61', value = '성장률 : 공 2.31, 방 1.58, 순 1.16, 내구력 10.85 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717068690130206771/5e4eeac6b9962820.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 쿠링":
        embed=discord.Embed(color=0xff00, title="쿠링[지6/수4]", description="획득방법 : 카루타나 마을 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 5, 5, 31', value = '성장률 : 공 1.65, 방 1.75, 순 1.52, 내구력 9.63 (전체 4.92)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717069271917789294/2019082928c90e35.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 쿠쿠르":
        embed=discord.Embed(color=0xff00, title="쿠쿠르[수7/화3]", description="획득방법 : 쟈쟈마을 초기지원 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 5, 5, 36', value = '성장률 : 공 1.66, 방 1.61, 순 1.64, 내구력 10.07 (전체 4.90)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717069772172427294/10486c0792db73d4.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 포링":
        embed=discord.Embed(color=0xff00, title="포링[수4/화6]", description="획득방법 : 쟈루 섬 (동478, 남319) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 5, 5, 30', value = '성장률 : 공 1.65, 방 1.65, 순 1.64, 내구력 9.46 (전체 4.94)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717069995221319731/2e5476e0752ecc3f.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 리스키":
        embed=discord.Embed(color=0xff00, title="리스키[지2/수8]", description="획득방법 : 카루타나 마을 앞마당 포획, C코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 5, 4, 31', value = '성장률 : 공 1.56, 방 1.71, 순 1.58, 내구력 10.24 (전체 4.85)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717070760962687116/09c0fb5c926ef5cb.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 초코링":
        embed=discord.Embed(color=0xff00, title="초코링[지7/풍3]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 7, 48', value = '성장률 : 공 2.14, 방 1.30, 순 1.47, 내구력 10.07 (전체 4.91)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721982962287247430/ac6bba4fb37b2c87.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 신하트링":
        embed=discord.Embed(color=0xff00, title="(新)하트링[화4/풍6]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 9, 53', value = '성장률 : 공 2.13, 방 1.19, 순 1.69, 내구력 9.71 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721982997141913680/1569a4a7ee8f3c26.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 골드카비트":
        embed=discord.Embed(color=0xff00, title="골드카비트[풍10]", description="획득방법 : 샴기르 마을 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 5, 5, 28', value = '성장률 : 공 1.67, 방 1.56, 순 1.75, 내구력 8.60 (전체 4.99)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717071168502366278/d44a8f1dd198bc6f.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 큐이":
        embed=discord.Embed(color=0xff00, title="큐이[화5/풍5]", description="획득방법 : 샴기르 마을 앞마당 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 5, 5, 28', value = '성장률 : 공 1.72, 방 1.52, 순 1.70, 내구력 8.77 (전체 4.94)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717071493606932500/7cc9fd61d76cbdb8.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 케이비":
        embed=discord.Embed(color=0xff00, title="케이비[지2/풍8]", description="획득방법 : 마리너스 마을 초기지원 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 5, 5, 30', value = '성장률 : 공 1.80, 방 1.65, 순 1.64, 내구력 8.96 (전체 5.08)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717071754035724389/992e04cea382e9e4.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 카비트":
        embed=discord.Embed(color=0xff00, title="카비트[화7/풍3]", description="획득방법 : 사이너스 섬 (동304, 남328) 포획, 쿠오산 박사(루니) 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 5, 5, 29', value = '성장률 : 공 1.69, 방 1.69, 순 1.75, 내구력 8.94 (전체 5.13)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717072041093627934/011815ddfe4e01d5.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 고르돈":
        embed=discord.Embed(color=0xff00, title="고르돈[지10]", description="획득방법 : 가우린 섬 (동166, 남356) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 8, 4, 46', value = '성장률 : 공 2.02, 방 1.88, 순 1.00, 내구력 10.07 (전체 4.91)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717072672344899594/739b341e2bc1cb81.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 기라돈":
        embed=discord.Embed(color=0xff00, title="기라돈[지8/수2]", description="획득방법 : 폐허가 된 탄광 4층 (동45, 남27) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 9, 5, 50', value = '성장률 : 공 1.91, 방 1.91, 순 1.07, 내구력 10.33 (전체 4.88)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717072966751617074/bf04f90ca5b78ca9.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 고르고":
        embed=discord.Embed(color=0xff00, title="고르고[화9/풍1]", description="획득방법 : 폐허가 된 탄광 4층 (동45, 남27) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 8, 6, 51', value = '성장률 : 공 2.12, 방 1.59, 순 1.26, 내구력 9.53 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717073513353314465/695341c9d2e331a6.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 투르돈":
        embed=discord.Embed(color=0xff00, title="투르돈[수3/화7]", description="획득방법 : 가우린 섬 (동237, 남80)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 7, 5, 50', value = '성장률 : 공 2.01, 방 1.66, 순 1.21, 내구력 10.77 (전체 4.88)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717073762113290320/d42f8ff67d6d7271.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 철기돈":
        embed=discord.Embed(color=0xff00, title="철기돈[지7/수3]", description="획득방법 : 고르돈 포획지역 (요리-야채볶음)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 8, 6, 51', value = '성장률 : 공 2.12, 방 1.69, 순 1.21, 내구력 10.09 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717472428065947648/b51368cfa66b16e2.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 킹고르":
        embed=discord.Embed(color=0xff00, title="킹고르[지1/수9]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 9, 5, 60', value = '성장률 : 공 2.23, 방 1.67, 순 1.02, 내구력 11.09 (전체 4.90)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721984935409483887/2ad64c50c5e77ea1.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 고루바":
        embed=discord.Embed(color=0xff00, title="고루바[지6/풍4]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 11, 6, 56', value = '성장률 : 공 1.92, 방 2.05, 순 1.12, 내구력 10.33 (전체 5.09)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721989532836167720/1378b328438005ae.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 가론고르":
        embed=discord.Embed(color=0xff00, title="가론고르[수2/화8]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 8, 6, 53', value = '성장률 : 공 2.20, 방 1.64, 순 1.12, 내구력 9.86 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721992698852278282/672ae7efc1d428ab.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 쿠보":
        embed=discord.Embed(color=0xff00, title="쿠보[수5/화5] (2등급)", description="획득방법 : 쿠오산 박사(베르가) 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 9, 5, 51', value = '성장률 : 공 1.86, 방 1.86, 순 1.06, 내구력 10.12 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717074398481219645/c5028bfa7ea0eef1.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 휴보":
        embed=discord.Embed(color=0xff00, title="휴보[지8/수2] (2등급)", description="획득방법 : 카난 퀘스트 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 6, 3, 36', value = '성장률 : 공 1.96, 방 1.82, 순 1.01, 내구력 10.12 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717074746696532028/22a4cbbf44eca85f.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 포보":
        embed=discord.Embed(color=0xff00, title="푸보[지3/수7]", description="획득방법 : 고야산 동굴 4층 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 7, 3, 39', value = '성장률 : 공 1.89, 방 1.94, 순 0.95, 내구력 10.74 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717085298638454794/38c6c00502ac84af.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 토로쟈":
        embed=discord.Embed(color=0xff00, title="토로쟈[수3/화7]", description="획득방법 : 속임수 동굴 최하층 입구 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 7, 4, 41', value = '성장률 : 공 1.93, 방 1.88, 순 1.06, 내구력 10.22 (전체 4.86)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717086173067214939/8c617c4465be1e19.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 부르보":
        embed=discord.Embed(color=0xff00, title="부르보[화4/풍6]", description="획득방법 : 페트와 이야기 하고 싶어 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 7, 4, 38', value = '성장률 : 공 1.87, 방 1.82, 순 1.26, 내구력 9.91 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717086556107833406/90970434a308e407.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카쿠":
        embed=discord.Embed(color=0xff00, title="카쿠[지3/수7]", description="획득방법 : 쟈루 섬 (동81, 남1140) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 6, 5, 35', value = '성장률 : 공 1.77, 방 1.77, 순 1.42, 내구력 9.92 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717098050455208056/92eaedca1c23e19a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 바우":
        embed=discord.Embed(color=0xff00, title="바우[지2/풍8]", description="획득방법 : 숲의 동굴 2층 (동27, 남32) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 4, 5, 27', value = '성장률 : 공 1.85, 방 1.60, 순 1.75, 내구력 8.85 (전체 5.19)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717098498117337229/8c4c811d2f3718be.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 바카":
        embed=discord.Embed(color=0xff00, title="바카[화4/풍6]", description="획득방법 : 쟈루 섬 (동90, 남1090) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 5, 6, 32', value = '성장률 : 공 1.99, 방 1.56, 순 1.69, 내구력 8.75 (전체 5.24)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717098760227913789/cfdb7293a606ff0f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카우":
        embed=discord.Embed(color=0xff00, title="카우[지7/풍3]", description="획득방법 : 숲의 동굴 4층 (동14, 남8) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 6, 4, 32', value = '성장률 : 공 1.80, 방 1.75, 순 1.41, 내구력 9.23 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717099086615937124/46c659a7910f4b06.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 노르노르":
        embed=discord.Embed(color=0xff00, title="노르노르[지3/풍7] (2등급)", description="획득방법 : 복권 1등 페트 (마리너스)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 7, 45', value = '성장률 : 공 2.09, 방 1.32, 순 1.64, 내구력 9.76 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717099866454753331/b772b357feab4973.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 도르도르":
        embed=discord.Embed(color=0xff00, title="도르도르[지3/수7]", description="획득방법 : 고루루 레이드 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 7, 47', value = '성장률 : 공 2.12, 방 1.23, 순 1.61, 내구력 10.27 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717100150723444869/5ae5628f38329189.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 고루루":
        embed=discord.Embed(color=0xff00, title="고루루[수5/화5]", description="획득방법 : 고루루 레이드 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 8, 49', value = '성장률 : 공 2.16, 방 1.22, 순 1.66, 내구력 9.78 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717100554483925072/2d2421ccd8662c42.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 고르고르":
        embed=discord.Embed(color=0xff00, title="고르고르[화8/풍2]", description="획득방법 : 가우린 섬 (동225, 남353) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 5, 6, 38', value = '성장률 : 공 2.12, 방 1.24, 순 1.67, 내구력 9.40 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717100873548824706/8b1e51a68a24032d.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 베루루":
        embed=discord.Embed(color=0xff00, title="베루루[화3/풍7]", description="획득방법 : 쟈루 섬 (동357, 남680) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 7, 42', value = '성장률 : 공 2.08, 방 1.29, 순 1.67, 내구력 9.61 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717101188004315156/0392b65584ffeff5.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 베르가":
        embed=discord.Embed(color=0xff00, title="베르가[지9/수1]", description="획득방법 : 쟈루 섬 (동467, 남630) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 7, 46', value = '성장률 : 공 2.00, 방 1.44, 순 1.52, 내구력 9.91 (전체 4.96)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717101194673258637/828b373ca08def1f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 베라라":
        embed=discord.Embed(color=0xff00, title="베라라[화4/풍6]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 7, 46', value = '성장률 : 공 2.07, 방 1.40, 순 1.61, 내구력 9.63 (전체 5.08)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721992305254334564/c16bd888bae1c1bf.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 설표":
        embed=discord.Embed(color=0xff00, title="설표[지9/풍1]", description="획득방법 : 베루루 포획지역 (요리-푸짐한 고기세트)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 7, 45', value = '성장률 : 공 2.09, 방 1.28, 순 1.64, 내구력 9.90 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717101211718778961/12ba3a93216039cc.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 어린설표":
        embed=discord.Embed(color=0xff00, title="어린설표[지9/풍1]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 7, 45', value = '성장률 : 공 2.09, 방 1.28, 순 1.64, 내구력 9.90 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721984358038110269/408fc5377425d821.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 레오딘":
        embed=discord.Embed(color=0xff00, title="레오딘[지8/수2]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 8, 7, 56', value = '성장률 : 공 2.15, 방 1.47, 순 1.40, 내구력 10.28 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721996492084346960/d43c22daafa6548c.gif")
        await message.channel.send(embed=embed) 
    if message.content == "!알려 펜타스":
        embed=discord.Embed(color=0xff00, title="펜타스[지2/수8]", description="획득방법 : 마리너스 마을 근처 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 6, 2, 33', value = '성장률 : 공 1.66, 방 2.19, 순 0.83, 내구력 11.10 (전체 4.68)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717102423180836914/d07d5572e1fc5c56.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 토리케라":
        embed=discord.Embed(color=0xff00, title="토리케라[지7/수3]", description="획득방법 : 마리너스 마을 근처 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 6, 2, 35', value = '성장률 : 공 1.70, 방 2.15, 순 0.81, 내구력 10.91 (전체 4.65)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717102427937177651/32118b33e7bc7a6d.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 토리노프스":
        embed=discord.Embed(color=0xff00, title="토리노프스[지7/수3]", description="획득방법 : 쟈루 섬 (동467, 남393) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 4, 2, 25', value = '성장률 : 공 1.75, 방 2.03, 순 0.88, 내구력 10.67 (전체 4.66)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717102432789987328/ab1f34dde0d0f7fe.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 토르프스":
        embed=discord.Embed(color=0xff00, title="토르프스[지10]", description="획득방법 : A코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 4, 5, 1, 29', value = '성장률 : 공 1.80, 방 2.21, 순 0.69, 내구력 10.74 (전체 4.70)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717102437374361710/ba3469498282fdb1.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 코발스":
        embed=discord.Embed(color=0xff00, title="코발스[수10]", description="획득방법 : 펜타스 포획지역 (요리-생선꼬치)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 8, 3, 50', value = '성장률 : 공 1.94, 방 1.98, 순 0.74, 내구력 11.95 (전체 4.66)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728628857447514122/de58156e9ec9fa3a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 고반케스":
        embed=discord.Embed(color=0xff00, title="고반케스[지4/수6]", description="획득방법 : 카루타나 마을 부근의 해변가 (동231, 남557) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 5, 3, 37', value = '성장률 : 공 2.08, 방 1.56, 순 1.04, 내구력 11.10 (전체 4.68)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717279244102795264/d62829b92df6ef66.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 쟈그라":
        embed=discord.Embed(color=0xff00, title="쟈그라[수5/화5]", description="획득방법 : 쿠오해저터널 1층 쿠오방향 (동20, 남35) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 5, 4, 43', value = '성장률 : 공 2.17, 방 1.35, 순 1.15, 내구력 10.67 (전체 4.66)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717279230848663562/62af259fac9a08d3.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 쟈그":
        embed=discord.Embed(color=0xff00, title="쟈그[수10]", description="획득방법 : 쿠오해저터널 1층 쟈루방향 (동10, 남25) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 5, 4, 49', value = '성장률 : 공 2.08, 방 1.36, 순 1.10, 내구력 11.58 (전체 4.54)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717279217464639538/2e2819b9bf743022.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 판지":
        embed=discord.Embed(color=0xff00, title="판지[지2/수8]", description="획득방법 : 쟈루 섬 (동157, 남704) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 4, 2, 31', value = '성장률 : 공 2.03, 방 1.48, 순 1.03, 내구력 11.02 (전체 4.54)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717279164994027550/401042db1b5d911d.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 쟈하드":
        embed=discord.Embed(color=0xff00, title="쟈하드[화2/풍8]", description="획득방법 : 쟈그 포획지역 (요리-모듬 꼬치)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 6, 47', value = '성장률 : 공 2.28, 방 1.34, 순 1.35, 내구력 10.24 (전체 4.98)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717465704349302845/9343cbc2b22bc159.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 판그라":
        embed=discord.Embed(color=0xff00, title="판그라[수2/화8]", description="획득방법 : 쟈그라 포획지역 (요리-모듬 꼬치)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 4, 46', value = '성장률 : 공 2.25, 방 1.40, 순 1.07, 내구력 11.09 (전체 4.72)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717465742232256563/36c181789daa2319.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 돌가로스":
        embed=discord.Embed(color=0xff00, title="돌가로스[지10]", description="획득방법 : D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 11, 2, 63', value = '성장률 : 공 2.17, 방 2.13, 순 0.45, 내구력 11.66 (전체 4.75)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717281204482605066/3d427d2749b78494.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 가가로스":
        embed=discord.Embed(color=0xff00, title="가가로스[수2/화8]", description="획득방법 : 리푸 섬 (동35, 남130) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 11, 4, 58', value = '성장률 : 공 2.15, 방 2.02, 순 0.78, 내구력 10.76 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717281214498865162/0a5e289a0b1fe01a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 기가로스":
        embed=discord.Embed(color=0xff00, title="기가로스[지3/풍7]", description="획득방법 : 리푸 섬 (동35, 남130) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 11, 6, 61', value = '성장률 : 공 2.01, 방 1.96, 순 1.07, 내구력 10.47 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717281219880026162/f511b4d0156a8fc4.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 비트로스":
        embed=discord.Embed(color=0xff00, title="비트로스[화3/풍7]", description="획득방법 : 아스마르 광산 6층 (동6, 남6) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 10, 4, 54', value = '성장률 : 공 2.13, 방 1.92, 순 0.88, 내구력 10.38 (전체 4.93)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717281244450390018/da60a28970de1cb6.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 메가로스":
        embed=discord.Embed(color=0xff00, title="메가로스[지4/수6]", description="획득방법 : 환생 보상 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 9, 3, 57', value = '성장률 : 공 2.02, 방 1.98, 순 0.74, 내구력 11.28 (전체 4.73)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717281276922429460/390148c4b15adff3.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 무이":
        embed=discord.Embed(color=0xff00, title="무이[수10]", description="획득방법 : 쿠르의 해저통로 (동47, 남32) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 8, 2, 48', value = '성장률 : 공 1.91, 방 2.00, 순 0.57, 내구력 12.10 (전체 4.48)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717285422451130368/31559f8a573b724f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 씨보스":
        embed=discord.Embed(color=0xff00, title="씨보스[지2/수8]", description="획득방법 : 쿠르의 해저통로 (동47, 남32) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 8, 2, 48', value = '성장률 : 공 1.71, 방 2.03, 순 0.92, 내구력 11.51 (전체 4.66)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717285410539307058/9e30a7e59dcfbcef.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 루이":
        embed=discord.Embed(color=0xff00, title="루이[수8/화2]", description="획득방법 : 벽청의 지하동굴[나] 8층 (동19, 남13) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 8, 3, 49', value = '성장률 : 공 1.86, 방 2.00, 순 0.75, 내구력 11.56 (전체 4.61)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717285489689886761/cd85c570356e2d65.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 투이":
        embed=discord.Embed(color=0xff00, title="투이[수5/화5]", description="획득방법 : 환생 보상 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 8, 3, 52', value = '성장률 : 공 1.79, 방 1.84, 순 0.75, 내구력 11.36 (전체 4.38)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717285395737477190/9cc56138f12d350d.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 다이노스":
        embed=discord.Embed(color=0xff00, title="다이노스[지3/수7]", description="획득방법 : 칠흑의 동굴 18층 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 11, 2, 66', value = '성장률 : 공 1.86, 방 2.12, 순 0.50, 내구력 12.14 (전체 4.41)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717286833960124496/93dc279e1ed5c183.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 다이노":
        embed=discord.Embed(color=0xff00, title="다이노[지9/수1]", description="획득방법 : C코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 11, 2, 61', value = '성장률 : 공 2.03, 방 2.16, 순 0.40, 내구력 11.71 (전체 4.60)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717286840016699492/668cf5ea1a1fe73e.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 프라키토스":
        embed=discord.Embed(color=0xff00, title="프라키토스[수2/화8]", description="획득방법 : 세르노스 섬 전역 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 9, 2, 57', value = '성장률 : 공 2.24, 방 1.94, 순 0.50, 내구력 11.42 (전체 4.69)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717286861055197234/31b5348896e3acff.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 프리토스":
        embed=discord.Embed(color=0xff00, title="프리토스[화2/풍8] (2등급)", description="획득방법 : 현재 획득 불가", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 11, 3, 69', value = '성장률 : 공 2.08, 방 1.99, 순 0.64, 내구력 11.80 (전체 4.71)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717286868802207814/5926de089de50aef.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 스텐토스":
        embed=discord.Embed(color=0xff00, title="스텐토스[지5/수5]", description="획득방법 : D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 13, 3, 72', value = '성장률 : 공 1.87, 방 2.21, 순 0.55, 내구력 12.38 (전체 4.63)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717286923395268629/ea06cc4834aa9711.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 화이토스":
        embed=discord.Embed(color=0xff00, title="화이토스[지2/수8]", description="획득방법 : 이벤트 상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 12, 2, 67', value = '성장률 : 공 2.13, 방 2.13, 순 0.45, 내구력 11.80 (전체 4.71)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/724954287951577179/124999-13.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 만모로스":
        embed=discord.Embed(color=0xff00, title="만모로스[수5/화5]", description="획득방법 : 가우린 섬 (동110, 남128), (동104, 남153) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 11, 2, 70', value = '성장률 : 공 1.75, 방 2.18, 순 0.45, 내구력 13.32 (전체 4.38)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717290940808560710/46947864ec526041.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 마모나스":
        embed=discord.Embed(color=0xff00, title="마모나스[지7/수3]", description="획득방법 : 가우린 섬 (동113, 남47) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 11, 3, 71', value = '성장률 : 공 1.61, 방 2.08, 순 0.69, 내구력 13.13 (전체 4.37)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717290946219343993/6ccefbd79d3fee80.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 만모":
        embed=discord.Embed(color=0xff00, title="만모[지9/수1]", description="획득방법 : 가우린 채석장 3층 (동21, 남15) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 12, 2, 73', value = '성장률 : 공 1.69, 방 2.12, 순 0.45, 내구력 12.85 (전체 4.26)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717290952833630218/a6ffbfd85b0da751.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 만모르":
        embed=discord.Embed(color=0xff00, title="만모르[수2/화8]", description="획득방법 : 가우린 채석장 5층 (동25, 남26) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 10, 2, 63', value = '성장률 : 공 2.00, 방 2.04, 순 0.40, 내구력 12.47 (전체 4.44)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717290978930851890/b34df3e6ceec3444.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 푸모나스":
        embed=discord.Embed(color=0xff00, title="푸모나스[지2/수8]", description="획득방법 : 만모 포획지역 (요리-야채볶음)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 9, 1, 67', value = '성장률 : 공 1.94, 방 2.02, 순 0.40, 내구력 14.04 (전체 4.37)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717291052544819270/2c8221b8e725b3ff.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 테라곤":
        embed=discord.Embed(color=0xff00, title="테라곤[화2/풍8]", description="획득방법 : C코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 9, 53', value = '성장률 : 공 2.02, 방 1.31, 순 1.71, 내구력 9.78 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717295297415479306/55172c53436caf58.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카르곤":
        embed=discord.Embed(color=0xff00, title="카르곤[화8/풍2]", description="획득방법 : 환생 보상 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 5, 8, 49', value = '성장률 : 공 2.13, 방 1.16, 순 1.78, 내구력 9.81 (전체 5.07)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717295364465492030/5b0ddfcf8eab21e3.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 포이비스":
        embed=discord.Embed(color=0xff00, title="포이비스[지5/풍5]", description="획득방법 : 비룡의 동굴 (동36, 남15) 포획, D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 8, 50', value = '성장률 : 공 2.01, 방 1.32, 순 1.64, 내구력 10.05 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717295389832773682/872d3ca16c3d410e.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 도라비스":
        embed=discord.Embed(color=0xff00, title="도라비스[풍10]", description="획득방법 : 황금색 페트 카난 퀘스트 보상(반복)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 9, 51', value = '성장률 : 공 2.00, 방 1.27, 순 1.78, 내구력 9.76 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717295603779895337/d318d692de14ab03.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 보르비스":
        embed=discord.Embed(color=0xff00, title="보르비스[지3/수7]", description="획득방법 : B코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 8, 52', value = '성장률 : 공 1.97, 방 1.33, 순 1.73, 내구력 10.47 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717295668519239732/72e2e7c7635c4275.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 하라비스":
        embed=discord.Embed(color=0xff00, title="하라비스[수8/화2]", description="획득방법 : 이벤트 상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 8, 53', value = '성장률 : 공 2.12, 방 1.23, 순 1.71, 내구력 10.17 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/724954388543832104/128000-11.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카키":
        embed=discord.Embed(color=0xff00, title="카키[화8/풍2]", description="획득방법 : 사이너스 섬 (동608, 남206) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 4, 7, 33', value = '성장률 : 공 1.84, 방 1.24, 순 2.08, 내구력 9.24 (전체 5.15)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717297517590609950/20893e311f9502ae.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 호르쿠":
        embed=discord.Embed(color=0xff00, title="호르쿠[지3/풍7]", description="획득방법 : 쟈루 섬 (동668, 남651) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 4, 6, 31', value = '성장률 : 공 1.58, 방 1.23, 순 2.08, 내구력 9.69 (전체 4.94)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717297529154175006/7be4325fdfa2f8b5.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 흑카키":
        embed=discord.Embed(color=0xff00, title="흑카키[지6/풍4]", description="획득방법 : C코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 4, 8, 36', value = '성장률 : 공 1.79, 방 1.28, 순 2.09, 내구력 9.50 (전체 5.15)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717297537517748264/c264427cdb4ce4ea.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 타키":
        embed=discord.Embed(color=0xff00, title="타키[화3/풍7]", description="획득방법 : 사이너스 섬 (동549, 남146) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 5, 3, 6, 28', value = '성장률 : 공 1.73, 방 1.12, 순 2.08, 내구력 9.46 (전체 4.93)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717297566642995221/ef5fafba372968d4.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 쿠쿠":
        embed=discord.Embed(color=0xff00, title="쿠쿠[풍10]", description="획득방법 : 쟈루 섬 (동669, 남652) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 4, 7, 34', value = '성장률 : 공 1.72, 방 1.14, 순 2.11, 내구력 9.12 (전체 4.98)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717297588512227418/c0c5be407267a459.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 쥬키":
        embed=discord.Embed(color=0xff00, title="쥬키[화5/풍5]", description="획득방법 : 쿠쿠 포획지역 (요리-생선꼬치)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 4, 8, 35', value = '성장률 : 공 1.86, 방 1.19, 순 2.10, 내구력 9.13 (전체 5.15)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728628897159184514/a79ff1074cd8a59a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 오가로스":
        embed=discord.Embed(color=0xff00, title="오가로스[지8/수2]", description="획득방법 : 아스마르 광산 6층 (동37, 남38) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 9, 6, 56', value = '성장률 : 공 2.12, 방 1.74, 순 1.16, 내구력 10.28 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717299909468094504/1e47bfda828b7a61.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 모가로스":
        embed=discord.Embed(color=0xff00, title="모가로스[수2/화8]", description="획득방법 : 퀴즈 마스터 (골드부비) 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 13, 8, 7, 55', value = '성장률 : 공 2.29, 방 1.56, 순 1.40, 내구력 9.76 (전체 5.25)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717299897786695720/0c7bed576abad617.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 오르곤":
        embed=discord.Embed(color=0xff00, title="오르곤[수8/화2]", description="획득방법 : 퀴즈 마스터 (얼룩부이비) 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 7, 53', value = '성장률 : 공 2.21, 방 1.53, 순 1.40, 내구력 10.57 (전체 5.14)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717299914241081394/10f19e5834fca11c.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 골로스":
        embed=discord.Embed(color=0xff00, title="골로스[화5/풍5] (1등급)", description="획득방법 : 환생 보상 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 13, 10, 7, 59', value = '성장률 : 공 2.23, 방 1.70, 순 1.21, 내구력 9.88 (전체 5.15)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717299886420131940/492216d2ce971abd.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 노르곤":
        embed=discord.Embed(color=0xff00, title="노르곤[화1/풍9] (2등급)", description="획득방법 : 복권 1등 페트 (쟈쟈)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 13, 9, 7, 60', value = '성장률 : 공 2.22, 방 1.51, 순 1.31, 내구력 9.97 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717299942770868224/2a365b161197dc60.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 알테로스":
        embed=discord.Embed(color=0xff00, title="알테로스[지1/수9] (2등급)", description="획득방법 : 부의 부탁 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 9, 56', value = '성장률 : 공 2.08, 방 1.28, 순 1.66, 내구력 10.32 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717300010588569710/f573f939059a5458.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 곤룡":
        embed=discord.Embed(color=0xff00, title="곤룡[지2/풍8]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 7, 53', value = '성장률 : 공 2.20, 방 1.43, 순 1.45, 내구력 10.14 (전체 5.07)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/718382108514582598/80fec59220f5d6e2.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 푸룡":
        embed=discord.Embed(color=0xff00, title="푸룡[수7/화3]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 8, 6, 57', value = '성장률 : 공 2.25, 방 1.57, 순 1.21, 내구력 10.47 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721990699330961488/8a3ce3016b94cead.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 지가로스":
        embed=discord.Embed(color=0xff00, title="지가로스[지7/수3]", description="획득방법 : 빛나는 보물상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 8, 7, 55', value = '성장률 : 공 2.16, 방 1.56, 순 1.40, 내구력 10.19 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721992747946606643/c8d52e90edc32125.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 흑귀":
        embed=discord.Embed(color=0xff00, title="흑귀[지6/풍4]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 8, 6, 56', value = '성장률 : 공 2.21, 방 1.56, 순 1.26, 내구력 10.28 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721996262374899752/ab5a28312d9a72c8.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 바로스":
        embed=discord.Embed(color=0xff00, title="바로스[풍7/지3]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 7, 52', value = '성장률 : 공 2.21, 방 1.32, 순 1.51, 내구력 9.97 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721996342712598538/9ffc21b92c0e71b6.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카르노스":
        embed=discord.Embed(color=0xff00, title="카르노스[지6/풍4]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 8, 7, 56', value = '성장률 : 공 2.19, 방 1.47, 순 1.40, 내구력 9.95 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721991180543328296/407b8b3fae73e9ec.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 라나프":
        embed=discord.Embed(color=0xff00, title="라나프[화2/풍2] (2등급)", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 9, 9, 51', value = '성장률 : 공 1.84, 방 1.76, 순 1.66, 내구력 9.03 (전체 5.26)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717302577838161950/162702c4c4dff0aa.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 라이혼":
        embed=discord.Embed(color=0xff00, title="라이혼[지5/수5] (1등급)", description="획득방법 : 미출현", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 10, 10, 57', value = '성장률 : 공 1.74, 방 1.74, 순 1.64, 내구력 9.10 (전체 5.12)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717302584087543828/45a39019e5da0c5f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 프이토":
        embed=discord.Embed(color=0xff00, title="프이토[지2/풍8] (2등급)", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 9, 8, 47', value = '성장률 : 공 1.66, 방 1.79, 순 1.66, 내구력 9.08 (전체 5.11)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717302603679268894/8e9b89665a8552b6.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 타이혼":
        embed=discord.Embed(color=0xff00, title="타이혼[화5/풍5] (1등급)", description="획득방법 : 부의 부탁 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 9, 10, 57', value = '성장률 : 공 1.86, 방 1.52, 순 1.73, 내구력 9.10 (전체 5.12)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717302824689598525/eac1e1719b2b6841.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 모나시프":
        embed=discord.Embed(color=0xff00, title="모나시프[풍10] (2등급)", description="획득방법 : 채석장의 비밀 퀘스트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 8, 8, 49', value = '성장률 : 공 1.72, 방 1.76, 순 1.61, 내구력 9.83 (전체 5.09)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717302889231417444/05ca59367a719c4d.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 다이노로스":
        embed=discord.Embed(color=0xff00, title="다이노로스[수5/화5]", description="획득방법 : A코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 8, 6, 56', value = '성장률 : 공 1.73, 방 1.73, 순 1.31, 내구력 11.14 (전체 4.77)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717311272156266506/2ecc5d762f283da5.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 타르노로스":
        embed=discord.Embed(color=0xff00, title="타르노로스[수7/화3]", description="획득방법 : 칠흑의 동굴 19층 (동34, 남25) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 8, 6, 54', value = '성장률 : 공 1.82, 방 1.70, 순 1.26, 내구력 11.33 (전체 4.78)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717311298119139328/c806df11f4670548.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 아토라지":
        embed=discord.Embed(color=0xff00, title="아토라지[수10]", description="획득방법 : C코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 8, 5, 49', value = '성장률 : 공 1.62, 방 1.97, 순 1.21, 내구력 11.71 (전체 4.80)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717311344927572018/32fe7f41f83633ee.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 스토라지":
        embed=discord.Embed(color=0xff00, title="스토라지[지2/수8]", description="획득방법 : D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 8, 4, 50', value = '성장률 : 공 1.79, 방 1.88, 순 1.12, 내구력 11.33 (전체 4.78)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717311351667818506/b9bf61fdaa2ee7cf.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 아리노스":
        embed=discord.Embed(color=0xff00, title="아리노스[지5/수5]", description="획득방법 : B코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 9, 6, 57', value = '성장률 : 공 1.94, 방 1.69, 순 1.26, 내구력 10.52 (전체 4.89)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717311503019147314/d05a736358d87e0b.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 코리토르스":
        embed=discord.Embed(color=0xff00, title="코리토르스[지7/수3]", description="획득방법 : 고야산 동굴 5층 전역 포획,B코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 5, 5, 36', value = '성장률 : 공 1.77, 방 1.68, 순 1.42, 내구력 10.24 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717313457078403182/f356f7ccf4c5e320.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 바로로크스":
        embed=discord.Embed(color=0xff00, title="바로로크스[지4/수6]", description="획득방법 : 사이너스 섬 (동382, 남479) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 6, 7, 5, 42', value = '성장률 : 공 1.68, 방 1.93, 순 1.26, 내구력 10.24 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717313474329575424/3fae278bcf78a90d.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 란베르스":
        embed=discord.Embed(color=0xff00, title="란베르스[수7/화3]", description="획득방법 : 도둑의 동굴 지하 2층 (동42, 남9) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 6, 5, 42', value = '성장률 : 공 1.77, 방 1.68, 순 1.36, 내구력 10.33 (전체 4.82)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717313509033115769/90aa8541cba8112e.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 노스토로스":
        embed=discord.Embed(color=0xff00, title="노스토로스[화9/풍1]", description="획득방법 : 미출현", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 7, 6, 5, 42', value = '성장률 : 공 1.77, 방 1.68, 순 1.36, 내구력 10.33 (전체 4.82)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717313498002096180/3aa0aaca93167e97.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 델푸스":
        embed=discord.Embed(color=0xff00, title="델푸스[지9/수1]", description="획득방법 : VIP 늑대 랜덤 페트병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 8, 55', value = '성장률 : 공 2.10, 방 1.37, 순 1.54, 내구력 10.09 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717316140539576440/caa1d0f9091a6862.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 갈푸스":
        embed=discord.Embed(color=0xff00, title="갈푸스[화9/풍1]", description="획득방법 : VIP 늑대 랜덤 페트병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 6, 8, 54', value = '성장률 : 공 2.27, 방 1.24, 순 1.50, 내구력 9.90 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717316180993638511/54f7aa2585da3d57.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 울푸스":
        embed=discord.Embed(color=0xff00, title="울푸스[수10]", description="획득방법 : VIP 늑대 랜덤 페트병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 8, 58', value = '성장률 : 공 2.15, 방 1.30, 순 1.59, 내구력 10.66 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717316211754532894/547b96034d949476.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 베르푸스":
        embed=discord.Embed(color=0xff00, title="베르푸스[풍10]", description="획득방법 : VIP 늑대 랜덤 페트병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 9, 53', value = '성장률 : 공 2.13, 방 1.19, 순 1.73, 내구력 9.76 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717316224807075870/bbf580fd383545fe.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 사이록스":
        embed=discord.Embed(color=0xff00, title="사이록스[화3/풍7]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 8, 53', value = '성장률 : 공 2.14, 방 1.37, 순 1.54, 내구력 9.76 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721987055877357608/67a42bade05601e7.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 볼프":
        embed=discord.Embed(color=0xff00, title="볼프[지7/수3]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 8, 5, 49', value = '성장률 : 공 2.25, 방 1.65, 순 1.07, 내구력 10.24 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721987015058653245/4752228ea2fe1601.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 페르페":
        embed=discord.Embed(color=0xff00, title="페르페[수6/화4]", description="획득방법 : VIP 늑대 랜덤 페트병(한정)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 7, 46', value = '성장률 : 공 1.96, 방 1.31, 순 1.69, 내구력 9.91 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717317782034710568/bdbbadcc4b42f68c.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 토라":
        embed=discord.Embed(color=0xff00, title="토라[화4/풍6]", description="획득방법 : VIP 늑대 랜덤 페트병(한정)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 6, 8, 47', value = '성장률 : 공 1.99, 방 1.27, 순 1.69, 내구력 9.71 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717317815681548348/cc2c3e14a41188c0.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카르페":
        embed=discord.Embed(color=0xff00, title="카르페[화7/풍3]", description="획득방법 : VIP 늑대 랜덤 페트병(한정)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 6, 45', value = '성장률 : 공 2.16, 방 1.31, 순 1.42, 내구력 9.63 (전체 4.88)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717317828402741259/00c7e6f2cc5da122.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 볼케":
        embed=discord.Embed(color=0xff00, title="볼케[화10]", description="획득방법 : VIP 볼케 펫병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 6, 8, 53', value = '성장률 : 공 2.22, 방 1.24, 순 1.59, 내구력 9.76 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717320133474779176/e7e551084b65f6ed.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카우거":
        embed=discord.Embed(color=0xff00, title="카우거[지7/풍3]", description="획득방법 : VIP 카우거 펫병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 8, 7, 54', value = '성장률 : 공 2.19, 방 1.47, 순 1.40, 내구력 9.95 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717319928021123112/db1bb7e21229db94.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 크루거":
        embed=discord.Embed(color=0xff00, title="크루거[지5/수5] (2등급)", description="획득방법 : 부의 부탁 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 8, 55', value = '성장률 : 공 2.08, 방 1.46, 순 1.51, 내구력 10.17 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717320091963883611/831f3d7303e3eb2f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 이구로스":
        embed=discord.Embed(color=0xff00, title="이구로스[지5/풍5]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 8, 54', value = '성장률 : 공 2.10, 방 1.37, 순 1.50, 내구력 10.05 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721988740997840956/ae230ab2de0e56c6.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 샤크론":
        embed=discord.Embed(color=0xff00, title="샤크론[수10]", description="획득방법 : VIP 샤크론 펫병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 8, 57', value = '성장률 : 공 2.15, 방 1.25, 순 1.64, 내구력 10.47 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717323571227131914/5737108082d0f3c7.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 마루아치":
        embed=discord.Embed(color=0xff00, title="마루아치[지1/풍9]", description="획득방법 : VIP 마루아치 펫병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 8, 55', value = '성장률 : 공 2.19, 방 1.33, 순 1.50, 내구력 10.09 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717323695177334795/a2c226e23de2c2fb.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 기린":
        embed=discord.Embed(color=0xff00, title="기린[지9/풍1]", description="획득방법 : VIP 기린 펫병", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 10, 4, 56', value = '성장률 : 공 2.15, 방 2.06, 순 0.83, 내구력 10.66 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717323774063542322/1784fc9904380ab7.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 젖소":
        embed=discord.Embed(color=0xff00, title="젖소[지5/풍5]", description="획득방법 : B코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 7, 6, 50', value = '성장률 : 공 2.08, 방 1.65, 순 1.26, 내구력 10.43 (전체 4.98)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717324124732522516/c162c9e43c7a9bca.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 흑우":
        embed=discord.Embed(color=0xff00, title="흑우[수5/화5]", description="획득방법 : D코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 7, 6, 48', value = '성장률 : 공 2.16, 방 1.52, 순 1.35, 내구력 10.47 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717324262263881738/3661bd8b57d4383a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 하누":
        embed=discord.Embed(color=0xff00, title="하누[지5/수5]", description="획득방법 : C코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 9, 5, 52', value = '성장률 : 공 1.87, 방 1.92, 순 1.16, 내구력 10.76 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717324269012516874/1fca1a03b86eddef.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 화우":
        embed=discord.Embed(color=0xff00, title="화우[화10]", description="획득방법 : A코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 8, 5, 4, 49', value = '성장률 : 공 2.08, 방 1.35, 순 1.07, 내구력 11.80 (전체 4.51)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717324276029456454/178ba266d32f43b4.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 로라미우스":
        embed=discord.Embed(color=0xff00, title="로라미우스[풍10]", description="획득방법 : 사이너스 섬 (동639, 남356) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 7, 6, 49', value = '성장률 : 공 2.25, 방 1.46, 순 1.31, 내구력 10.17 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717444000570671104/2330c6c42f1530ee.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 타라미우스":
        embed=discord.Embed(color=0xff00, title="타라미우스[지8/풍2]", description="획득방법 : 사이너스 섬 (동620, 남372) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 7, 6, 47', value = '성장률 : 공 2.24, 방 1.45, 순 1.31, 내구력 9.76 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717444027884109914/3804945f9897cab6.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 미라미우스":
        embed=discord.Embed(color=0xff00, title="미라미우스[화9/풍1]", description="획득방법 : 사이너스 섬 (동590, 남381) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 6, 46', value = '성장률 : 공 2.22, 방 1.32, 순 1.36, 내구력 9.85 (전체 4.89)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717444064366034974/da28fe5bbb4dcab0.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 보라미우스":
        embed=discord.Embed(color=0xff00, title="보라미우스[지1/수9]", description="획득방법 : 사이너스 섬 (동648, 남339) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 6, 49', value = '성장률 : 공 2.16, 방 1.34, 순 1.31, 내구력 10.19 (전체 4.81)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717444108033065061/f7ba8231b3c798e1.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 파투스":
        embed=discord.Embed(color=0xff00, title="파투스[수3/화7]", description="획득방법 : 쟈루 섬 (동124, 남764) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 8, 6, 53', value = '성장률 : 공 2.15, 방 1.55, 순 1.26, 내구력 10.12 (전체 4.97)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717445395126550548/3a3f217d7db95b18.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 클리오스":
        embed=discord.Embed(color=0xff00, title="클리오스[지6/수4]", description="획득방법 : 쟈루 섬 (동167, 남605) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 10, 4, 58', value = '성장률 : 공 2.01, 방 2.01, 순 0.78, 내구력 10.62 (전체 4.80)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717445410565783653/4d290c58fd6d4f30.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 배모티스":
        embed=discord.Embed(color=0xff00, title="배모티스[화2/풍8]", description="획득방법 : 쟈루 섬 (동166, 남722) 포획", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 8, 5, 49', value = '성장률 : 공 2.10, 방 1.64, 순 1.16, 내구력 9.86 (전체 4.90)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717445421978484847/ed3e7179dcd28c57.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 후바티":
        embed=discord.Embed(color=0xff00, title="후바티[수10]", description="획득방법 : A코스 랜덤 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 7, 54', value = '성장률 : 공 2.25, 방 1.35, 순 1.40, 내구력 10.81 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717446431320965241/e3166bdc2b537033.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 테르가":
        embed=discord.Embed(color=0xff00, title="테르가[수3/화7]", description="획득방법 : 복권 1등 페트 (카루타나)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 7, 6, 48', value = '성장률 : 공 2.15, 방 1.51, 순 1.40, 내구력 9.95 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717448213753233492/0922922ee3be75be.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 테이토스":
        embed=discord.Embed(color=0xff00, title="테이토스[수5/화5]", description="획득방법 : 복권 1등 페트 (샴기르)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 14, 3, 75', value = '성장률 : 공 2.00, 방 2.26, 순 0.55, 내구력 11.90 (전체 4.81)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717448225866645564/2bb0a52527cbc74c.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 호네":
        embed=discord.Embed(color=0xff00, title="호네[화1/풍9]", description="획득방법 : 리푸섬 진입 퀘스트 랜덤 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 8, 50', value = '성장률 : 공 2.15, 방 1.22, 순 1.66, 내구력 9.58 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717451787740905542/31423a57864156b7.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 호루":
        embed=discord.Embed(color=0xff00, title="호루[지2/수8]", description="획득방법 : 리푸섬 진입 퀘스트 랜덤 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 8, 65', value = '성장률 : 공 2.12, 방 1.30, 순 1.45, 내구력 11.04 (전체 4.87)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/717451794099208203/40abeec311520ade.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 프라피":
        embed=discord.Embed(color=0xff00, title="프라피[화5/풍5]", description="획득방법 : 난파선 전역", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 5, 7, 44', value = '성장률 : 공 2.06, 방 1.21, 순 1.66, 내구력 9.68 (전체 4.93)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/718376672046350336/00eef28a9d3cd61f.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 모사크":
        embed=discord.Embed(color=0xff00, title="모사크[수10]", description="획득방법 : 난파선 레이드 (리바이어던)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 13, 8, 7, 58', value = '성장률 : 공 2.29, 방 1.43, 순 1.31, 내구력 10.28 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/718376692275478602/c622c9719fa198d3.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 델타르돈":
        embed=discord.Embed(color=0xff00, title="델타르돈[지9/풍1]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 8, 7, 53', value = '성장률 : 공 2.06, 방 1.54, 순 1.35, 내구력 9.86 (전체 4.95)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721985839986638909/c99cced2ee37c28a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카르카로돈":
        embed=discord.Embed(color=0xff00, title="카르카로돈[지1/풍9]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 7, 54', value = '성장률 : 공 2.23, 방 1.33, 순 1.35, 내구력 10.00 (전체 4.91)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721986223538962502/3799d1927a432d84.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 프리쉴라":
        embed=discord.Embed(color=0xff00, title="프리쉴라[지2/수8]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 6, 46', value = '성장률 : 공 2.22, 방 1.32, 순 1.40, 내구력 9.67 (전체 4.94)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721989510644105226/eab00e43dc7e73a4.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 호르카":
        embed=discord.Embed(color=0xff00, title="호르카[지6/수4]", description="획득방법 : 위드쿠폰 1차", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 9, 7, 7, 50', value = '성장률 : 공 1.94, 방 1.49, 순 1.46, 내구력 10.02 (전체 4.89)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721989582194868235/94bbd13a306543b9.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 익시노돈":
        embed=discord.Embed(color=0xff00, title="익시노돈[풍10]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 6, 9, 50', value = '성장률 : 공 2.08, 방 1.20, 순 1.78, 내구력 9.61 (전체 5.06)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721991631271886948/1a5d818b06d89618.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 야크노":
        embed=discord.Embed(color=0xff00, title="야크노[지8/풍2]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 6, 53', value = '성장률 : 공 2.22, 방 1.47, 순 1.31, 내구력 10.12 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721992683002003507/3adb54f0396ff0d6.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 바쿰":
        embed=discord.Embed(color=0xff00, title="바쿰[지4/수6]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 11, 3, 66', value = '성장률 : 공 2.09, 방 2.04, 순 0.69, 내구력 12.09 (전체 4.82)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721992673279344760/0c003f718481d714.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 타르톤":
        embed=discord.Embed(color=0xff00, title="타르톤[지2/풍8]", description="획득방법 : 빛나는 페트상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 9, 2, 53', value = '성장률 : 공 2.22, 방 1.92, 순 0.47, 내구력 11.07 (전체 4.61)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721992805177753630/365ae35cdd57c8eb.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 바우트":
        embed=discord.Embed(color=0xff00, title="바우트[수1/화9]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 10, 2, 56', value = '성장률 : 공 2.26, 방 2.04, 순 0.42, 내구력 10.82 (전체 4.72)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721994800081010738/b9b263b78edf7b3c.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 샤우트":
        embed=discord.Embed(color=0xff00, title="샤우트[지5/풍5]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 12, 2, 63', value = '성장률 : 공 2.12, 방 2.20, 순 0.40, 내구력 11.09 (전체 4.72)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721994916242128928/849f92d79fa3d4be.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 카라고니스":
        embed=discord.Embed(color=0xff00, title="카라고니스[지2/풍8]", description="획득방법 : 몽환의 동굴 (낮) (동11, 남12) (요리 - 특제 삶은 달걀)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 5, 8, 49', value = '성장률 : 공 2.22, 방 1.16, 순 1.62, 내구력 9.76 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721997247100878858/cbe9b51f3f77bc8a.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 트라고니스":
        embed=discord.Embed(color=0xff00, title="트라고니스[수10]", description="획득방법 : 루이 포획지역 (요리 - 특제 삶은 달걀)", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 6, 8, 57', value = '성장률 : 공 2.24, 방 1.25, 순 1.50, 내구력 10.43 (전체 4.99)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/721997282668707880/743a7b2e1170c0a1.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 아비시니안":
        embed=discord.Embed(color=0xff00, title="아비시니안[화1/풍9]", description="획득방법 : 베르푸스 레이드", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 5, 7, 47', value = '성장률 : 공 2.23, 방 1.21, 순 1.57, 내구력 9.76 (전체 5.01)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726063265741799434/0961e673011d5476.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 모나토":
        embed=discord.Embed(color=0xff00, title="모나토[풍10]", description="획득방법 : 듀얼 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 9, 56', value = '성장률 : 공 2.27, 방 1.25, 순 1.59, 내구력 10.00 (전체 5.11)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/726070242270248970/992986efcb3aeecc.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 레피온":
        embed=discord.Embed(color=0xff00, title="레피온[수2/화8]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 8, 52', value = '성장률 : 공 2.22, 방 1.24, 순 1.54, 내구력 9.90 (전체 5.00)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728632426519199854/aa4db839688e6d00.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 블랙드래곤":
        embed=discord.Embed(color=0xff00, title="블랙드래곤[수2/화8]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 7, 53', value = '성장률 : 공 2.32, 방 1.38, 순 1.40, 내구력 9.81 (전체 5.10)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728632496404693022/e7bdf0e9bed4a8ac.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 구루마루":
        embed=discord.Embed(color=0xff00, title="구루마루[지6/풍4]", description="획득방법 : VIP 페트", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 7, 56', value = '성장률 : 공 2.24, 방 1.34, 순 1.45, 내구력 10.28 (전체 5.03)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728632411495333949/f92f225c4b8b4727.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 부루마루":
        embed=discord.Embed(color=0xff00, title="부루마루[수8/화2]", description="획득방법 : 이벤트 상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 6, 7, 53', value = '성장률 : 공 2.24, 방 1.26, 순 1.54, 내구력 10.66 (전체 5.04)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/729322314138910751/b67971ec1bacecc2.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 아르마루":
        embed=discord.Embed(color=0xff00, title="아르마루[지5/수5]", description="획득방법 : 이벤트 상자", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 11, 7, 7, 53', value = '성장률 : 공 2.19, 방 1.33, 순 1.50, 내구력 10.09 (전체 5.02)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/729322290759729182/fb4e76663025e4c7.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 디사크":
        embed=discord.Embed(color=0xff00, title="디사크[화8/풍2]", description="획득방법 : 심연의 악몽 레이드 보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 12, 7, 7, 54', value = '성장률 : 공 2.32, 방 1.38, 순 1.35, 내구력 9.95 (전체 5.05)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/728656458643800085/81fc1181022afb77.gif")
        await message.channel.send(embed=embed)
    if message.content == "!알려 파이카스":
        embed=discord.Embed(color=0xff00, title="파이카스[화9/풍1]", description="획득방법 : B코스 랜덤보상", timestamp=message.created_at)
        embed.add_field(name = '초기치 : 10, 13, 1, 58', value = '성장률 : 공 1.98, 방 2.45, 순 0.36, 내구력 10.62 (전체 4.79)')
        embed.set_image(url="https://cdn.discordapp.com/attachments/716792879481225328/730226724360552529/17457360858e312c.gif")
        await message.channel.send(embed=embed)
app.run(token)
