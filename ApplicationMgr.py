from Menu import Menu
from Integrals import Integrals
from History import History
from InputReader import InputReader
from Help import Help

log = History()
menu = Menu()
reader = InputReader()
sub = Integrals()
help = Help()

while True:

    selection = menu.select()

    if selection == 'q':
        break
    elif selection == '1':
        result = sub.singleIntegral()
        log.add(result)
    elif selection == '2':
        results = sub.manyIntegrals()
        log.add(results)
    elif selection == '3':
        log.show()
        raw_input("Press any key to close...")
    elif selection == '4':
        help.show()
        raw_input("Press any key to close...")

if not(log.isEmpty()):
    log.show()
    if reader.yesNoInput("Save history to file?"):
        log.saveToFile()

print("Goodbye!")
