
#Class Features
#    ===>    Input: rawtext in string
#    ===>    Convert raw text into tokens
#    ===>    Assign Part-Of-Speech tag to each of the tokens
#    ===>    self.TokenizedText           ==>     Access all token-POS pairs in indexed order for matching.
#    ===>    self.UniqueTokenizedText     ==>     Access all unique token-POS pairs for corpus generation


import nltk
class Tokenizer:
    def __init__(self,rawtext):
        pos = nltk.word_tokenize(rawtext)
        self.TokenizedText = nltk.pos_tag(pos)
        self.UniqueTokenizedText = list(set(self.TokenizedText))
                
#Un-comment below sections for testing code integrity:
#Raw_Text = "As a high school dropout myself and now a mother of six, one child being a recent high school graduate, one just entering high school, and another soon to enter high school in a year with three others trailing behind, I often find myself reflecting on my high school years. Why was I so unmotivated to finish high school? What made me want to go back to school? The question it all comes down to is, what can be done to prevent high school students from losing motivation, detouring them from dropping out and not becoming just another statistic? Motivating high school students may seem like a daunting task; however, it is easier than we think by encouraging them, helping them acquire their own aspirations, and making school interesting. Students will not only meet graduation requirements, but they will feel a sense of accomplishment while doing it."
#text1 = Tokenizer(Raw_Text)
#print(text1.TokenizedText)