import concept_corpus
import itertools
import tokenizer
class Mini_Corpus:
    def __init__(self, doc_data, noun_index):
        self.noun_index = noun_index
        self.doc_data = doc_data
        self.doc_combs = list(itertools.combinations(range(len(self.doc_data)), 2))
        self.match_data = self.match_detect()
        self.query_data = self.mini_queries(self.match_data)
        
    def match_detect(self):
        
        match_data = []
        for comb in self.doc_combs:
            matches = []
            for index_x, code_x  in enumerate(self.doc_data[comb[0]]):
                for index_y , code_y in enumerate(self.doc_data[comb[1]]):
                    if code_x == code_y:
                        matches.append((index_x, index_y))
            match_data.append(self.match_range(matches))
        return(match_data)
    
    
    def match_range(self,match_data):
        self.used = [[],[]]
#        self.used = []
        match_ranges = []    
        def range_gen(elmx,match_data):
            int_elmx = elmx
            for match in match_data:
                
                if match[0] not in self.used[0] or match[1] not in self.used[1]:
#                if match not in self.used:
                    if match[0]-elmx[-1][0] > 0 and match[0]-elmx[-1][0] < 3 and match[1]-elmx[-1][1] > 0 and match[1]-elmx[-1][1] < 3:
                        elmx.append(match)
                        self.used[0].append(match[0])
                        self.used[1].append(match[1])
#                        self.used.append(match)
                        return(range_gen(elmx,match_data))
            return(elmx)
        for element in match_data:
            if element[0] not in self.used[0] or element[1] not in self.used[1]:
#            if element not in self.used:
                elmx = []
#                self.used.append(element)
                self.used[0].append(element[0])
                self.used[1].append(element[1])
                elmx.append(element)
                rangex = range_gen(elmx,match_data)
                if len(rangex) >1:
                    match_ranges.append((rangex[0],rangex[-1]))
        return(match_ranges)
    
    
    def mini_queries(self,match_data):
        query_data = []
        for i in range(len(match_data)):
            comb_queries = []
            comb = match_data[i]
            d1 = self.doc_combs[i][0]
            d2 = self.doc_combs[i][1]
            for rangex in comb:
                newrange = ((self.noun_index[d1][rangex[0][0]],self.noun_index[d1][rangex[1][0]]),(self.noun_index[d2][rangex[0][1]],self.noun_index[d2][rangex[1][1]]))
                comb_queries.append(newrange)
            query_data.append(comb_queries)
        return(query_data)
            
            
            
            
#            
#        
#        
#        
#
#    
#Raw_Text = "Along with the degradation of labor, Gandhi believes that capitalism imbues greediness in every human being. The introduction of machinery makes man a limitless consumer of commodities leading to the multiplication of wants and desires. This further leads to unhealthy competition which ultimately results in violence. Therefore, he believes that violence is inherently embedded in the western civilization which promotes capitalism and hence considers capitalism to be immoral, driven only by comforts and bodily welfare"
#
#
#Raw_Text2 = "According to Gandhi's beliefs, alongside degradation of labor, capitalism also permeates greediness in all humans. Induction to machinery makes humans boundless users of commodities which results in growth of needs and desires. Further, this results in unhealthy competition which eventually leads to brutality. Thus, he concludes that capitalism is unethical and is driven just by comfort and personal well being as violence is innately implanted in western ideologies which promotes capitalism "
#
#
#text1 = tokenizer.Tokenizer(Raw_Text)
#text2 = tokenizer.Tokenizer(Raw_Text2)
#
#a1 = text1.tokenized_text
#a2 = text2.tokenized_text
#x = concept_corpus.Concept_Corpus([text1.nounset,text2.nounset])
#
#print(a1[3:12])
#print(a2[7:14])
#print("")
#
#print(a1[21:28])
#print(a2[21:27])
#print("")
#
#print(a1[55:65])
#print(a2[69:78])
#print("")
#
#y = Mini_Corpus(x.doc_data,[text1.noun_index,text2.noun_index]) 
#print(y.match_data)
#print(y.query_data)


