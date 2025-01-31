# Discord Bot Example for Discord.py
discord.pyを使用してPythonでDiscordのBotアプリケーションを作成してみたい方向けのリポジトリになります。
以下のような方に有用なサンプルになるかと思います。
- とりあえず何か作ってみたいけど何から手を付ければ良いかわからない
- 雛形的なものが欲しい
- DiscordのBotがどういう仕組なのか知りたい

## 注意
あくまでExample(使用例)ですのでdiscord.py全ての機能を網羅しているわけではありません。
本格的な実装や運用には処理の最適化やサーバー上での動作など他にも必要なモノが多くあります。
それらの前段階としてdiscord.pyを知る手段の1つとして参考にしていただければと思います。

## 必要な準備
動作させたいコンピューター上にGitとPythonを導入した上で進めてください。
今回はWindowsのコマンドプロンプトでの操作を例として説明します。
Discord Developer Portalでの操作やサーバーIDの取得方法などは省略します。
1. このリポジトリのクローン
2. コマンドプロンプトでリポジトリのディレクトリを開き、以下のコマンドでPythonの仮想環境を作成
```
python -m venv venv
```
3. 仮想環境の立ち上げ
```
venv\Scripts\activate
```
4. 必要パッケージのインストール
```
pip install -r requirements.txt
```
5. [Discord Developer Portal](https://discord.com/developers/docs/intro)でアプリケーションを作成し、トークンとBot招待用のURLを取得
6. `.env-example`を`.env`にリネームし、`YourDiscordTokenHere`の部分を取得したトークンに書き換える
7. 取得した招待用URLから任意のサーバーにBotを招待する
8. 招待したサーバーのサーバーIDを取得し、`.env`の`YourDiscordServerIdHere`の部分をサーバーIDに書き換える
9. 仮想環境を立ち上げた状態のコマンドプロンプトから以下のコマンドでBotを起動
```
python bot.py
```
1. Discord上でBotを使用して動作を確認する

## 参考
- [Discord.py公式ドキュメント](https://discordpy.readthedocs.io/ja/stable/)