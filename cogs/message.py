import discord
from discord.ext import commands
from discord import app_commands


# Cogの定義
class MessageCog(commands.Cog):
    '''メッセージ関連の機能をまとめたCogになります'''
    def __init__(self, bot):
        self.bot = bot

    # 実行すると「こんにちは！」とメッセージを返すコマンド
    @app_commands.command(name='hello', description='挨拶をします')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message('こんにちは！')

    # 実行すると埋め込みメッセージのサンプルを返すコマンド
    @app_commands.command(name='embed_message', description='埋め込みメッセージを送信')
    async def embed_message(self, interaction: discord.Interaction):
        '''埋め込みメッセージの一通りの機能を使用したサンプルです
            以下の項目を設定しています
            基本部分:
                - title: タイトル
                - color: 埋め込みメッセージの左縁の色
                - description: 説明
            追加部分:
                - field: 追加で表示出来るフィールド
                - author: メッセージの送信者
                - footer: メッセージの下部に表示されるテキスト
                - image: 画像
                - thumbnail: サムネイル
            それぞれに設定されたテキストや画像を参考にどこを示した部分なのか確認してみてください
            ローカル画像の使用についても触れています
        '''
        embed = discord.Embed(
            title='タイトル部分です',
            color=discord.Color.green(),
            description='説明部分です'
        )

        embed.add_field(name='フィールド部分', value='フィールド部分の内容')

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar)
        embed.set_footer(text='フッター部分です')

        # Botでローカルに保存されている画像を使用するには以下のように画像を読み込みます
        image_file = discord.File('assets/image.png', filename='image.png')
        embed.set_image(url='attachment://image.png')
        embed.set_thumbnail(url='attachment://image.png')
        await interaction.response.send_message(embed=embed, file=image_file) # 画像を送信する場合はfile引数にファイルを指定する (メッセージのみの場合は不要)
    
    # 実行するとオプション値に指定された文字を返すコマンド
    @app_commands.command(name='yamabiko', description='オプション値に指定された文字を返します')
    @app_commands.describe(word='返ってくる文字')
    async def yamabiko(self, interaction: discord.Interaction, word: str):
        await interaction.response.send_message(word)

async def setup(bot):
    await bot.add_cog(MessageCog(bot))