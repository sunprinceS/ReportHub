* ProtoNet 與 MatchNet 在 1-shot 的情形下是等價的
* MANN 的 LRUA 全名叫做 Least Recently Used Access， writing 時優先寫最近讀的時
  候用過的位置或最少被讀寫的位置
* ULML 那篇 design 的 representation，因為有做 clustering 的關係，所以有幾何上的語義，而 learn update rule 那篇則沒有
* ULML 在 meta-test 時，不會在 retrain representation，meta-test僅僅是K-shot
  training examples，然後test samples
* 所以我們不會說 "Unsupervised Learning"，因為 unsupervised 的部份根本沒有learning :p
