from rdkit import Chem
from rdkit.Chem import Draw
import PIL

size = (120, 120)
m = Chem.MolFromSmiles('с16h32')
fig = Draw.MolToImage(m, size=size)
fig = fig.save('img.png')


def add_functions(self):
    self.pushButton.clicked.connect(lambda: self.write_name(self.lineEdit.text()))


def write_name(self, text):
    try:
        print(text.upper())
        formula = Namer(text.upper()).molecular_formula()
        name = Namer(text.upper()).analyser()
        name = translator.translate(name)
        self.label_2.setText(f'{formula} - {name}')
    except:
        self.label_2.setText('Неправильно введена формула')