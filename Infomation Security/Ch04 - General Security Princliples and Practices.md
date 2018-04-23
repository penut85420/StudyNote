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

## 可接受行為 AUP - Acceptable Use Policy
+ 必須要能夠具體指導(Guide)使用者
+ 要足夠彈性(Flexible)以應付意外情況(Unanticipated Situations)
+ 制定方向：
	+ 哪些動作可以接受？
	+ 哪些動作不可以接受？
	+ 哪裡可以讓使用者獲得更多資訊？
	+ 如果違規，要如何處置？

## 備份 Backup Policy
+ 用來防止資料的損壞(Corruption)和丟失(Loss)
+ 維持完整性和可用性(Integrity & Availability)
+ 制定方向：
	+ 哪些資料需要被備份？
	+ 要如何備份這些資料？
		+ Ex: 雲端、USB、異地備份
	+ 備份的資料會存放在哪裡？
	+ 誰可以存取這些備份？
	+ 這些備份資料要被保留(Retain)多久？
		+ 不一定所有資料都採用單一的策略
	+ 備份可以被重複使用的頻率？

## 保密 Confidentiality Policy
+ 用來保護(Safeguard)機密訊息
+ 包含所有訊息傳播手段，例如電話、印刷、口頭
+ 制定方向：
	+ 什麼資料是機密的？
	+ 應該如何處理這些資料？
	+ 要如何發布這些機密訊息？
	+ 如果機密資訊外洩要怎麼辦？
+ 員工可能會被要求簽屬保密協定(Nondisclosure Agreements)

## 資料保存 Data Retention Policy
+ 制定資料保留的時間長短
+ 可能透過法律或者業務需求來制定
	+ 例如：納稅的資料要保留七年

## 硬體政策 Physical Security
+ 保護硬體的安全
+ 硬體的危害可能包含天然災害
	+ Ex: 淹水，所以把機房設置在二樓
+ 常見的硬體保護手法：
	+ 周遭的防禦 Perimeter Protection
		+ 實體的阻隔，例如：牆壁
		+ 感應器、看門狗、警衛
		+ 記得 Defense in Depth 原則
			+ 單一的保護機制並不足夠
	+ 防電磁裝置 Electronic Emanations
		+ 國家級的攻擊可能透過電磁波來分析資訊
		+ 使用防電波磁裝置來保護
	+ 防火 Fire Protection
		+ 防止火災，例如：滅火器、灑水設備

## 無線裝置 Wireless Device Policy
+ 包含手機、平板、掌上型電腦
+ 可能會要求員工上班時不能使用或攜帶
+ 制定方向：
	+ 組織可以購買的裝置種類
	+ 個人可以帶入工作場所的裝置
	+ 可以使用該裝置進行哪些行為？
	+ 例外狀況需要授權單位的許可

## 執行 Implementing Policy
+ 內部員工要去遵守這些政策
+ 確保政策持續在進行(Ongoing)

## 發展 Develope Policy
+ 以團隊的方式(Team Approach)來制定
+ Policy 是慢慢發展出來的
+ 先制定目標清單
+ 然後編寫文件
+ 最後達成共識

## 建立共識 Building Consensus
+ 透過 Selling the Policy 來建立共識
+ 發展企業文化，凝聚向心力
+ 通常由高級管理階層來推廣和宣傳

## 教育 Education
+ Initial Training 一次性的訓練
	+ 主要在員工剛進入公司時做的訓練
+ Refresher Training 週期性的訓練
	+ 提醒員工自己的責任
	+ 提供員工最新的政策更新與責任相關事宜

## 執行與維護 Enforcement & Maintenance
+ 責任定義：
	+ 違規舉報
	+ 發生違規時的處置
+ 隨著公司和技術的變化，政策也會隨之改變
+ 政策也要包含如何修改政策的條款

## 工具 Security Administration Tools
+ Security Checklists
	+ 條列式的審核
+ Security Matrices
	+ 把重點放在希望達成的目標
	+ Ex: 轉帳這個行為，完整性 > 機密性

## 人員安全 Personnel Security
+ 人類很脆弱QQ
+ 防止惡意的 Insider 使用的手法：
	+ 背景調查 Background Investigations
		+ 前科調查(Criminal Record)
		+ 打電話去上一間公司問(Reference Evaluations)
	+ 活動監測 Monitor Employee Activity
		+ 包含網路活動、監視器、通話紀錄等
	+ 強制休假 Mandatory Vacations
		+ 符合勞基法的規定
		+ 避免員工壓力過大，做出傷害公司的行為
	+ 離職政策 Exit Procedures
		+ 保密協議很重要

## 總結 Summary
+ Security Principles
	+ Separation of Privileges Principle
	+ Least Privilege Principle
	+ Defense in Depth Principle
	+ Security through Obscurity(X)

+ Policies
	+ Acceptable Use Policy
	+ Backup Policy
	+ Confidentiality Policy
	+ Data Retention Policy
	+ Wireless Device Policy
	+ Physical Security

+ About a Policy
	+ Implementing Policy
	+ Develope Policy
	+ Building Consensus
	+ Education
	+ Enforcement & Maintenance

+ Administration Tools
	+ Security Checklists
	+ Security Matrices

+ Physical Security
	+ Perimeter Protection
	+ Electronic Emanations
	+ Fire Protection

+ Personnel Security
	+ Background Checks
	+ Ongoing Monitoring
	+ Mandatory Vacations
	+ Exit policies