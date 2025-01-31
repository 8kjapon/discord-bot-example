import discord
from discord.ext import commands
from discord import app_commands

# モーダルウィンドウ表示用クラスの定義
class ModalView(discord.ui.Modal, title='モーダルウィンドウ'):
    '''モーダルウィンドウの表示と設定を行うクラスです
        self.name: styleでshortを指定することで1行の入力欄を表示します
        self.content: styleでlongを指定することで複数行の入力欄を表示します
        placeholderで入力欄に表示されるテキストを設定できます
    '''
    def __init__(self):
        super().__init__()
        
        # 入力欄の設定
        self.name = discord.ui.TextInput(label='お名前', style=discord.TextStyle.short, placeholder='でぃすこ ぼっと')
        self.content = discord.ui.TextInput(label='内容', style=discord.TextStyle.long, placeholder='文章を入力してください')
        
        # 入力欄を追加
        self.add_item(self.name)
        self.add_item(self.content)

    # モーダルウィンドウ内で送信ボタンが押された時の処理
    async def on_submit(self, interaction: discord.Interaction):
        '''入力された内容を埋め込みメッセージとして送信
            入力された情報は以下のように扱えます
            self.name.value: お名前項目の入力内容
            self.content.value: 内容項目の入力内容
        '''
        embed = discord.Embed(
            title='入力された内容',
            color=discord.Color.orange()
        )
        embed.add_field(name='お名前', value=self.name.value, inline=False)
        embed.add_field(name='内容', value=self.content.value, inline=False)

        await interaction.response.send_message(embed=embed)
        self.stop()

# Cogの定義
class ModalCog(commands.Cog):
    '''モーダルウィンドウの表示機能をまとめたCogになります'''
    def __init__(self, bot):
        self.bot = bot
    
    # モーダルウィンドウのサンプルを表示するコマンド
    @app_commands.command(name='modal', description='モーダルウィンドウのサンプルを表示します')
    async def modal(self, interaction: discord.Interaction):
        view = ModalView()
        await interaction.response.send_modal(view)
        await view.wait() # モーダルウィンドウの操作が完了するまで待機

async def setup(bot):
    await bot.add_cog(ModalCog(bot))