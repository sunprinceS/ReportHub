* p5: Meta Learning 的目標是什麼呢？簡單來說就是 learning to learn。一般通常的 learning 說的是，給定一大筆 data，或者說一個 dataset，我們希望能 learn 一個 model 在沒看過的 data 上也能 generalize 的很好。那 meta-learning 想做的則是給定一大筆想學的 task ，每一個 task 包含了一個 dataset，以及一個衡量這個 task 學習成效的 metric，通常這個 dataset 都不會太大。給定一個新的 task，我們希望 model 能 build on 當中 limited-size 的 dataset，去完成我們賦予他的 task。
這個 equation 所表示的是就是我們希望找到這樣的一組參數，在 sample 出來的 task當中，都能在 對應的 metric 上表現的很好。

* 上面的 formulation 有點抽象，我們來看一個常見的應用， few-shot classification，首先我們先 hold 部份的 label 起來供 meta-testing 的時候使用，所以只從一個 label 的 subset 去 sample task 出來，而每個 task 都包含了training data和 testing data，traiing data 是S，又叫做 support set，而 testing data 則是以 B表示，那我們希望能 maximize classification 的 performance。

* 那這裡我參考了之前 Vinyals 在 NIPS 給的 talk，對目前為止所有 meta-learning 的
  方法做了個分類，有以下三種，再接下來的幾張投影片會依序介紹。

* 那第一個是 metric-base 的方法，跟 nearset neighbour 的想法很像，predict 出來的probability over y 是 wieghted sum of 那些在 support set 裡頭的 label。那這個weight 怎麼決定呢？由一個 kernel function 決定，而這個 kernel function 做的事就是把原先的 input 打到 latent space 上後再去衡量similarity，either Euclidean distance 或 cosine distance 或 whatever。 

那通常都是 design model 架構，使得這個 model 主要的目的就是為了比較 similarity 所設計的。像是 simaset network，就是用兩個 weight tying 的 feature encoder，去算 xi 和 xj 在 latent space 上的 L1 distnace，在乘上一個 weight，過 sigmoid 後當成 probability
  而 prototypical network 的想法也是類似，把 x 打到 latent space 上，找到每個對應的labelｙ 在 latent space 上的 中心點，當一筆新的 data 進來的時候，把他跟每個中心點的距離 softmax 後當成 probability。

所以我們可以說，這類的 model meta-learn 的東西其實就是 feature encoder ，並相信
這個 encoder 是可以 generalize cross task 的。

* model-based的方法，就是我直接 learn 一個 condition on support set 的 model ，
  當新的 x 進來後直接輸出。 (其實上面提到的 metric-based 的方法可以算是這個方法
  的 special case 啦，個人認為)。所以說這類的方法做的事情呢，其實就是如何去
  condition on support set。這裡介紹兩種實做方式，一種是用 external
  memory 去存 support set 的資訊，常見的架構是用 Neural Turing Machine ，他所
  meta-learn 的事情其實就是讀寫的時候，這個 weight 該怎麼設這樣，像是有一篇他在
  write的時候，他會優先寫最近剛讀的位置，或者是最少被讀寫的位置，LRUA，Least
  Recently Used Access，那之前君璇也有 intro 過一篇 superised 的方法，就是只會寫
  那些夠 superise 的那些 data， ground truth label predict 出來的機率卻很低的那
  些 sample。
  
  那另一種實做方式呢？就是一個蠻 DL 的方式，他 condition on S 的方式，就是在
  predict 時，直接把 support set 跟input x 直接灌進一個 temporal convolution
  layer 中做prediction...

  所以總結一下，我覺得這類方法 meta-learn 的事情是使用 support set 的策略，可能是
  reading 或 writing 的 weight ，或某個 convolution layer learn 到的黑魔法。

* 那最後一類方法則是 optimization-base 的方法，他會先利用一個另外的 model ，不妨
  叫做 meta-learner model，condition on S，去 predict 在每個 task 裡， learner
  model 的些 hyper-parameter，像是...

  那常見的幾種方法都是在 gradient 上做文章，像是家喻戶曉的 MAML，就是利用
  利用在 support set 上得到的 gradient 去找一個比較好的 intial point，希望在
  testing 的時候，只要iterate個幾步就能得到好的 performance。

  那他還有很多變形，像是 probilistic 版本的，就是說今天我們輸出的是一個 initial
  point 的 distribution，你在算 loss 的時候就是要多加一個 minimize KL divergence
  of support set 和 testing set 的 term這樣。那另外一個方向則是 first order 版本
  ，如果你有自己照著 paper 上的推導推過一遍，你會發現我們要拿來更新 intial point
  的 gradient 會有一個二街微分的項，所以這類的方法就是把這個像給丟到，那他的另外
  一個延伸是 Reptile，這裡就先不展開了，如果有需要等等我們可以討論。

  所以總結一下，這類方法就是在 meta-learn 給定一個 task，如何找出好的
  hyper-parameter 。

