import hazm
sent2vec_model_path = 'sent2vec.model'


wordEmbedding = hazm.WordEmbedding(model_type='fasttext')
wordEmbedding.load_model('word2vec.bin')
# wordEmbedding.doesnt_match(['سلام', 'درود', 'خداحافظ', 'پنجره'])
#
# wordEmbedding.doesnt_match(['ساعت', 'پلنگ', 'شیر'])
