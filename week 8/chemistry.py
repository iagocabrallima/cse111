def main():
    formula = "C13H18O2"
    mass = 5.04
  
    periodic_table_dict = make_periodic_table()
  
    known_molecules_dict = make_known_molecules_dict()

    symbol_quantity_list = parse_formula(formula, periodic_table_dict)

    total_molar_mass = calculate_molar_mass(
        symbol_quantity_list, periodic_table_dict)

   
    compound_name = get_formula_name(formula, known_molecules_dict)


    moles_in_sample = mass/total_molar_mass

  
    number_protons = sum_protons(symbol_quantity_list, periodic_table_dict)

    
    print(f"Molar mass of {formula}: {total_molar_mass:,.5f} grams/mole")

    
    print(f"Number of moles in the sample: {moles_in_sample:,.5f} moles")

    
    print(f"Compounds name is: {compound_name}")

    
    print(f"Number of protons in the compound: {number_protons}")


def make_known_molecules_dict():
  
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water",
        "C6H12O6": "glucose"
    }

    return known_molecules_dict


def make_periodic_table():
  
    periodic_table_dict = {
       
        'Ac': ['Actinium', 227, 89],
        'Ag': ['Silver', 107.8682, 47],
        'Al': ['Aluminum', 26.9815386, 13],
        'Ar': ['Argon', 39.948, 18],
        'As': ['Arsenic', 74.9216, 33],
        'At': ['Astatine', 210, 85],
        'Au': ['Gold', 196.966569, 79],
        'B': ['Boron', 10.811, 5],
        'Ba': ['Barium', 137.327, 56],
        'Be': ['Beryllium', 9.012182, 4],
        'Bi': ['Bismuth', 208.9804, 83],
        'Br': ['Bromine', 79.904, 35],
        'C': ['Carbon', 12.0107, 6],
        'Ca': ['Calcium', 40.078, 20],
        'Cd': ['Cadmium', 112.411, 48],
        'Ce': ['Cerium', 140.116, 58],
        'Cl': ['Chlorine', 35.453, 17],
        'Co': ['Cobalt', 58.933195, 27],
        'Cr': ['Chromium', 51.9961, 24],
        'Cs': ['Cesium', 132.9054519, 55],
        'Cu': ['Copper', 63.546, 29],
        'Dy': ['Dysprosium', 162.5, 66],
        'Er': ['Erbium', 167.259, 68],
        'Eu': ['Europium', 151.964, 63],
        'F': ['Fluorine', 18.9984032, 9],
        'Fe': ['Iron', 55.845, 26],
        'Fr': ['Francium', 223, 87],
        'Ga': ['Gallium', 69.723, 31],
        'Gd': ['Gadolinium', 157.25, 64],
        'Ge': ['Germanium', 72.64, 32],
        'H': ['Hydrogen', 1.00794, 1],
        'He': ['Helium', 4.002602, 2],
        'Hf': ['Hafnium', 178.49, 72],
        'Hg': ['Mercury', 200.59, 80],
        'Ho': ['Holmium', 164.93032, 67],
        'I': ['Iodine', 126.90447, 53],
        'In': ['Indium', 114.818, 49],
        'Ir': ['Iridium', 192.217, 77],
        'K': ['Potassium', 39.0983, 19],
        'Kr': ['Krypton', 83.798, 36],
        'La': ['Lanthanum', 138.90547, 57],
        'Li': ['Lithium', 6.941, 3],
        'Lu': ['Lutetium', 174.9668, 71],
        'Mg': ['Magnesium', 24.305, 12],
        'Mn': ['Manganese', 54.938045, 25],
        'Mo': ['Molybdenum', 95.96, 42],
        'N': ['Nitrogen', 14.0067, 7],
        'Na': ['Sodium', 22.98976928, 11],
        'Nb': ['Niobium', 92.90638, 41],
        'Nd': ['Neodymium', 144.242, 60],
        'Ne': ['Neon', 20.1797, 10],
        'Ni': ['Nickel', 58.6934, 28],
        'Np': ['Neptunium', 237, 93],
        'O': ['Oxygen', 15.9994, 8],
        'Os': ['Osmium', 190.23, 76],
        'P': ['Phosphorus', 30.973762, 15],
        'Pa': ['Protactinium', 231.03588, 91],
        'Pb': ['Lead', 207.2, 82],
        'Pd': ['Palladium', 106.42, 46],
        'Pm': ['Promethium', 145, 61],
        'Po': ['Polonium', 209, 84],
        'Pr': ['Praseodymium', 140.90765, 59],
        'Pt': ['Platinum', 195.084, 78],
        'Pu': ['Plutonium', 244, 94],
        'Ra': ['Radium', 226, 88],
        'Rb': ['Rubidium', 85.4678, 37],
        'Re': ['Rhenium', 186.207, 75],
        'Rh': ['Rhodium', 102.9055, 45],
        'Rn': ['Radon', 222, 86],
        'Ru': ['Ruthenium', 101.07, 44],
        'S': ['Sulfur', 32.065, 16],
        'Sb': ['Antimony', 121.76, 51],
        'Sc': ['Scandium', 44.955912, 21],
        'Se': ['Selenium', 78.96, 34],
        'Si': ['Silicon', 28.0855, 14],
        'Sm': ['Samarium', 150.36, 62],
        'Sn': ['Tin', 118.71, 50],
        'Sr': ['Strontium', 87.62, 38],
        'Ta': ['Tantalum', 180.94788, 73],
        'Tb': ['Terbium', 158.92535, 65],
        'Tc': ['Technetium', 98, 43],
        'Te': ['Tellurium', 127.6, 52],
        'Th': ['Thorium', 232.03806, 90],
        'Ti': ['Titanium', 47.867, 22],
        'Tl': ['Thallium', 204.3833, 81],
        'Tm': ['Thulium', 168.93421, 69],
        'U': ['Uranium', 238.02891, 92],
        'V': ['Vanadium', 50.9415, 23],
        'W': ['Tungsten', 183.84, 74],
        'Xe': ['Xenon', 131.293, 54],
        'Y': ['Yttrium', 88.90585, 39],
        'Yb': ['Ytterbium', 173.054, 70],
        'Zn': ['Zinc', 65.38, 30],
        'Zr': ['Zirconium', 91.224, 40],
    }

    return periodic_table_dict


