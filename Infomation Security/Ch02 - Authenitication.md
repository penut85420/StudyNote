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
+ ### 強制型 Mandatory Access Control
	+ 指定安全標籤(Security Label)給每個主體和物件
	+ 由安全標籤來決定行為是否准許(Granted)
	+ 常見的應用方式為 **Rule-Based 存取控制**
		+ Rule-Base 是 Mandatory 的一種實作方式
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
+ ### 斟酌型 Discretionary Access Control
	+ 依照物件所有者的喜好決定
	+ 商業操作上常見的設計
	+ 基本上比較彈性、易實作
	+ 基本上比 Mandatory 不安全
	+ 包含 Identity-Based 存取控制、Access Control Lists(ACLs)
+ ### 非斟酌型 Non-Discretionary Access Control
	+ 根據 Subject 的角色與任務決定存取控制權
		+ 也可稱為 Role-Based, Task-Based Access Control
	+ 適用於角色轉換頻繁(High Turnover)的公司
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
+ ### 混和式 Hybrid

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
	+ 所有在模型下的資料都是 CDIs
	+ IVPs 會確保系統中資料的完整性
	+ TPs 會接收 CDIs 或 UDIs 並且製造 CDIs
	+ TPs 必須保證所有可能的 UDIs 都會變成安全的 CDIs
+ ### Noninterference Model
	+ 通常是其他模型額外的補充
	+ 確保模型彼此不會互相干擾

## Who Goes There?
+ Something You Know: 密碼
+ Something You Have: Smart Card
+ Something You Are: 指紋
+ Ex: 信用卡則包含了實體 & 簽名，其中簽名屬於生物特徵

## 密碼的問題 Trouble With Passwords
+ 在實務上有很嚴重的問題
+ 人類無法選擇過於安全的密碼
+ 密碼的優點：
	+ 成本低，免費
	+ 方便性，易於修改
+ 密碼的缺點：
	+ 太容易被破解
	+ 對Bad Guy很有優勢
+ 密碼是資訊安全的底限(Bottom Line)

## Keys vs Passwords
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

## Good & Bad Passwords
+ 不好的密碼可能單調、重複或單字
+ 好的密碼大小寫混雜、長度足夠

## 密碼實驗 Password Experiment
+ **實際的實驗內容參考PPT第28頁**
+ 實驗的過程發現，使用者很難遵從(Compliance)實驗規則
+ 選擇密碼的建議：
	+ 系統指定的密碼可能比較好
	+ 使用密碼破解工具(Cracking Tool)測試安全性
	+ 定期(Periodic)更換密碼

## 密碼攻擊 Attacks on Password
+ Outsider > Normal User > Administrator
+ 有時可能一個脆弱的密碼就導致整個系統被入侵

## 密碼重試 Password Retry
+ 有些系統可能會在三次嘗試之後鎖定登入
+ 鎖定登入的等待越久，雖然安全性越高，但使用者也越不方便

## 密碼檔案 Password File
+ 把密碼存在一個檔案裡面是不好的主意
+ 加密(Cryptographic)方法：雜湊(Hash)
	+ 在密碼檔案裡面儲存 y = h(pwd)
	+ 即便密碼檔案被獲取，攻擊者也不知道密碼是多少
	+ 但攻擊者可以藉由猜測密碼 x 得到 y = h(x) 來破解密碼
	+ 所以還是無法降低攻擊者的猜測
+ 若使用字典攻擊
	+ 攻擊者只要算一次雜湊值就可以猜測所有人的密碼
	+ 對攻擊者的成本好像反而更低了
+ 更好的加密方法：Hash with Salt
	+ Salt 是 Admin 選的
	+ 選擇亂數 s，計算 y = h(pwd, s)
	+ 在密碼檔案裡面儲存 s 跟 y
	+ Salt 是公開的
	+ 驗證密碼非常容易
	+ 但是攻擊者就不能一次猜全部

## Password Cracking: Do The Math
+ PPT第35~37頁

## 其他問題 Other Password Issues
+ 太多密碼要記，所以重複使用的密碼太多
+ 社交工程(Social Engineering)
	+ 釣魚網頁
	+ 社交詐騙
+ Error Logs 可能含有近似真實密碼的紀錄
+ Bugs、按鍵側錄(Keystroke Logging)、間諜軟體(Spyware)等

