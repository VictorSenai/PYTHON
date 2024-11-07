import tkinter
import tkinter.messagebox

janela = tkinter.Tk()

janela.geometry("300x500")
janela.title("Calculo IMC")

texto_altura = tkinter.Label(janela, text = "Qual a sua altura")
texto_altura.pack(padx = 10, pady = 10)

e_altura = tkinter.Entry(janela)
e_altura.pack(padx=10, pady=10)

texto_peso = tkinter.Label(janela, text = "Qual o seu peso")
texto_peso.pack(padx = 10, pady = 10)

e_peso = tkinter.Entry(janela)
e_peso.pack(padx=10, pady=10)


def click():
    altura = float(e_altura.get())
    peso = float(e_peso.get())
    imc = round (peso / (altura**altura),2)
    tkinter.messagebox.showinfo("Calculo realizado",f"Vocé tem { e_altura.get()} de altura e pesa {e_peso.get()} o Seu IMC é {imc} ")
    print(f"oi")
   


botao = tkinter.Button(janela,text =" Seu IMC é  ", command = click)
botao.pack(padx = 10, pady = 10)


janela.mainloop()

