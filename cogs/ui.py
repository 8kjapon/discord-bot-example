import discord
from discord.ext import commands
from discord import app_commands

# ボタン表示用クラスの定義
class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label='ボタン', style=discord.ButtonStyle.primary)
    async def button(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True # ボタンを無効化
        button.label = '✔' # ボタンのラベルを変更
        await interaction.response.edit_message(content='ボタンが押されました', view=self)
        self.stop()

# ドロップダウンメニューの内容を定義
class Dropdown(discord.ui.Select):
    def __init__(self):
        # 選択肢の設定
        options = [
            discord.SelectOption(label='壱', value='いち', description='選択肢1'),
            discord.SelectOption(label='弐', value='に', description='選択肢2'),
            discord.SelectOption(label='参', value='さん', description='選択肢3')
        ]
        super().__init__(placeholder='選択してください', min_values=1, max_values=1, options=options)
    
    # ドロップダウンメニューが選択された時の処理
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f'-{self.values[0]}-が選択されました', view=None) # メッセージを更新し、ドロップダウンメニューを非表示

# ドロップダウンメニュー表示用クラスの定義
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(Dropdown())

# Cogの定義
class UiCog(commands.Cog):
    '''ボタンやドロップダウンメニュー等のUI表示機能をまとめたCogになります'''
    def __init__(self, bot):
        self.bot = bot
    
    # 押すとメッセージ内容が更新されるボタンを表示するコマンド
    @app_commands.command(name='button', description='押すとメッセージを返すボタンを表示します')
    async def button(self, interaction: discord.Interaction):
        view = ButtonView()
        await interaction.response.send_message('ボタンを押してください', view=view)
        await view.wait() # ボタンが押されるまで待機

    # ドロップダウンメニューを表示し、選択された内容を表示するコマンド
    @app_commands.command(name='dropdown', description='ドロップダウンメニューのサンプルを表示します')
    async def dropdown(self, interaction: discord.Interaction):
        view = DropdownView()
        await interaction.response.send_message('ドロップダウンメニューを表示します', view=view)

async def setup(bot):
    await bot.add_cog(UiCog(bot))