# DownloadChineseTrack
ここ( http://hanyujiaocai.jinkan.kyoto-u.ac.jp/2017beijing/2017CALL/index1.html )  
から中国語の各課の音声ダウンロードとファイル整理  
(もともとの音声ファイルの配置とか名前設定が劣悪すぎてiPhoneに入れようとするとファイル名がコンフリクトする。。)<br>
追記：小テストが12月何日かにあるっぽく、それ用のやつも追加。
## とりあえず使い方。

```
$ cd [this project dir]
```
で、プロジェクトディレクトリに移動。
```
$ source venv/bin/activate
```
で、仮想環境venvを有効化。<br>
で、全課の音声ファイルだったら、
```
$ python Main.py
```
第1回小テスト用だったら、
```
$ python 1st_CheckTest.py
```
をやると、いい感じ。のはず。

## Main.pyがやってること。
各課の本文の音声のみをcontents/honbunフォルダに移動、    
各課の文法例文の音声、各フォルダから取り出してrenameをしてcontents/HonbunAndBunpou/L{i}/に移動。<br>
他削除。(iは、0<i<23)

## 1st_CheckTest.pyがやってること
contents/1stCheckTest/に課題例文をダウンロード。

## なんか、timeoutとか、エラーがでたら。
とりあえずcontents/HonbunAndBunpouフォルダ削除して、もっかい
```
$ python Main.py
```
それでもなんか無理だったら、ファイルダウンロードするコードのあとに1秒くらいスリープいれると、出来る。かも。
```
import time
time.sleep(1) #<-これを、for文の中の適当なとこにいれてみる。
```   
