import tkinter as tk
from tkinter import messagebox, ttk

# Define the diseases and symptoms
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
    for disease, disease_symptoms in rules.items():
        match_count = sum(1 for symptom in selected_symptoms if symptom in disease_symptoms)
        if match_count >= 3:
            return diseases[disease]
    return "No disease matches the given symptoms"

class DiagnosisApp:
    def __init__(self, master):
        self.master = master
        master.title("Corn Disease Diagnosis System")
        master.geometry("400x400")
        master.config(bg="#f7f7f7")

        self.selected_symptoms = []
        self.check_vars = {code: tk.BooleanVar() for code in symptoms.keys()}

        title_label = tk.Label(master, text="Corn Disease Diagnosis", font=("Helvetica", 16, "bold"), bg="#f7f7f7")
        title_label.pack(pady=10)

        instruction_label = tk.Label(master, text="Select the symptoms observed:", bg="#f7f7f7")
        instruction_label.pack(pady=5)

        symptom_frame = ttk.Frame(master)
        symptom_frame.pack(pady=10)

        for code, desc in symptoms.items():
            chk = tk.Checkbutton(symptom_frame, text=desc, variable=self.check_vars[code], bg="#f7f7f7")
            chk.pack(anchor='w')

        diagnose_button = tk.Button(master, text="Diagnose", command=self.diagnose, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        diagnose_button.pack(pady=20)

        reset_button = tk.Button(master, text="Reset", command=self.reset, bg="#f44336", fg="white", font=("Helvetica", 12))
        reset_button.pack(pady=5)

    def diagnose(self):
        self.selected_symptoms = [code for code, var in self.check_vars.items() if var.get()]

        if not self.selected_symptoms:
            messagebox.showwarning("Warning", "No symptoms were selected. Cannot diagnose.")
            return
        
        result = forward_chaining(self.selected_symptoms)
        messagebox.showinfo("Diagnosis Result", result)

    def reset(self):
        for var in self.check_vars.values():
            var.set(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnosisApp(root)
    root.mainloop()
