import sparknlp

spark = sparknlp.start(aarch64=True)

lemmatizer = LemmatizerModel.pretrained("lemma", "fa") \
    .setInputCols(["token"]) \
    .setOutputCol("lemma")

nlp_pipeline = Pipeline(stages=[document_assembler, tokenizer, lemmatizer])
light_pipeline = LightPipeline(nlp_pipeline.fit(spark.createDataFrame([['']]).toDF("text")))
results = light_pipeline.fullAnnotate(['فرماندهان	فرماندهی	فرمانده	فرمانده‌ای	فرماندهٔ	فرماند



from spacy.lang.fa.examples import sentences
docs = nlp.pipe(sentences)