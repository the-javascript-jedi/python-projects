#  pip install translate
from translate import Translator

translator=Translator(to_lang="es")
try:
    with open('./test.txt',mode='r') as my_file:
        print(my_file.read())
        text=my_file.read()
        translation=translator.translate("This is a pen.")
        print("translation",translation)
        with open('./test-es.txt',mode='w') as my_translated_file:
            my_translated_file.write(translation)
except FileNotFoundError as e:
    print('check your file path silly!')