class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
   
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula, "
                                           f"unknown element symbol: {symbol}",
                                           formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula, "
                                       "unmatched close parenthesis",
                                       formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    
                    message = "invalid formula"
                else:
                   
                    message = "invalid formula, illegal character"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula, "
                               "unmatched open parenthesis",
                               formula, start_index - 1)
        return elem_dict, index

    
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())



NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def calculate_molar_mass(symbol_quantity_list, periodic_table_dict):
    symbol_list = [i[0] for i in symbol_quantity_list]
    quantity_list = [i[1] for i in symbol_quantity_list]
 
    atomic_mass = []
    for i in symbol_list:
        values = periodic_table_dict[i]
        atomic_mass.append(values[1])

    molar_mass = []
    for (x, y) in zip(atomic_mass, quantity_list):
        molar_mass.append(x*y)

    total_molar_mass = sum(molar_mass)

 
    return total_molar_mass


def get_formula_name(formula, known_molecules_dict):
   
    if formula in known_molecules_dict:

        
        compound_name = known_molecules_dict[formula]

    else:
        compound_name = "Not Found in Dictionary!"

    return compound_name


def sum_protons(symbol_quantity_list, periodic_table_dict):
   
   
    symbol_list = [i[0] for i in symbol_quantity_list]
    quantity_list = [i[1] for i in symbol_quantity_list]
  
   
    atomic_number = []
    for i in symbol_list:
        values = periodic_table_dict[i]
        atomic_number.append(values[2])
 
    num_protons = []
    for (x, y) in zip(atomic_number, quantity_list):
        num_protons.append(x*y)

    total_num_protons = sum(num_protons)


    return total_num_protons

if __name__ == "__main__":
    main()