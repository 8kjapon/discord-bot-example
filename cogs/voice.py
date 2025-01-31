import discord
from discord.ext import commands
from discord import app_commands

# Cogの定義
class VoiceCog(commands.Cog):
    '''ボイスチャンネル関連の機能をまとめたCogになります'''
    def __init__(self, bot):
        self.bot = bot
        self.text_channel_ids = {}

    # コマンドが呼び出されたテキストチャンネルのIDを各処理で使用する為に保存・取得・削除する処理
    # テキストチャンネルのIDを保存
    def _set_text_channel_id(self, guild_id, channel_id):
        if guild_id not in self.text_channel_ids:
            self.text_channel_ids[guild_id] = channel_id

    # テキストチャンネルのIDを取得
    def _get_text_channel_id(self, guild_id):
        if guild_id in self.text_channel_ids:
            return self.text_channel_ids.get(guild_id)
        else:
            return None

    # テキストチャンネルのIDを削除
    def _clear_text_channel_id(self, guild_id):
        if guild_id in self.text_channel_ids:
            del self.text_channel_ids[guild_id]

    # ボイスチャンネルに参加するコマンド
    @app_commands.command(name='join', description='コマンド入力者の入室しているボイスチャンネルに接続します')
    async def join(self, interaction: discord.Interaction):
        # コマンド入力者が入室しているボイスチャンネルを取得
        voice_channel = interaction.user.voice.channel

        # ボイスチャンネルが取得出来た場合は接続
        if voice_channel:
            await voice_channel.connect()
            await interaction.response.send_message(f'{voice_channel.name}に接続しました')

            # テキストチャンネルのIDを保存
            self._set_text_channel_id(interaction.guild.id, interaction.channel.id)
        else:
            await interaction.response.send_message('ボイスチャンネルに接続してください')

    # ボイスチャンネルから切断するコマンド
    @app_commands.command(name='disconnect', description='ボイスチャンネルから切断します')
    async def disconnect(self, interaction: discord.Interaction):
        voice_client = interaction.guild.voice_client

        if voice_client:
            await voice_client.disconnect()
            await interaction.response.send_message(f'{voice_client.channel.name}から切断しました')

            # テキストチャンネルのIDを削除
            self._clear_text_channel_id(interaction.guild.id)
        else:
            await interaction.response.send_message('ボイスチャンネルに接続していません')

    # 音声ファイルを再生するコマンド
    @app_commands.command(name='play', description='チャンネルに接続しているボットが音声ファイルを再生します')
    async def play(self, interaction: discord.Interaction):
        voice_client = interaction.guild.voice_client

        if voice_client:
            voice_client.play(discord.FFmpegPCMAudio(source='assets/sound.ogg')) # 指定した音声ファイルを再生
            await interaction.response.send_message('音声ファイルを再生します')
        else:
            await interaction.response.send_message('ボイスチャンネルに接続していません')

    # ボイスチャンネルのユーザーのステータス変化に反応して行う処理
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        '''ユーザーがミュートを有効・解除した際にメッセージを送る機能になります
            on_voice_state_updateはボイスチャンネル上でユーザーのステータスが変化した際に呼び出されるイベントです
            以下のような情報を取得します
                member: ステータスが変化したユーザー
                before: 変化前の状態
                after: 変化後の状態
            これらの情報を使用して監視対象のステータスが変化した際に任意の処理を行うことが出来ます
        '''
        # ミュート状態が変化した場合にメッセージを送信
        # ただしボットでないユーザー(member.bot == False)のみを対象とする
        if before.self_mute != after.self_mute and not member.bot:
            # メッセージを送信するテキストチャンネルは/joinコマンドが呼び出されたチャンネルを指定
            channel_id = self._get_text_channel_id(member.guild.id)
            text_channel = member.guild.get_channel(channel_id)

            # テキストチャンネルが正常に取得出来た場合はメッセージを送信
            if text_channel:
                if after.self_mute:
                    # ミュートになった場合
                    await text_channel.send(f'{member.display_name}がミュートになりました')
                else:
                    # ミュートが解除された場合
                    await text_channel.send(f'{member.display_name}のミュートが解除されました')

async def setup(bot):
    await bot.add_cog(VoiceCog(bot))