"""
NFCカードの読み取りコードだよ

使用に当たって
①↓このサイトからZadig2.9をダウンロード
https://zadig.akeo.ie/
②NFCリーダーをPCに接続
③Zadigを起動して、「Option→List All Devices」をチェック
④「Device」からNFCリーダーを選択(RC-s380?)
⑤「Driver」から「WinUSB」を選択
⑥「Install Driver」をクリックしてドライバをインストール

そのうえでanaconda上で
「pip install nfcpy」でライブラリを入れてね

これで実行可能だーやったね！
実行してタグをかざすと、UIDとタグの種類が表示されるよ
"""

import nfc

def on_connect(tag):
    print("NFCタグを検出しました")
    print("UID:", tag.identifier.hex())
    print("Type:", tag)
    return True

def main():
    clf = nfc.ContactlessFrontend('usb')
    print("NFCタグを待機中...")
    try:
        clf.connect(rdwr={'on-connect': on_connect})
    finally:
        clf.close()

if __name__ == "__main__":
    main()