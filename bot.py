import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .envからトークンとサーバーIDを取得
load_dotenv()
TOKEN = os.getenv('TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

# Botの定義
class Bot(commands.Bot):
    def __init__(self):
        # テキストコマンドの設定
        super().__init__(command_prefix='!', intents=discord.Intents.all())
        
        # Cogのリスト
        self.initial_extensions = ['cogs.message', 'cogs.ui']

    async def setup_hook(self):
        # Cogの読み込み
        for extension in self.initial_extensions:
            await self.load_extension(extension)
        
        # コマンドの同期
        # 開発環境では以下のようにサーバーIDを指定して同期することで即座にコマンドが反映されるようになります
        self.tree.copy_global_to(guild=discord.Object(id=SERVER_ID))
        await self.tree.sync(guild=discord.Object(id=SERVER_ID))
        # 本番環境では以下のように記述することで全てのサーバーとコマンドを同期します
        # self.tree.sync()

    async def on_ready(self):
        print('ボットが起動しました')

        # Botのステータスを任意のテキストに変更
        await self.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='ボットが起動しています'))

# Botの起動
bot = Bot()
bot.run(TOKEN)