* 那在最後這個 overview 收尾之前，我引了一下 Finn 他的博論來說一下一個好的
  meta-learning 做的性質，blahblah

* 那這篇 paper 想解決什麼樣的問題呢？簡單來說他想利用 meta learning 來去 improve
  unsupervised learning 所 learn 到的 representation 在 downstreamk 的
  performance。

  一般 unsupervised learning 的目標不外乎 capture data 的 distribution 去做
  generative modeling，或者說就像這篇說的去讓 downstream task 做的更塊更好。但在
  後者的應用上，我們的 objective 卻依舊是 reconstruction, distanglement 之類，不
  是非常的一致，所以我們想利用 Meta-Learning 去解決。那這篇是要透由學習 update
  rule 來處理這件事。

* 那基本流程是這樣

* 首先是 Meta-Objective，也就是今天model要學的到底是什麼。這裡呢，我們希望說
  model 可以根據少少的資料點去學一個 linear regression 的 weight，在看到新的
  data point 的時候，能夠 predict 的不錯。

* 那 update rule呢？
  他的 highlight 是說，這個方法很 general ，可以 generalize 到任何架構的 model
  上，而他又是 biologically-motivated，他的每個 neuron 的更新方式是根據pre和post
  的突觸，但其實說穿了跟 Backpropogation 其實是一碼子事啦...

* 那我概略說一下他的更新流程，今天 base model 用 phi, W,V 去描述，這個V是
  backprop的時候用的，以前我們都會直接跟W tigh 在一起，用W transpose 去表示。

  這裡的 x 和 z 呢？就是 forward pass 會產生的 tensor，分別表示在過 activation
  之前後的 tensor。而 delta 是 erro signal，是算 backward pass 的產物，那他會透由另外一個
  tensor h 去算出來，那這個 h呢， 一般的 SGD 就是由前一層的 error signal 去算出
  來，那這裡是一個 function of ...blahblah。在最後更新 W 時，則是...blahblah，

* 那過來講他的實驗，首先他做了一件事情， feature permutation，那做這件事的目的，
  是為了讓 model 所 learn 到的 rule 是 feature-invariant 的，不會說換了個
  feature (這裡explicitly 是直接 permutation) 就會完全 learn 不起來。

* 那這篇 paper 先做了個實驗，講述了現在 representation learning 方法的缺點。

* 那個長條圖的實驗解釋： 要看的比較主要有兩個，一個是VAE vs learned，與
  supervised vs learned，VAE 就是先用所有的 data ，把每個 meta-train 的所有
  unlabeled data union 起來 train 一個VAE，在用這個 learn 到的 embedding 在其上
  做 few-learning。而 supervised 則是根據少少的 few-shot data 直接 train

* Meta-overfitting，如果我們把 train 在影像上的 encoder update rule apply 到 NLP
  上呢？結果是這樣，看起來 feature shuffling 並沒有真的 decoorelate domain 的影
  響。

* Across different depth 和 number of unit，一開始 initial 很差，unsupervised
  update 迭代幾次後， accuracy 越來越好。

* 以下我會介紹兩篇分別在兩個面向跟這篇很相近的paper，做完比較之後再給 conclusion
  。

* ULML，這篇是之前要聞 intro 過的，他想解決的問題跟剛剛report的一樣，不過用了完
  全不同的方式。那這篇怎麼做的呢？既然你沒有 label，那就自動生 label 出來。
  首先，先用所有的 unsupervised data learn 一個 embedding ，把x打到 latent space
  上。接著在 latent space 上做 clustering，賦予 input label，那有了 label 之後，
  我們就可以使用之前提到的 meta-learning 方法了。

* 如果我的理解沒錯的話，我覺得這篇做的事情，其實是在 meta-learn 如何在給定的
  embedding 下，做好想完成的 task。標題其實有點誤導人，因為他根本沒有 improve
  embedding algorithm，他自己paper的discussion也提到了他們的結果 significantly depend on
  embedding generating procedure。其實你在 input space 做 clustering 也是可以，
  其實有就是一個 embedding weight matrix 為 identiry 的特例，只是可能不那麼具 semantics，結果可能會不好。

* 那另一篇 Opimization as a model 則是剛剛前面跳過的 LSTM-Meta Learner
* 首先觀察到SGD和LSTM cell update 相似的地方，所以這篇做的事就是把 optimizer 換
  成 LSTM，那其中的 input / forget gate 則是 function of ...blahblah

* 那其實這兩篇本質上非常類似，因為 optimizer 提供的就是一個如何更新的 rule，但這
  篇並沒有處理在沒有 loss 的情況下如何去 learn 這個 optimizer 。所以我覺得今天 report 這篇最主要的貢獻其實是在於他提供了一個 unsupervised learning 的 meta-earing 框架















* ULML 那篇 design 的 representation，因為有做 clustering 的關係，所以有幾何上的語義，而 learn update rule 那篇則沒有
* ULML 在 meta-test 時，不會在 retrain representation，meta-test僅僅是K-shot
  training examples，然後test samples
