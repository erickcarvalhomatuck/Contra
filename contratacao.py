import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

class CandidatosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SRE Pouso Alegre - Superintendência Regional de Ensino")
        self.root.state("zoomed")
        self.root.configure(bg="#f0f0f0")

        # Nome dos arquivos CSV para salvar os dados
        self.lista_nomes = [
            "Língua Portuguesa e Itinerários",
            "Inglês e Itinerários",
            "Geografia e Itinerários",
            "Biologia e Itinerários",
            "Química e Itinerários",
            "Física e Itinerários",
            "História e Itinerários",
            "Filosofia e Itinerários",
            "Sociologia e Itinerários",
            "Ensino Religioso e Itinerários",
            "Listagem Geral"
        ]
        self.candidatos = []
        self.lista_selecionada = self.lista_nomes[0]

        # Interface - Menu de seleção da lista
        self.label_lista = tk.Label(root, text="Selecione a Listagem:", font=("Helvetica", 14), bg="#f0f0f0")
        self.label_lista.pack(pady=5)
        self.lista_var = tk.StringVar(value=self.lista_nomes[0])
        self.lista_menu = ttk.Combobox(root, textvariable=self.lista_var, values=self.lista_nomes, font=("Helvetica", 14), state="readonly")
        self.lista_menu.pack(pady=5)
        self.lista_menu.bind("<<ComboboxSelected>>", self.carregar_lista)

        # Área de entrada de dados
        self.frame_inputs = tk.Frame(root, bg="#f0f0f0")
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="Nome do Candidato:", font=("Helvetica", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.frame_inputs, font=("Helvetica", 14), width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self.frame_inputs, text="Classificação:", font=("Helvetica", 14), bg="#f0f0f0").grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.entry_classificacao = tk.Entry(self.frame_inputs, font=("Helvetica", 14), width=10)
        self.entry_classificacao.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        self.button_adicionar = tk.Button(self.frame_inputs, text="Adicionar Candidato", command=self.adicionar_candidato, font=("Helvetica", 14), bg="#4CAF50", fg="white", width=20)
        self.button_adicionar.grid(row=0, column=4, padx=10, pady=5)

        # Treeview para exibir a lista
        self.frame_table = tk.Frame(root)
        self.frame_table.pack(pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(self.frame_table, columns=("Posição", "Nome", "Classificação", "Status"), show="headings")
        self.tree.heading("Posição", text="Posição")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Classificação", text="Classificação")
        self.tree.heading("Status", text="Status")
        self.tree.column("Posição", width=80, anchor="center")
        self.tree.column("Nome", width=300, anchor="w")
        self.tree.column("Classificação", width=150, anchor="center")
        self.tree.column("Status", width=150, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 14))  
        style.configure("Treeview.Heading", font=("Helvetica", 16))

        # Status e Exclusão múltipla
        self.frame_status = tk.Frame(root, bg="#f0f0f0")
        self.frame_status.pack(pady=10)
        tk.Label(self.frame_status, text="Status:", font=("Helvetica", 14), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.status_var = tk.StringVar()
        self.status_options = ["PRESENTE", "AUSENTE", "CONFERENCIA", "DESISTENCIA", "ESCOLHEU VAGA"]
        self.status_menu = ttk.Combobox(self.frame_status, textvariable=self.status_var, values=self.status_options, font=("Helvetica", 14), state="readonly", width=15)
        self.status_menu.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.button_atualizar_status = tk.Button(self.frame_status, text="Atualizar Status", command=self.atualizar_status, font=("Helvetica", 14), bg="#0078D7", fg="white", width=20)
        self.button_atualizar_status.grid(row=0, column=2, padx=10, pady=5)

        self.button_excluir = tk.Button(self.frame_status, text="Excluir Candidato", command=self.excluir_candidato, font=("Helvetica", 14), bg="red", fg="white", width=20)
        self.button_excluir.grid(row=0, column=3, padx=10, pady=5)

        self.button_exportar = tk.Button(root, text="Exportar para Excel", command=self.exportar_excel, font=("Helvetica", 14), bg="#FF5722", fg="white", width=20)
        self.button_exportar.pack(pady=10)

        # Eventos de teclado
        self.root.bind("<Control-s>", lambda event: self.salvar_lista())

        # Carregar lista inicial
        self.carregar_lista()

    def adicionar_candidato(self):
        nome = self.entry_nome.get()
        classificacao = self.entry_classificacao.get()

        if nome and classificacao.isdigit():
            self.candidatos.append({"Nome": nome, "Classificação": int(classificacao), "Status": "PRESENTE"})
            self.reclassificar_candidatos()
            self.salvar_lista()
            self.entry_nome.delete(0, tk.END)
            self.entry_classificacao.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente!")

    def reclassificar_candidatos(self):
        self.candidatos.sort(key=lambda x: x["Classificação"])
        self.tree.delete(*self.tree.get_children())
        for idx, candidato in enumerate(self.candidatos, start=1):
            self.tree.insert("", "end", values=(f"{idx}º", candidato["Nome"], candidato["Classificação"], candidato["Status"]))

    def atualizar_status(self):
        selected_items = self.tree.selection()
        if selected_items:
            novo_status = self.status_var.get()
            for item in selected_items:
                item_values = self.tree.item(item, "values")
                nome = item_values[1]
                for candidato in self.candidatos:
                    if candidato["Nome"] == nome:
                        candidato["Status"] = novo_status
            self.reclassificar_candidatos()
            self.salvar_lista()
        else:
            messagebox.showwarning("Erro", "Selecione pelo menos um candidato!")

    def excluir_candidato(self):
        selected_items = self.tree.selection()
        if selected_items:
            for item in selected_items:
                item_values = self.tree.item(item, "values")
                nome = item_values[1]
                self.candidatos = [c for c in self.candidatos if c["Nome"] != nome]
            self.reclassificar_candidatos()
            self.salvar_lista()
        else:
            messagebox.showwarning("Erro", "Selecione pelo menos um candidato para excluir!")

    def salvar_lista(self):
        df = pd.DataFrame(self.candidatos)
        df.to_csv(f"{self.lista_var.get()}.csv", index=False)

    def carregar_lista(self, event=None):
        self.lista_selecionada = self.lista_var.get()
        self.candidatos = []
        if os.path.exists(f"{self.lista_selecionada}.csv"):
            self.candidatos = pd.read_csv(f"{self.lista_selecionada}.csv").to_dict("records")
        self.reclassificar_candidatos()

    def exportar_excel(self):
        pd.DataFrame(self.candidatos).to_excel(f"{self.lista_var.get()}.xlsx", index=False)
        messagebox.showinfo("Sucesso", "Lista exportada para Excel!")

root = tk.Tk()
app = CandidatosApp(root)
root.mainloop()
