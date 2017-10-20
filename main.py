import tokenizer
import concept_corpus

SampleText = "As a high school dropout myself and now a mother of six, one kid being a recent high school graduate, one just entering high school, and another soon to enter high school in a year with three others trailing behind, I often find myself reflecting on my high school years. Why was I so unmotivated to finish high school? What made me want to go back to school? The question it all comes down to is, what can be done to prevent high school students from losing motivation, detouring them from dropping out and not becoming just another statistic? Motivating high school students may seem like a daunting task; however, it is easier than we think by encouraging them, helping them acquire their own aspirations, and making school interesting. Students will not only meet graduation requirements, but they will feel a sense of accomplishment while doing it."

tokens = tokenizer.Tokenizer(SampleText)
tokenized_text = tokens.tokenized_text
#print(tokenized_text)
tokens_nouns = tokens.nounset
#print(tokens_nouns)
corpus = concept_corpus.Concept_Corpus(tokens_nouns,tokens_nouns)
new_corpus = corpus.reduced_corpus()
#print(new_corpus)

