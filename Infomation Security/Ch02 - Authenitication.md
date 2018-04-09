# Chapter 2 - Authentication 認證

## 存取控制簡介 Basics of Access Control
+ 方法(Method)與物件(Component)的集合(Collection)
	+ 機密性(Confidentiality)
	+ 完整性(Integrity)
+ 存取控制的目標是在許可範圍內，去認證允許(Permitted)主體(Subject)存取物件(Object)的行為
+ 主體不一定是人，只要發出請求(Request)的都是主體

## 存取與控制 Access & Control
+ 包含了**存取**(Access)與**控制**(Control)兩個部分
+ 認證 Authentication
	+ 誰可以過去? (Who goes there?)
	+ 認證人對機器的存取
	+ 認證機器對機器的存取
+ 授權 Authorization
	+ 可不可以做這件事? (Are you allow to do that?)
	+ 有了存取權後可以做什麼?
	+ 對行為施加限制
+ <span style="color:red">**注意**</span>：
	存取控制常被當成授權的代名詞(Synonym)，但完整定義必須包含兩個部分
+ 主體 Subject
	+ 發出要存取資源需求的個體(Entity)
+ 對象 Object
	+ 主體試圖存取的資源
+ 最低存取原則 Least Privilege Philosophy
	+ 給予主體足夠完成所需工作的權限即可

## 控制 Control
+ 允許或禁止對象訪問的機制(Mechanisms)
	+ 也可以說是不合法存取的一種阻礙(Barrier)
+ 控制常見的種類
	+ 管理層面 Administrative
		+ 從**管理策略**來執行(Enforce)安全規則
		+ 例如：雇用策略 Hiring Practice，無不良紀錄才雇用
		+ 雇用後的狀況觀察：使用量監測和稽核(Usage Monitoring & Accounting)
	+ 邏輯與技術 Logic & Technical
		+ 對象存取的限制(Restrictions)
		+ 例如：
			+ 識別 Identification：多對一的比較
			+ 認證 Authentication：一對一的比較
			+ 加密 Encryption
	+ 實體 Physical
		+ 將存取限制施加在硬體上
		+ 例如：圍牆(Fence)、牆壁、上鎖的門

## 存取控制技術 Access Control Techniques
+ 選擇符合組織需求的技術
+ 也要考慮使用者的接受度

## 存取控制設計 Access Control Designs
+ ### Mandantory Access Control
	+ 指定安全標籤(Security Label)給每個主體和物件
	+ 由安全標籤來決定行為是否准許(Granted)
	+ 常見的應用方式為 **Rule-Based 存取控制**
		+ Rule-Base 是 Mandantory 的一種實作方式
		+ 需要知道給主體哪種等級的安全標籤
		+ 是一種強制的存取控制
	+ 常見軍方(Military)資料分級(Classifications)
		+ 未分類 Unclassified
		+ 敏感但未分類 Sensitive but Unclassified
		+ 機密 Confidential
		+ 秘密 Secret
		+ 最高機密 Top Secret
	+ 常見商業(Commercial)資料分級
		+ 公開 Public
		+ 敏感 Sensitive
		+ 私人 Private
		+ 機密 Confidential
+ ### Discretionary Access Control
	+ 依照物件所有者的喜好決定
	+ 商業操作上常見的設計
	+ 基本上比較彈性、易實作
	+ 基本上比 Mandantory 不安全
	+ 包含 Identity-Based 存取控制、Access Control Lists(ACLs)
+ ### Non-Discretionary Access Control
	+ 根據主體的角色與任務決定存取控制權
		+ 也可稱為 Role-Based, Task-Based Access Control
	+ Lattice-Based Control 是一種 Non-Discretionary Access Control 的變體(Variation)
		+ 主體和對象之間具有一組用於定義訪問規則和條件的邊界

## 存取控制的管理 Access Control Administration
+ 主要分為集中式、分散式、混合式
+ ### 集中式 Centralized
	+ 所有的需求都經過一個權力核心
	+ 管理政策相對單純
	+ 因為都經過一個點，所以會有效能瓶頸(Bottlenecks)
+ ### 分散式 Decentralized
	+ 物件的存取控制不是集中的
	+ 相對複雜的管理策略
	+ 效能相對穩定

## 責任 Accountability
+ 系統管理員使用系統審核(Auditing)來監測
	+ 誰在使用系統 (Who is using the system)
	+ 在使用系統做什麼 (What users are doing)
+ Logs 訊息很重要，負責追蹤事件
+ 但這個過程會對效能造成影響
	+ 限制 Logs 的數量大小
	+ 設定 Logs 啟動的門檻(Clipping Level)
	+ 紀錄關鍵的事件才能在事後追蹤

## 存取控制模型 Access Control Models
+ ### State Machine Model
	+ 定義 Object 的狀態和轉換的集合
	+ Ex: 印表機的休眠、列印中狀態
	+ #### Bell-LaPadula Model
		+ 強調機密性(Confidentiality)
		+ No read up, no write down
			+ 不可以讀機密性高的文件
			+ 不可以把高機密內容寫到機密性低的文件
	+ #### Biba Model
		+ 強調完整性(Integrity)
		+ No read down, no write up
			+ 將軍不去讀小兵寫的策略
			+ 小兵不能寫將軍的策略
+ ### Clark-Wilson Model
	+ 不是一種狀態機模型
	+ 用不同的途徑(Approach)確保完整性
	+ CDIs: Constrained Data Items 受保護的資料
	+ UDIs: Unconstrained Data Items 未受保護的資料
	+ IVPs: Integrity Verification Procedures
		+ 驗證資料完整性的程序
	+ TPs: Transaction Procedures
		+ 任何對資料進行的授權修改行為
	+ 所有在模型下的資料都是CDIs
	+ IVPs會確保系統中資料的完整性
	+ TPs會接收CDIs或UDIs並且製造CDIs
	+ TPs必須保證所有可能的UDIs都會變成安全的CDIs
+ ### Noninterference Model
	+ 通常是其他模型額外的補充
	+ 確保模型彼此不會互相干擾

# Who Goes There?
+ Something You Know: 密碼
+ Something You Have: Smartcard
+ Something You Are: 指紋
+ Ex: 信用卡則包含了實體 & 簽名，其中簽名屬於生物特徵

# 密碼的問題 Trouble With Passwords
+ 在實務上有很嚴重的問題
+ 人類無法選擇過於安全的密碼
+ 密碼的優點：
	+ 成本低，免費
	+ 方便性，易於修改

# Keys vs Passwords
+ 密鑰
	+ 長度 64 Bits，也可以理解成 8 Bytes的字串之類的
	+ 則有 2^64 種組合
	+ 而且系統隨機挑選密鑰
	+ 攻擊者必須嘗試至少 2^63 次
+ 密碼
	+ 長度 8 個字元，有 256 種不同的字元
	+ 則有 256^8 = 2^64 種組合
	+ 但使用者並不會隨機挑選
	+ 攻擊者嘗試次數遠小於 2^63 次
	+ 使用字典攻擊(Dictionary Attack)

# Good & Bad Passwords
+ 不好的密碼可能單調、重複或單字
+ 好的密碼大小寫混雜、長度足夠

# Attacks on Passwords
+ 