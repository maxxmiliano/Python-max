import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela= customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("fazer login")

    texto = customtkinter.CTkLabel(janela, text= "fazer login")
    texto.pack(padx=10, pady=10)

    email= customtkinter.CTkEntry(janela,placefolder_text="seu email")
    email.pack(padx=10, pady=10)
    


