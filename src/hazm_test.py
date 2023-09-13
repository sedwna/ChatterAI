import hazm

wordEmbedding = hazm.WordEmbedding(model_type='fasttext')
wordEmbedding.load_model('fasttext_skipgram_300.bin')


wordEmbedding.doesnt_match(['سلام' ,'درود' ,'خداحافظ' ,'پنجره'])

wordEmbedding.doesnt_match(['ساعت' ,'پلنگ' ,'شیر'])
