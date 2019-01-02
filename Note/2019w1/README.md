# 2019 第一週學習筆記

回顧今年，真的是學了不少東西。雖然世界很大，要學的東西很多，自己學過的東西相比之下只是九牛一毛。但期許自己能夠溫故知新，每天都要學點東西。

## 使用 Shell Script 完成 Git Quick Push
+ 自己的小專案其實都不用太認真
+ 大多時候直接 `git add . && git commit && git push`
+ 懶人 Push 的 Shell Script 因此誕生
	```shell
	#!/bin/bash
	# QuickPush.sh
	# Author: Penut
	if [ "$2" != "" ]; then
		cd "$2"
	fi

	if [ "$1" = "" ]; then
		echo "Usage: ./QuickPush.sh [commit-msg] <subfolder>"
	else
		git add .
		git commit -m "$1"
		git push
	fi
	```

## 使用 PIL 獲得圖片額外資訊並進行分類管理
+ 一個檔案在 OS 裡面似乎只有 Last Modified Date
+ 只有圖片有建立日期
+ 透過 PIL 套件來獲得相關資訊
	```python
	import PIL.Image
	import PIL.ExifTags

	img = PIL.Image.open(path)
	exifdata = {
		PIL.ExifTags.TAGS[k]: v
		for k, v in img._getexif().items()
		if k in PIL.ExifTags.TAGS
	}
	orgDate = exifdata['DateTimeOriginal']
	```

## 使用 touch 指令修改圖片的 Last Modified Date
+ `$ touch -d "yyyymmdd HH:MM:SS" [file-path]`