# Machine Learning Note

## 向量分析
+ 幾何學 + 代數 + 微積分 = 向量分析
+ 機器學習 = 大量資料 + 特徵(Feature) + 樣式(Pattern) + 推理法則
+ 推理法則：
	+ 分類 Classification
	+ 集群 Clustering
	+ 迴歸 Regression
	+ 加強 Reinforcement
+ 向量分析 -> 分析大量資料的工具

## 數學的量
+ 純量 Scalar
	+ a = 21
+ 向量 Vector
	+ v = [21, 35]
+ 張量 Tensor
	+ x = [[21, 35], [47, 58]]

# Linear Classifiers

## 區別函式 Discriminant Functions
+ 公式在 PPT Ch4 P.3
+ 一個用來表示分類器很有用的方法
+ 一個種類一個 Function
+ 產生一個決策區域(Decision Region)
+ 區域的邊邊就是決策邊界(Decision Boundary)

## 線性區別函式 Linear Discriminant Functions
+ 有權重向量(Weight Vector, D-Dimensional)
+ 有偏置/閥值(Bias/Threshold)
+ Two Category Case 就會有兩個權重

## 線性分類器 Linear Classifiers
+ PPT Ch4 P.9
+ 如何獲得最小的J
+ 梯度下降法 Gradient Descent
	+ 泰勒展開式 Taylor Expansion
	+ 基本策略
		1. 設定 Learning Rate h > 0 & Threshold e > 0
		2. 隨機初始化 X0 屬於 R 當作起始點，設定 K = 0
		3. do k = k + 1
		3.     xk = xk-1-n-Vf(xk-1) (梯度下降的操作)
		4. until |f(xk) - f(xk-1)| < E
		5. Return xk & f(xk)

## 感知器 Perceptron
+ 輸入多個訊號，再輸出一個訊號 yin，經過激發函式最後輸出 y
+ 感知器是類神經網路的基本
+ 激發函式 Activation Function
	+ 決定是否激發神經元的加總輸出
	+ 二元階梯 Binary Step Function
		+ f(x) =  1, x >= Theta
		+ f(x) =  0, x <  Theta
	+ 二極階梯 Bipolar Step Function
		+ f(x) =  1, x >= Theta
		+ f(x) = -1, x <  Theta
	+ 二元S型 Binary Sigmoid
		+ ![](https://i.imgur.com/kEZGTAx.png)
	+ 二極S型 Bipolar Sigmoid
		+ ![](https://i.imgur.com/qm30Zeh.png)
	+ 以上皆屬於非線性函數
	+ 不使用非線性函數，多層的神經網路分類功效會很差
	+ 例：圖上用了三層跟用了一層的效果一樣

## 訓練感知器 Training Perceptron
+ 被稱為感知器或神經元(Neuron)
+ 一種透過感知器演算法從 Training Vectors 學習的 Learning Machine
+ Perceptron Algorithm
	+ 計算出一個 w 滿足以下關係  
		![](https://i.imgur.com/xGSxtr7.png)
	+ 步驟
		1. 定義一個 Cost Function
		2. 選擇一個演算法去最小化 Cost Function
		3. 該最小值就是 w
	+ Cost Function 是分段的線性
	+ 一種感知器演算法的變形  
		![](blob:https://imgur.com/a2db3989-731f-4fe1-ab5d-96c7368389dd)
	+ 這是一種 Reward & Punishment 的形式
+ Least Squares Methods
	+ 如果 Class 是線性可分的，則感知器的 Output 為 ±1
	+ Small 在這裡代表均方誤差的小
	+ Rx 是自相關矩陣 Auto Correlation Matrix
	+ E[xy] 是互相關向量 Cross Correlation Vector
+ Multi-Class Generalization
	+ 根據 MSE(Mean Square Error) 計算出一個 M 表示線性區別函數
	+ MSE 有個重要的性質：g(x) 是一個均方誤差的估計值
+ Mean Square Error Regression
+ 偽逆矩陣 Pseudoinverse Matrix
	+ The solution 是最小平方和

## The Bias - Variance Dilemma
+ 分類器：ML 去預測 x 的 Label
+ 增加 Bias 會減少誤差，反之亦然
+ 複雜的模型會得到 Low-Bias 但是高誤差

## Logistic Discrimination
+ 透過線性函式計算相似率(Likelihood Ratios)
+ 未知的參數常用來估計最大相似率

# Training Algorithms for Linear Classifiers
+ 從樣本邊界獲得 Maximum Margin  
![](https://i.imgur.com/ruVJvvy.png)