#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )

import os
from filesplit.split import Split
from tkinter import Tk, filedialog

def get_manual_path(isfile):
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    if isfile:
        open_c = filedialog.askopenfilename()
    else:
        open_c = filedialog.askdirectory()
    root.destroy()
    return open_c

print(' Select file to split...', end='\r')
input_file = get_manual_path(True)
print(' Select output directory...', end='\r')
output_directory = get_manual_path(False)

Split(input_file, output_directory).bysize(1024*1024*25)
splitted_files_to_send = os.listdir(output_directory)
for sfile in splitted_files_to_send:
    if sfile != 'manifest':
        os.rename(output_directory + '/' + sfile, output_directory + '/' + sfile + '.pysilon')
input('Done (press ENTER to quit)      ')

#THIS WAS MADE BY @MASTERAUXB ON TWITTER PLEASE DO NOT DELETE 
#ORIGINAL AUTHOR : https://github.com/mategol/PySilon-malware
#MODDED AUTHOR : https://github.com/MaitreAuxb/
#I TOOK TIME TO CREATE THIS PROJECT PLEASE DO NO DELETE THIS
#PLEASE DO NOT ADD PAYLOAD ON VIRUSTOTAL ( it shares signatures with other av companies )
