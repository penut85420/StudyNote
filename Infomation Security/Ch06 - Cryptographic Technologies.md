# Chapter 6 - Cryptographic Technologies

## Crypto
+ Cryptology - 密碼學，指的是研究密碼的這門學問
+ Cryptography - 加密，只包含加密的演算法
+ Cryptanalysis - 解密，只包含解密的演算法
+ Crypto - 以上全部

## Speak
+ A cipher or cryptosystem is used to encrypt the plaintext.
	+ Cipher 或 Cryptosystem 是用來加密(Encrypt)文本(Plaintext)的。
+ The result of encryption is ciphertext.
	+ 加密出來的結果叫做密文(Ciphertext)。
+ We decrypt ciphertext to recover plaintext.
	+ 將密文解密(Decrypt)來復原文本。
+ A symmetric key cryptosystem uses the same key to encrypt as to decrypt.
	+ 對稱金鑰系統(Symmetric Key Cryptosystem)使用一把相同的金鑰(Key)來加密或解密
	+ 密文要寄給 10 個人就需要 10 把 Keys。
+ A public key cryptosystem uses a public key to encrypt and a private key to decrypt
	+ 公開金鑰系統(Public Key Cryptosystem)也可稱為非對稱加密，只需要一把公鑰來加密，和一把私鑰來解密。
	+ 無論寄給多少人，都只需要保管兩把 Keys。

## Kerchoffs Principle
+ 加密演算法是完全公開的。
+ 攻擊者非常熟悉這個系統。
+ 只有 Keys 是保密的。

## 傳統加密法
+ Simple Substitution
	+ 單純的代換法，有一個代換表。
+ Caesar's Cipher
	+ 透過位移法加密，例如 A 位移 3 變成 D。
+ 以上兩種方法可以用英文字母頻率破解。

## Cryptanalysis
+ 如果最好的破解方法是嘗試所有可能，那就是個安全(Secure)的加密系統。
+ 如果有任何破解捷徑，那這個加密系統就不安全(Insecure)。
+ 所以一個 Insecure 的系統可能比 Secure 更難破解。

