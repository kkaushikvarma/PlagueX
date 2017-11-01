import concept_corpus
import itertools
import tokenizer
class Mini_Corpus:
    def __init__(self, doc_data):
        self.doc_data = doc_data
        self.match_data = self.match_detect()
        self.used_spaces = []
        
    def match_detect(self):
        doc_combs = list(itertools.combinations(range(len(self.doc_data)), 2))
        match_data = []
        for comb in doc_combs:
            for index_x, code_x  in enumerate(self.doc_data[comb[0]]):
                for index_y , code_y in enumerate(self.doc_data[comb[1]]):
                    if code_x == code_y:
                        self.tree_alg(comb[0],comb[1],index_x, index_y)
        
    def tree_alg(self, docID_1, docID_2, range_1, range_2):
        
        left_range = []
        right_range = []
        
        print(docID_1, docID_2, range_1, range_2)
        

    
Raw_Text = "As St.Francis high school dropout myself and now a mother of six children, one kid being a recent high school graduate, one just entering high school, and another soon to enter high school in a year with three others trailing behind, I often find myself reflecting on my high school years. Why was I so unmotivated to finish high school? What made me want to go back to school? The question it all comes down to is, what can be done to prevent high school students from losing motivation, detouring them from dropping out and not becoming just another statistic? Motivating high school students may seem like a daunting task; however, it is easier than we think by encouraging them, helping them acquire their own aspirations, and making school interesting. Students will not only meet graduation requirements, but they will feel a sense of accomplishment while doing it."


text1 = tokenizer.Tokenizer(Raw_Text)
x = concept_corpus.Concept_Corpus(text1.nounset,text1.nounset)
print(x.n_reduced)



y = Mini_Corpus(x.doc_data)

print(y.doc_data)