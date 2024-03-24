# カウントダウンタイマー

## 使い方
### 設定画面
- タイマーの時間を設定できます。
- "window always on top" をONにすると、このウィンドウが最前面に表示されます。
- 再生ボタンを押すと、タイマー画面に遷移しタイマーを開始します。

### タイマー画面
- クリックするとタイマーを一時停止・再開できます。
- フォーカス時に右下に表示されるボタンを押すと、タイマーを停止し設定画面に遷移します。

## ダウンロード
https://github.com/mh326/countdown-timer/releases

## コマンドライン引数
```
countdown-timer_windows.exe -m 1 -s 30 -w -st -a
```
| オプション                    | 説明                              |
| ----------------------------- | --------------------------------- |
| `-m` `--min`                  | 初期値（分）                      |
| `-s` `--sec`                  | 初期値（秒）                      |
| `-w` `--window-always-on-top` | "window always on top" をONにする |
| `-st` `--sound-on-time-over`  | "sound on time over" をONにする   |
| `-a` `--auto-start`           | 起動時にタイマーを開始する        |
