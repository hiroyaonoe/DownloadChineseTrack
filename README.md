# DownloadChineseTrack
ここ( http://hanyujiaocai.jinkan.kyoto-u.ac.jp/2017beijing/2017CALL/index1.html )  
から中国語の各課の音声ダウンロードとファイル整理  
(もともとの音声ファイルの配置とか名前設定が劣悪すぎてiPhoneに入れようとするとファイル名がコンフリクトする。。)
## とりあえず使い方。

```
$ cd [this project dir]
```
で、プロジェクトディレクトリに移動。
```
$ source venv/bin/activate
```
で、仮想環境venvを有効化。
```
$ python Main.py
```
をやると、いい感じ。のはず。

## Main.pyがやってること。
各課の本文の音声のみをcontents/honbunフォルダに移動、    
各課の文法例文の音声をcontents/Liフォルダ(iは、0<i<23の整数)に移動。他削除。

## なんか、timeoutとか、エラーがでたら。
とりあえずcontentsフォルダ削除して、もっかい
```
$ python Main.py
```
それでもなんか無理だったら、ファイルダウンロードするコードのあとに1秒くらいスリープいれると、出来る。かも。
```
import time
time.sleep(1) #<-これを、for文の中の適当なとこにいれてみる。
```   
なんかいい方法あったら教えてくれ。

