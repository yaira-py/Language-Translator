import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from deep_translator import MyMemoryTranslator

class Translator:
    def __init__(self,root):
        self.root=root
        self.root.title('Translator')
        self.root.geometry('500x550')
        self.root.configure(bg="#dad7d7")

        self.languages={'English':'en-US','Hindi':'hi-IN','Tamil':'ta-IN',
                        'French':'fr-FR','Spanish':'es-ES','German':'de-DE','Japanese':'ja-JP'}

        self.title_lb=tk.Label(self.root,text='Language Translator',font=('Arial',16,'bold'),bg='#dad7d7',fg='#333333')
        self.title_lb.pack(pady=10)

        self.input_entry=tk.Text(self.root ,width=35,height=6,font=('Arial',12,'bold'))
        self.input_entry.pack(pady=20,padx=15)

        self.frame_btn=tk.Frame(self.root)
        self.frame_btn.pack(pady=10)

        self.text_btn=tk.Button(self.frame_btn,text='text to ',font=('Arial',12,'bold'),bd=0,relief='flat',bg='#dad7d7',fg="#3C4B74")
        self.text_btn.pack(pady=10,side='left',padx=10)

        self.to_btn=tk.Button(self.frame_btn,text= '➡️',font=('Arial',12,'bold'),bd=0,relief='flat',bg='#dad7d7',fg="#3C4B74")
        self.to_btn.pack(pady=10,side='left',padx=10)

        self.lang_btn=ttk.Combobox(self.frame_btn,values=list(self.languages.keys()),state='readonly',width=12)
        self.lang_btn.set('Hindi')
        self.lang_btn.pack(pady=10,side='left',padx=10)

        self.gen_btn=tk.Button(self.root,text='Generate',font=('Arial',14,'bold'),bg="#5369A5",fg='white',command=self.translate)
        self.gen_btn.pack(pady=10)

        self.output_entry=tk.Text(self.root,width=35,height=6,font=('Arial',12,'bold'))
        self.output_entry.pack(pady=15,padx=15)

    def translate(self):
        text=self.input_entry.get('1.0','end-1c')
        if not text.strip():
            messagebox.showerror('Invalid','pls enter text to translate')
            return

        target_lang=self.languages[self.lang_btn.get()]
        translated = MyMemoryTranslator(source='en-US',target=target_lang).translate(text)
       
        self.output_entry.delete('1.0','end')
        self.output_entry.insert('1.0',translated)
        



if __name__=="__main__":
    window=tk.Tk()
    app=Translator(window)
    window.mainloop()
