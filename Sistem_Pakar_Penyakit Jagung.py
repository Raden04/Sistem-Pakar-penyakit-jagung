import tkinter as tk
from tkinter import messagebox, ttk

diseases = {
    "P001": "Bulai",
    "P002": "Blight",
    "P003": "Leaf Rust",
    "P004": "Burn",
    "P005": "Stem Borer",
    "P006": "Cob Borer"
}

rules = {
    "P001": ["G1", "G2", "G3", "G4", "G5"],
    "P002": ["G6", "G7", "G8", "G9", "G10"],
    "P003": ["G10", "G11", "G12", "G13", "G14"],
    "P004": ["G15", "G16", "G17", "G18", "G19"],
    "P005": ["G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27"],
    "P006": ["G28", "G29", "G30", "G31"]
}

symptoms = {
    "G1": "Chlorotic colored leaves",
    "G2": "Experiencing stunted growth",
    "G3": "White like flour on leaves",
    "G4": "Leaves curl and twist",
    "G5": "Impaired cob formation",
    "G6": "Wilted leaves",
    "G7": "Small spots unite forming larger spots",
    "G8": "Elongated light brown spots",
    "G9": "Brown elliptical spots",
    "G10": "Leaves look dry",
    "G11": "Small brown or yellow spots",
    "G12": "Red spots on the midrib",
    "G13": "Irregular white and brown threads",
    "G14": "Yellowish brown flour-like powder",
    "G15": "Swelling of the cob",
    "G16": "White to black fungus on seeds",
    "G17": "Swollen seeds",
    "G18": "Glands formed in seeds",
    "G19": "White to black fungus appearing",
    "G20": "Small holes in the leaf",
    "G21": "Slits in the stem",
    "G22": "Flowers at the cob base",
    "G23": "Stems and tassels break easily",
    "G24": "Pile of broken tassels",
    "G25": "Male flowers not formed",
    "G26": "Flour or dirt around the hoist",
    "G27": "Slightly yellow leaves",
    "G28": "Transverse holes in the leaves",
    "G29": "Corn cob hair is cut/dry",
    "G30": "End of cob has a quiver",
    "G31": "Larvae presence"
}

def forward_chaining(selected_symptoms):
    possible_diseases = []
    for disease, disease_symptoms in rules.items():
        match_count = sum(1 for symptom in selected_symptoms if symptom in disease_symptoms)
        if match_count >= 3:
            possible_diseases.append(diseases[disease])
    if possible_diseases:
        return ", ".join(possible_diseases)
    return "No disease matches the given symptoms"

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        canvas = tk.Canvas(self, borderwidth=0, background="#f7f7f7")
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class DiagnosisApp:
    def __init__(self, master):
        self.master = master
        master.title("Corn Disease Diagnosis System")
        master.geometry("500x600")
        master.resizable(False, False)
        master.config(bg="#f7f7f7")

        self.selected_symptoms = []
        self.check_vars = {code: tk.BooleanVar() for code in symptoms.keys()}

        header_frame = tk.Frame(master, bg="#4CAF50")
        header_frame.pack(fill='x')

        title_label = tk.Label(header_frame, text="Corn Disease Diagnosis", font=("Helvetica", 18, "bold"), fg="white", bg="#4CAF50")
        title_label.pack(pady=15)

        instruction_frame = tk.Frame(master, bg="#f7f7f7")
        instruction_frame.pack(pady=10, padx=20, fill='x')

        instruction_label = tk.Label(instruction_frame, text="Select the symptoms observed:", font=("Helvetica", 12), bg="#f7f7f7")
        instruction_label.pack(anchor='w')

        symptoms_frame = ScrollableFrame(master)
        symptoms_frame.pack(pady=10, padx=20, fill='both', expand=True)

        for idx, (code, desc) in enumerate(symptoms.items(), start=1):
            chk = tk.Checkbutton(symptoms_frame.scrollable_frame, text=f"{idx}. {desc}", variable=self.check_vars[code], bg="#f7f7f7", anchor='w', justify='left', wraplength=450, font=("Helvetica", 10))
            chk.pack(anchor='w', pady=2)

        buttons_frame = tk.Frame(master, bg="#f7f7f7")
        buttons_frame.pack(pady=10)

        diagnose_button = tk.Button(buttons_frame, text="Diagnose", command=self.diagnose, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=15, height=2)
        diagnose_button.grid(row=0, column=0, padx=10)

        reset_button = tk.Button(buttons_frame, text="Reset", command=self.reset, bg="#f44336", fg="white", font=("Helvetica", 12), width=15, height=2)
        reset_button.grid(row=0, column=1, padx=10)

        result_frame = tk.Frame(master, bg="#f7f7f7")
        result_frame.pack(pady=10, padx=20, fill='x')

        self.result_label = tk.Label(result_frame, text="", bg="#f7f7f7", font=("Helvetica", 12, "bold"), fg="#333")
        self.result_label.pack(anchor='w')

        footer_frame = tk.Frame(master, bg="#f7f7f7")
        footer_frame.pack(side='bottom', fill='x', pady=10)

        footer_label = tk.Label(footer_frame, text="© 2024 Corn Disease Diagnosis System", font=("Helvetica", 8), bg="#f7f7f7", fg="#888")
        footer_label.pack()

    def diagnose(self):
        self.selected_symptoms = [code for code, var in self.check_vars.items() if var.get()]

        if not self.selected_symptoms:
            messagebox.showwarning("Warning", "No symptoms were selected. Cannot diagnose.")
            return

        result = forward_chaining(self.selected_symptoms)
        self.result_label.config(text=f"Diagnosis Result: {result}", fg="#4CAF50")

    def reset(self):
        for var in self.check_vars.values():
            var.set(False)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosisApp(root)
    root.mainloop()
