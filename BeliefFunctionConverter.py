import tkinter as tk
from tkinter import ttk

class DempsterShaferConverter:
    def __init__(self, subset_dico, hyp_tested):
        """
        Initialise un convertisseur Dempster-Shafer avec un dictionnaire de sous-ensembles et une hypothèse testée.

        Args:
            subset_dictionary (dict): Un dictionnaire représentant les sous-ensembles avec les valeurs de masse associées.
                                      La clé est un ensemble (frozenset) représentant le sous-ensemble, et la valeur est une liste
                                      contenant la valeur de masse à l'indice 0 et la représentation du sous-ensemble à l'indice 1.
            hypothesis_tested (set): L'hypothèse testée, représentée par un ensemble.
        """
        self.subset_dico = subset_dico
        self.hyp_tested = hyp_tested
    
    def mass_to_belief(self):
        """
        Convertit les valeurs de masse en fonction de croyance.

        Returns:
            float: La fonction de croyance résultante.
        """
        bel = 0
        if len(self.hyp_tested) > 0:
            for subset in self.subset_dico.keys():
                if (subset.issubset(self.hyp_tested) and len(subset) > 0):
                    bel += self.subset_dico[subset][0]
        return bel

    def mass_to_plausibility(self):
        """
        Convertit les valeurs de masse en fonction de plausibilité.

        Returns:
            float: La fonction de plausibilité résultante.
        """
        pl = 0
        if len(self.hyp_tested) > 0:
            for subset in self.subset_dico.keys():
                intersect = subset.intersection(self.hyp_tested)
                if (intersect and len(intersect) > 0):
                    pl += self.subset_dico[subset][0]
        return pl

    def mass_to_basis(self):
        """
        Convertit les valeurs de masse en base.

        Returns:
            float: La base résultante.
        """
        b = 0
        for subset in self.subset_dico.keys():
            if (subset.issubset(self.hyp_tested)):
                b += self.subset_dico[subset][0]
        return b

    def mass_to_vacuous_belief(self):
        """
        Convertit les valeurs de masse en vacuous belief.

        Returns:
            float: La croyance vacante résultante.
        """
        q = 0
        for subset in self.subset_dico.keys():
            if (self.hyp_tested.issubset(subset)):
                q += self.subset_dico[subset][0]
        return q

    def get_subsets(self, subset):
        """
        Génère tous les sous-ensembles d'un ensemble donné.

        Args:
            subset (set): L'ensemble à partir duquel les sous-ensembles doivent être générés.

        Returns:
            list: Une liste contenant tous les sous-ensembles générés.
        """
        subsets = [[]]
        for element in subset:
            subsets += [x + [element] for x in subsets]
        return subsets[1:]