## Double Transposition
+ 用二維陣列來打亂原文順序。
+ ![原文](https://i.imgur.com/LuXi6Ju.png)→![密文](https://i.imgur.com/F3FqErn.png)
+ Key 表示為 (3, 5, 1, 4, 2) & (1, 3, 2)

## One-Time Pad
+ 主要使用 XOR 做運算。
+ Encryption
	+ Plaintext XOR Key = Ciphertext
	+ ![Example](https://i.imgur.com/ufMK7hI.png)
+ Decryption
	+ Ciphertext XOR Key = Plaintext
	+ ![Example](https://i.imgur.com/RF8v1FJ.png)

## 目的
+ 機密性 Confidentiality
	+ 訊息的內容經過加密後要被隱藏(Concealed)。
+ 完整性 Integrity
	+ 確認接收到的就是寄出去的。
+ 不可否認性 Nonrepudiation
	+ 寄件者不能表示他沒有發送訊息。
+ 認證 Authentication

## 加密演算法 Cryptographic Algorithms
+ 分為對稱和非對稱兩種。
+ 文本 > 加密 > 密文 > 解密 > 文本。
+ 早期會使用含糊的方式增加安全性，但現在系統都比較嚴格而且公開。

## 對稱演算法 Symmetric Algorithms
+ 也稱之為 Secret Key Cryptosystems。
+ 雙方都要知道 Key。
+ Key 也稱為 Shared Secret Key 或 Secret Key。
+ Key Length，代表 Key 的 Bits 數，是最重要的部分。
	+ 越長的 Key 保護程度也越高。
	+ 最常見的對抗手法是暴力破解。
	+ 長度為 n 的 Key 就有 2^n 種組合。

## DES - Data Encryption Standard
+ 美國的一種加密標準。
+ 56 Bits 的 Key Length。
+ 有四種 Mode 的操作，因為加密訊息過長，需要分段處理與打亂。
+ 但是現在 56 Bits 已經不夠長，所以現在使用 Triple DES (3DES)。
	+ 把 DES 重複做三次。

## DES 規格
+ DES 是一種費斯妥密碼(Feistel Cipher)。
	+ 64 Bits Block
		+ 固定加密 64 Bits的明文。
	+ 56 Bits Key Length
	+ 16 回合
	+ 每個回合產生 48 Bits 的 Subkey
+ 安全性主要依靠 S-Boxes
	+ Map 6 Bits to 4 Bits
	+ ![S-Boxes](https://i.imgur.com/npZDoXS.png)
	+ 給定6位元輸入，將首尾兩個位元和中間四個位元作為條件進行查表，最終獲得4位元輸出。
	+ Ex: 以 011011 做為輸入，將首尾兩個位元 01 和中間的位元 1101 進行查表，輸出 1001。

## DES 變化
+ 3DES 有比較強的保護，可能使用 2 或 3 把 Keys。
	+ 3DES-EEE (Encrypt-Encrypt-Encrypt) 使用三把 Keys。
	+ 3DES-EDE (Encrypt-Decrypt-Encrypt) 使用 1 ~ 3 把 Keys。

## AES - Advanced Encryption Standard
+ 是國家標準研究院(National Institute of Standards, NIST)贊助的比賽中獲獎的演算法。
+ AES 允許使用者選擇 3 種不同長度的 Keys
	+ 128, 192 或 256 Bits。
	+ 越長越安全。
+ Block Size: 128, 192 or 256 Bits
+ Key Length: 128, 192 or 256 Bits
+ 10 ~ 14 回合，每個回合使用四個 Functions
	+ ByteSub (Nonlinear Layer)
		+ 就是 AES 的 S-Box。
		+ 用前四個 Bits 和後四個 Bits 查表。
		+ ![ByteSub](https://i.imgur.com/Cyi9rFX.png)
	+ ShiftRow (Linear Mixing Layer)
		+ 向左 Shift
		+ "mnop" Shift 1 => "nopm"
	+ MixColumn (Nonlinear Layer)
		+ 對每個Column做非線性、可逆的操作
	+ AddRoundKey (Key Addition Layer)
		+ 運算：Subkey XOR Block
		+ Subkey 是用 Key Schedule 演算法產生的。
+ 解密部分 Decrypt
	+ AddRoundKey 只要再做一次 XOR 就好。
	+ MixColumn 是 Invertible 的查表。
	+ ShiftRow 照原方向轉回去就好。
	+ ByteSub 也是可逆的查表。

## 非對稱加密演算法 Asymmetric Algorithms
+ 也可稱為 Public Key Cryptosystems。
+ 數學運算出兩把 Keys，公鑰和私鑰。
+ 用公鑰加密的訊息只能以私鑰解密。
+ 公鑰可以公開讓大家都可以加密自己的訊息。
+ RSA, Rivest Shamir Adelman Algorithm
	+ 最廣為人知的非對稱加密演算法。
	+ 依靠大質數很難被因數分解。
+ PGP, Pretty Good Privacy
	+ 跨平台的方案。
	+ 包含了許多加密演算法在內，也有 RSA
	+ 支援分散式公鑰管理的架構。

## 信任的網頁 The Web of Trust
+ Keys 的交換是個困難的問題。
	+ 在 PGP 之前，必須在離線狀態下交換 Keys。
+ PGP 加上 Web of Trust 讓使用者可以判斷公鑰的真實性。
+ 四個信任等級：
	+ 隱性信任 Implicit Trust
	+ 充分信任 Full Trust
	+ 邊際信任 Marginal Trust
	+ 不可信任 Untrusted

## 對稱與非對稱式加密的比較
+ 對稱式加密不好擴展。
+ 非對稱加密比對稱加密慢。
+ 對稱式加密在通訊電路上表現傑出，例如虛擬私人網路。
+ 非對稱式加密在用戶數量多的時候比較實用。

## 數位簽章 Digital Signatures
+ 替加密系統增加完整性和不可否認性。
+ 不可否認性只能在非對稱式加密上執行。
+ 數位簽章的創建：
	+ 使用雜湊函式來產生一個獨特的訊息摘要。
	+ 經常使用 SHA 跟 MD 演算法。
	+ 使用私鑰來加密訊息摘要。
+ 數位簽章的驗證：
	+ 收件人解密訊息獲得文本與數位簽章。
	+ 收件人使用相同的雜湊函式來創造新的訊息摘要。
	+ 收件人使用寄件人的公鑰解密數位簽章獲得寄件人的訊息摘要。
	+ 收件人比對兩個訊息摘要，如果相同就驗證成功。
	+ 如果不同，可能是惡意的訊息，也可能是傳送錯誤。

## 數位憑證 Digital
+ 數位憑證是第三方認證的擔保。
+ 第三方負責驗證發件人的身份。
+ 憑證頒發機構 Certification Authorities
	+ 常見的有 VeriSign 和 Thawte。