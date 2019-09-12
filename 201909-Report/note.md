* Meta Learning 的 objective 是什麼呢？ 以下我們定義 theta 為想優化的模型參數，D
為 dataset 或者說 task，而 A 則是一個衡量給定一組參數在 dataset D 表現好度的函數，那 meta
learning 的目標是希望所 learn 的這組參數，平均而言，在每個 dataset 上都能有不錯
的表現

* 以下介紹各種方法
  * metric-based: 目前應用在 classification 的問題上，learn 一個 feature encoder
  * model-based: learn 一個 condition on support set，或者說  meta-training 的
    training set 的 model，目前看到的方法除了簡單粗暴的用 RNN 來 encode support
    set，也有用 memory network 的方法。
  * optimization-based 的方法，主要是 meta-learn training 的各個 module，像是
    optimizer、 initial weight 、hyper-param

* Motivation: 在對 task 之間的 relation 一無所知的情況下，只能遷就於大家都一樣的
  方法，但如果我們對 task 有一些 prior knowledge 呢？像是知道他的一些 meta data
  ，像是文字上的描述，或 normalize 過的 sample 等等

* 考慮兩個極端，第一種就是剛剛所說的，這組參數很 general，但卻沒辦法在特定 task
  上 adapt 的很好

* 以下會介紹幾種 task conditioning 的實做方法，
  * 第一種呢？是先 learn 一個額外的 encoder 去 encode task，得到一個這個 task 的
    representation，可能 jointly 一起 learn 或 offline learn ，那之後的 sample
    會先 condition on 這個 representation ，才去進行下游的 meta learning

      * TADAM：這個額外的 encoder 會去 encode 每個 sample，而我們average over task
      裡頭的每個 class 的每個 sample 的 embedding 去當做這個 task 的
      representation

      * CAML: offline learn 一個 prototype network，得到每個 class 的 prototype
        ，利用這個 prototype 過另一個 NN，輸出要拿來 normalize sample x_i 的
        mean 和 variance

      * CTM: 先利用 support set 得到一個 對 channel 做 attention 的 weight，利用
      這組 weight 去 attend over support set 和 query set，再做 metric learning

      想法就是利用對 task 的一些認知，去抽出更 discriminative 的 feature，讓後面
      的 model 更好 learn

    * 另一種則是 cross-modality，主要借用了 zero-shot 的想法

    * 剛剛所提到的是在 feature 上動手腳，那這篇則是在參數上動手腳，是我之前
      intro 過個 hierarchical structured meta learning

* 在語音或 NLP ，我們對 task 的定義會更明確一點，
  * lang2vec: phonology 上，syntax 上，geographic 上






* Motivation 是什麼呢? 以下為了解釋方便，麻煩大家用 learn initial weight 的 meta
  learning 方法來想。直覺上來說， meta learner 是比較 high-level的
  ，那他應該可能要比 task learner 要有更高的 capacity，但現有的方法像是 MAML 或
  Reptile ，是都使用相同的 parameter，在相同的 space 上去做 search。

* 說白了，就是限制 task learner 的 freedom，
  左圖是一個 feedforward 的 network，其中有塗色的是表示 task learner 可以改的，
  那這個 output 有三個 dimension，不過能動的只有兩個 cell的 output ，所以相當於
  是只能在原先 space 的 subspace 上去移動，像右圖
  其實跟 task conditioning 的想法就是一體兩面


