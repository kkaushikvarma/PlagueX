from tkinter import *
from PIL import Image, ImageTk
import nltk
from nltk.corpus import wordnet as wn
import PlagueX_2_0_main

import PlagueX_2_0_main_custom
import PlagueX_2_0_concept_corpus
import webbrowser

class Gui:
        
    def page1(self):
        
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 200)
        data_frame.pack(side = "top")
        R1 = Radiobutton(data_frame, text="From folder '/TestCases'", variable=var1, value=1,bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 10 bold"))
        R1.invoke()
        R1.select()
        R1.pack(side = "top")

        R2 = Radiobutton(data_frame, text="Custom Text:", variable=var1, value=2,bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 10 bold"))
        E1 = Entry(data_frame)
        E2 = Entry(data_frame)
        E3 = Entry(data_frame)
        E4 = Entry(data_frame)
        R2.pack(side = "top")
        E1.pack(side = "top")
        E2.pack(side = "top")
        E3.pack(side = "top")
        E4.pack(side = "top")
        def process():
            if var1 == 1:
                PlagueX_2_0_main.main()
            else:
                PlagueX_2_0_main_custom.main(E1.get(),E2.get(),E3.get(),E4.get())
            webbrowser.open_new("output.txt")
        def hood():
            data = PlagueX_2_0_main_custom.main(E1.get(),E2.get(),E3.get(),E4.get())
            self.tokens = data[0]
            self.nounset = data[1]
            self.concepts = data[2]
            self.scores = data[3]
            self.d1 = E1.get()
            self.d2 = E2.get()
            self.d3 = E3.get()
            self.d4 = E4.get()
            webbrowser.open_new("output.txt")
            window.destroy()
            self.page2()

        footer = Frame(main_frame, width = 600, height = 70, bg = "#ecf0f1")
        button1 = Button(footer, text = "Under the Hood", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 8, command = hood)
        button1.pack(side = "left")
        button2 = Button(footer, text = "Get Results", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") ,pady = 8, command = process )
        button2.pack(side = "right")

        footer.pack_propagate(0)
        footer.pack(side = "bottom")
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
    def page2(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5)
        data_frame.pack(side = "top")
        
        label1 = Label (data_frame, text = "Tokenized Text", width = 20, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 14 bold"))
        label1.pack(anchor = "nw")
        label2 = Label (data_frame, text = str(self.d1), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label2.pack(anchor = "nw",pady = 10)
        text1 = Label (data_frame, text = str(self.tokens[0]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text1.pack(anchor = "nw",pady = 3)
        label3 = Label (data_frame, text = str(self.d2), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label3.pack(anchor = "nw",pady = 10)
        text2 = Label (data_frame, text = str(self.tokens[1]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text2.pack(anchor = "nw",pady = 3)
        label4 = Label (data_frame, text = str(self.d3), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label4.pack(anchor = "nw",pady = 10)
        text3 = Label (data_frame, text = str(self.tokens[2]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text3.pack(anchor = "nw",pady = 3)
        label5 = Label (data_frame, text = str(self.d4), bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label5.pack(anchor = "nw",pady = 10)
        text4 = Label (data_frame, text = str(self.tokens[3]), bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text4.pack(anchor = "nw",pady = 3)
        
        def next():
            window.destroy()
            self.page3()
            
        
        
        footer = Frame(main_frame, width = 600, height = 120, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)
        button2 = Button(main_frame, text = "NEXT", width = 8, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 6, command = next)
        button2.pack(side = "bottom", pady =8)
        inspectlabel = Label(footer, text = "Inspect Integrity:", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") , pady = 8)
        inspectlabel.pack(anchor = "nw")
        E1 = Entry(footer)
        E1.pack(anchor = "center")
        ttext = StringVar()
        def np():
            pos = nltk.word_tokenize(E1.get())
            tokenized_text = nltk.pos_tag(pos)
            ttext.set(tokenized_text)
        
        button2 = Button(footer, text = "Get Tokens", width = 10, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , command = np )
        button2.pack(anchor = "center", pady = 4)
        text4 = Label (footer, textvariable = ttext, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 9"))
        text4.pack(anchor = "center",pady = 3)

        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
        
        
        
        
    def page3(self):
        window = Tk()
        main_frame = Frame(window, width = 600, height = 800)
        header = Frame(main_frame, width = 600, height = 70, bg = "#c0392b")
        header.pack_propagate(0)
        header.pack(side = "top")
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)

            # labels can be text or images
        img = Label(header, image=render, borderwidth = 0, highlightthickness =0)
        img.image = render
        img.place(x=0, y=0)

        var1 = IntVar()
        data_frame = Frame(main_frame, bg = "#ecf0f1", pady = 5)
        data_frame.pack(side = "top")
        
        label1 = Label (data_frame, text = "Concept Corpus", width = 20, bg = "#c0392b", fg = "#ecf0f1",relief = "groove", font = ("Helvetica 14 bold"))
        label1.pack(anchor = "nw")
        label2 = Label (data_frame, text = "Nouns Set", bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label2.pack(anchor = "nw",pady = 10)
        
        text1 = Label (data_frame, text = str(self.nounset), wraplength=200, bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text1.pack(anchor = "nw",pady = 3)
        
        label2 = Label (data_frame, text = "Reduced Concepts", bg = "#ecf0f1", fg = "#2c3e50", font = ("Helvetica 12 bold"))
        label2.pack(anchor = "nw",pady = 10)
        
        text1 = Label (data_frame, text = str(self.concepts), wraplength=200, bg = "#ecf0f1", fg = "#34495e", font = ("Helvetica 9"))
        text1.pack(anchor = "nw",pady = 3)
        
        def next():
            window.destroy()
            self.page2(E1.get(),E2.get(),E3.get(),E4.get())
            
        
        
        footer = Frame(main_frame, width = 600, height = 170, bg = "#c0392b")
        footer.pack_propagate(0)
        footer.pack(side = "bottom", pady = 8)
        nfooter = Frame(footer, bg = "#c0392b")
        nfooter.pack(anchor = "n")
        mfooter = Frame(footer, bg = "#c0392b")
        mfooter.pack(anchor = "n")
        button1 = Button(mfooter, text = "Under the Hood", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 12 bold") , pady = 8, command = next)
        button1.pack(side = "left", padx = 5)
        button2 = Button(mfooter, text = "Next", width = 10, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 13 bold") ,pady = 8, command = next )
        button2.pack(side = "right", padx = 5)
        inspectlabel = Label(nfooter, text = "Inspect Integrity: (Threshold = 2.02)", width = 30, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 11 bold") , pady = 8)
        inspectlabel.pack(anchor = "nw")
        E1 = Entry(nfooter)
        E1.pack(anchor = "center")
        E2 = Entry(nfooter)
        E2.pack(anchor = "center")
        
        ttext = StringVar()
        def checksim(synset1,synset2):
            score = 0
            for syn1 in synset1:
                for syn2 in synset2:
                    try:
                        ns = wn.lch_similarity(syn1,syn2)
                    except:
                        ns = 0
        #            ns = wn.wup_similarity(syn1,syn2)
                    if isinstance(ns, float):
                        if ns > score:
                            score = ns

    
            return(score)
        def np():
            w1 = E1.get()
            w2 = E2.get()
            score = checksim(wn.synsets(w1),wn.synsets(w2))
            print(score)
            ttext.set(score)
        
        
        button2 = Button(nfooter, text = "Check Concept Match", width = 20, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 10 bold") , command = np )
        button2.pack(anchor = "center", pady = 4)
        text4 = Label (nfooter, textvariable = ttext, bg = "#c0392b", fg = "#ecf0f1", font = ("Helvetica 9"))
        text4.pack(anchor = "center",pady = 3)

        
        main_frame.pack_propagate(0)
        main_frame.pack()
        window.mainloop()
        
    
    
a = Gui()
a.page1()
    