# Chapter 4 - General Security Principles and Practices

## 常見的安全原則 Common Security Principles
+ ### 分散權力原則 Separation of Privileges Principle
	+ 避免單一 User 擁有過大的權力
	+ Ex: 兩個鑰匙才能啟動一顆飛彈
	+ Ex: 公司的存摺與印章
+ ### 最小權力原則 Least Privilege Principle
	+ 每個 User 只擁有最小的權力
	+ 但 Admin 經常沒有注意到(Inattention)
		+ 把 User 放在權力太廣闊(Broad)的層級
	+ 或者發生權力轉移(Privilege Creep)
		+ 當 User 的角色改變，但現有的權力卻沒有改變
+ ### 深度防禦原則 Defense in Depth Principle
	+ 分層式(Layered)的防禦
	+ 可以解決效能瓶頸(Bottleneck)問題
+ ### 模糊式的安全 Security through Obscurity
	+ 在早期，可以把安全建立在 User 的無知
	+ 但現在資訊發達，已經不能這樣做
	+ 現在的資安都要建立在演算法公開的情形下設計
		+ 只有 Key 是私有的

## 安全政策 Security Policies
+ 安全政策必須要是個可以寫出來的文件(Written Document)
+ 可能是單個文件或多個文件，以供不同用戶組使用

## 可接受的政策 AUP - Acceptable Use Policy
+ 必須要能夠具體指導(Guide)使用者
+ 要足夠彈性(Flexible)以應付意外情況(Unanticipated Situations)
+ 要制定一個 AUP，必須要能夠回答以下問題：
	+ 哪些動作可以接受？
	+ 哪些動作不可以接受？
	+ 哪裡可以讓使用者獲得更多資訊？
	+ 如果違規，要如何處置？

## 備份政策 Backup Policy
+ 用來防止資料的損壞(Corruption)和丟失(Loss)
+ 維持完整性和可用性(Integrity & Availability)
+ 要制定一個備份政策，必須要能夠回答以下問題：
	+ 哪些資料需要被備份？
	+ 要如何備份這些資料？
		+ Ex: 雲端、USB、異地備份
	+ 備份的資料會存放在哪裡？
	+ 誰可以存取這些備份？
	+ 這些備份資料要被保留(Retain)多久？
		+ 不一定所有資料都採用單一的策略
	+ 備份可以被重複使用的頻率？