class BeliefConverter(tk.Tk):
    """A GUI application for belief conversion.

    This application allows users to convert beliefs between different representations
    using Dempster-Shafer theory.

    Attributes:
        initial_representation (tk.StringVar): The initial belief representation.
        mass_value (tk.StringVar): The mass value for a selected subset.
        focals_text (tk.StringVar): Text variable to display focals.
        target_representation (tk.StringVar): The target belief representation.
        result_text (tk.StringVar): Text variable to display the conversion result.
        subset_chosen (tk.StringVar): The chosen subset for conversion.
        hyp_tested (tk.StringVar): The hypothesis tested for conversion.
        subset_dico (dict): Dictionary to store subsets and their mass values.
    """
    def __init__(self):
        """Initialize the BeliefConverter."""
        super().__init__()

        self.title("Belief Converter")
        self.geometry("400x600")

        self.initial_representation = tk.StringVar()
        self.mass_value = tk.StringVar()
        self.focals_text = tk.StringVar()
        self.target_representation = tk.StringVar()
        self.result_text = tk.StringVar()
        self.subset_chosen = tk.StringVar()
        self.hyp_tested = tk.StringVar()
        self.subset_dico = dict()

        self.create_widgets()

    def create_widgets(self):
        """Create widgets for the GUI."""
        # Input field for initial representation
        input_frame = ttk.LabelFrame(self, text="Cadre de discernement (Ex : H, V, T)")
        input_frame.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        input_entry = ttk.Entry(input_frame, textvariable=self.initial_representation, width=30)
        input_entry.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Button pour valider le cadre
        cadre_button = ttk.Button(self, text="Valider le cadre", command=self.valider_cadre)
        cadre_button.grid(column=1, row=0, padx=10, pady=10, sticky="w")

        # Dropdown menu for mass values
        subset_frame = ttk.LabelFrame(self, text="Subsets")
        subset_frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        self.subset_options = list()
        self.subset_dropdown = ttk.Combobox(subset_frame, textvariable=self.subset_chosen, state="readonly", values=self.subset_options)
        self.subset_dropdown.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        self.subset_dropdown.bind("<<ComboboxSelected>>", self.update_subset_value)

        # Input field for initial representation
        self.mass_frame = ttk.LabelFrame(self, text="Mass value for " + self.subset_chosen.get())
        self.mass_frame.grid(column=0, row=2, padx=10, pady=10, sticky="w")

        self.mass_entry = ttk.Entry(self.mass_frame, textvariable=self.mass_value, width=30)
        self.mass_entry.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Output field for focals
        focals_frame = ttk.LabelFrame(self, text="Focals")
        focals_frame.grid(column=1, row=2, padx=10, pady=10, sticky="w")

        focals_label = ttk.Label(focals_frame, textvariable=self.focals_text)
        focals_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Button to perform conversion
        convert_button = ttk.Button(self, text="Apply", command=self.update_mass_value)
        convert_button.grid(column=0, row=3, padx=10, pady=10, sticky="w")

        # Dropdown menu for target representation
        target_frame = ttk.LabelFrame(self, text="Target Representation")
        target_frame.grid(column=0, row=4, padx=10, pady=10, sticky="w")

        target_options = ["Belief Function", "Plausibility Function", "Basis", "Vacuous Belief"]
        target_dropdown = ttk.Combobox(target_frame, textvariable=self.target_representation, state="readonly", values=target_options)
        target_dropdown.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Dropdown menu for hyp
        hyp_frame = ttk.LabelFrame(self, text="Hypothèse testée")
        hyp_frame.grid(column=0, row=5, padx=10, pady=10, sticky="w")

        self.hyp_options = list()
        self.hyp_dropdown = ttk.Combobox(hyp_frame, textvariable=self.hyp_tested, state="readonly", values=self.hyp_options)
        self.hyp_dropdown.grid(column=0, row=0, padx=10, pady=10, sticky="w")
        self.hyp_dropdown.bind("<<ComboboxSelected>>", self.update_subset_value)

        # Button to perform conversion
        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        convert_button.grid(column=0, row=6, padx=10, pady=10, sticky="w")

        # Output field for result
        result_frame = ttk.LabelFrame(self, text="Result")
        result_frame.grid(column=0, row=7, padx=10, pady=10, sticky="w")

        result_label = ttk.Label(result_frame, textvariable=self.result_text)
        result_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

    def get_subsets(self, liste):
        taille = len(liste)
        nb_subset = 2**taille
        subsets = []
        for i in range(nb_subset):
            code_binaire = "{0:0{1}b}".format(i, taille)
            subset = set([element for element, bit in zip(liste, code_binaire) if bit=='1'])
            subsets.append(subset)
        return subsets
    
    def valider_cadre(self):
        self.subset_dico = dict()
        mass_function_str = self.initial_representation.get()
        mass_function_str = mass_function_str.replace(" ", "")
        mass_function = list(mass_function_str.split(","))
        mass_function = self.get_subsets(mass_function)
        for elem in mass_function:
            s='{'
            i = 1
            l = len(elem)
            if l > 0:
                for sub in elem:
                    if i < l:
                        s += sub + ', '
                        i+=1
                    else:
                        s+= sub + '}'
                self.subset_dico[frozenset(sorted(elem))] = [0, s]
            else:
                self.subset_dico[frozenset(sorted(elem))] = [0, '{}']
        l=[]
        for val in self.subset_dico.values():
            l.append(val[1])
        self.subset_options = l
        self.subset_dropdown['values'] = self.subset_options
        self.hyp_options = l
        self.hyp_dropdown['values'] = self.hyp_options
    
    def update_subset_value(self, event=None):
        self.mass_frame['text'] = ("Mass value for " + self.subset_chosen.get())

    def update_mass_value(self, event=None):
        subset_str = self.subset_chosen.get()
        for key in self.subset_dico.keys():
            if self.subset_dico[key][1] == subset_str:
                subset = key
        if subset in self.subset_dico.keys():
            self.subset_dico[subset][0] = float(self.mass_value.get())
        else:
            print("Subset not found in dictionary.")

        focals = ""
        for key in self.subset_dico.keys():
            if self.subset_dico[key][0] > 0:
                focal = 'm('+ self.subset_dico[key][1] + ") = " + str(self.subset_dico[key][0]) + '\n'
                focals = focals + focal
                self.focals_text.set(focals)

    def update_hyp_tested(self, event=None):
        self.hyp_options = list(self.subset_dico.keys())
        self.hyp_dropdown['values'] = self.subset_options
    
    def convert(self, event=None):
        for key in self.subset_dico.keys():
            if self.subset_dico[key][1] == (self.hyp_tested.get()):
                self.hyp = key
        converter = DempsterShaferConverter(self.subset_dico, self.hyp)
        target_representation = self.target_representation.get()
        if target_representation == "Belief Function":
            result = converter.mass_to_belief()
        elif target_representation == "Plausibility Function":
            result = converter.mass_to_plausibility()
        elif target_representation == "Basis":
            result = converter.mass_to_basis()
        elif target_representation == "Vacuous Belief":
            result = converter.mass_to_vacuous_belief()
        else:
            result = 'Choose a target representation'

        self.result_text.set(str(result))

if __name__ == "__main__":
    app = BeliefConverter()
    app.mainloop()