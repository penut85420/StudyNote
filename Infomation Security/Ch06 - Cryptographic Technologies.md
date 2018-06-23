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
![原文](https://i.imgur.com/LuXi6Ju.png)
↓
![密文](https://i.imgur.com/F3FqErn.png)