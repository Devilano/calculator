from tkinter import *
import googletrans
import textblob
from tkinter import ttk,messagebox




root = Tk()
root.title("Wagle-translator")
#root.iconbitmap("c:/gui/wagle.ico")
root.geometry("880x300")


def translate_it():
    #Delete any previous translation
    translate_text.delete(1.0,END)
    try:
        # Get Language from dictionary keys
        # Get the fom language key
        for key,value in language.items():
            if (value == original_combo.get()):
                from_language_key = key

          #Get the to language key
        for key, value in language.items():
            if (value == translated_combo.get()):
                to_language_key = key
         #turn original text into a textblob
        words = textblob.TextBlob(original_text.get(1.0,END))

        #Translate Text
        words = words.translate(from_lang=from_language_key, to=to_language_key)

        #output translated text to screen
        translate_text.insert(1.0,words)


    except Exception as e:
        messagebox.showerror("Translator",e)


def clear():
     #Clear the text boxes
     original_text.delete(1.0,END)
     translate_text.delete(1.0,END)

#language_list=(1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)
# Grab language list from GoogleTrans
language =googletrans.LANGUAGES

# Convert to list
language_list=list(language.values())





# Text Boxes
original_text = Text(root,height=10,width=40)
original_text.grid(row=0,column=0,pady=20,padx=10)

translate_button =Button(root,text="Translate!",font=("Helvetica",24),command=translate_it,bg="orange")
translate_button.grid(row=0,column=1,pady=20,padx=10)

translate_text= Text(root,height=10,width=40)
translate_text.grid(row=0,column=2,pady=20,padx=10)

# Combo boxes
original_combo =ttk.Combobox(root,width=50,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)

translated_combo=ttk.Combobox(root,width=50,value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)

# Clear button
clear_button= Button(root,text="Clear",command=clear,bg="lightblue",width=7)
clear_button.grid(row=2,column=1)





root.mainloop()