## 生物辨識 Something You Are
+ 需要便宜且可靠的辨識裝置
+ 雖然研究很活躍但是普及速度不快
+ ## 理想的生物特徵 Ideal Biometric
	+ ### 普遍性 Universal
		+ 大家都有的
	+ ### 區分性 Distinguishing
		+ 非常明確的區分
	+ ### 永久性 Permanent
		+ 一輩子永遠不會改變
	+ ### 可蒐集 Collectable
		+ 方便蒐集的特徵
	+ 安全，簡易使用等等

## 生物辨識的模式 Biometric Modes
+ 識別 Identification
	+ 一對多的比對
	+ Ex: FBI 的指紋資料庫
+ 認證 Authentication
	+ 一對一的比對
+ 識別比較難

## 註冊 Enrollment
+ 必須多做幾次，確保準確度
+ 是許多系統難以克服的困難

## 辨識 Recognition
+ 要快速、簡單而且準確

## 合作對象 Cooperative Subjects
+ 有時候對象是不合作的，造成正確率下降
+ 沒有良好的註冊，就沒有良好的辨別率

## 誤差 Biometric Errors
+ Fraud Rate: 把 A 誤認成 B
+ Insult Rate: 認為 A 不是 A
+ 假設更改辨識門檻：
	+ 如果標準設在 99%，則 Fraud Rate 低，Insult Rate 高
		+ Ex: 可能因為感冒造成聲音辨識不出來
	+ 如果標準設在 30%，則 Fraud Rate 高，Insult Rate 低
		+ Ex: 可能會讓雙胞胎被誤認
+ Equal Error Rate
	+ 當 Fraud Rate == Insult Rate

## 指紋 Fingerprint Biometric
+ 類型：迴圈(Loop)、中心(Whorls)跟拱橫紋(Arches)
+ 用一些手法強化圖片特徵，例如：加高對比值

## 手掌 Hand Geometry
+ 辨識手掌形狀、指寬、指長
+ 適合認證(Authentication)，但不適合識別(Identification)
+ 優點
	+ 快，只要1分鐘註冊，5秒鐘識別
	+ 兩隻手是對稱的
+ 缺點
	+ 不適用年紀太小或太大的人
	+ 高 Equal Error Rate

## 視網膜 Iris

## EER 比較 Equal Error Rate Comparison
+ 指紋 5%
+ 手 10^-3
+ 視網膜 10^-6
	+ 但不容易實現

## Something You Have
+ 擁有的東西
	+ Ex: 車鑰匙、信用卡
	+ Ex: 密碼產生器

## 辨識與認證方法 Identification & Authentication Methods
+ 兩步驟驗證 Two-Factor Authentication
+ 手機可以是一種密碼產生器

## Single Sign-On
+ 避免頻繁且多次的登入
+ Kerberos 是其中一種
	+ 使用對稱加密
	+ 提供 End-To-End 的安全性
		+ 傳送過程無法讀取內容
	+ 使用分佈式環境，但由中央伺服器執行
	+ 包含數據庫和認證過程
	+ 弱點包含：
		+ 單點故障(Single Failure)
		+ 效能瓶頸
		+ Session Key 會在客戶端上存在一小段時間，可能被盜用

## File & Data Ownership
+ Data Owner
	+ 承擔最大的責任，設定資料分級
+ Data Custodian
	+ 實施安全策略，通常是 IT 部門的成員
+ Data User
	+ 每天使用資料，要負責遵守安全政策

## 攻擊手法 Related Methods of Attacks
+ 暴力破解 Brute Force Attack
	+ 嘗試所有可能
+ 字典攻擊 Dictionary Attack
	+ 嘗試一些可能的組合
+ 詐騙攻擊 Spoofing Attack
	+ 釣魚網站

## 總結 Summary
+ Access Control Designs
	+ Mandatory
	+ Discretionary
	+ Non-Discretionary
+ Access Control Administration
	+ Centralized
	+ Decentralized
	+ Hybrid
+ Access Control Models
	+ State Machine Model
		+ Bell-LaPadula Model - Confidentiality
		+ Biba Model - Integrity
	+ Clark-Wilson Model
	+ Noninterference Model
+ Biometric
	+ Fingerprint
	+ Hand Geometry
	+ Iris