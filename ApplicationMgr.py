from Menu import Menu
from Integrals import Integrals
from History import History
from InputReader import InputReader
from Help import Help

# creating necessary objects
log = History()
menu = Menu()
reader = InputReader()
sub = Integrals()
myHelp = Help()

while True:

    selection = menu.select()           #

    if selection == 'q':                # Quiting the main menu
        break
    elif selection == '1':              # choosing single integral option
        result = sub.singleIntegral()
        log.add(result)
    elif selection == '2':              # choosing many integrals
        results = sub.manyIntegrals()
        log.add(results)
    elif selection == '3':              # choosing history
        log.show()
        raw_input("Press any key to close...")
    elif selection == '4':              # choosing help
        myHelp.show()
        raw_input("Press any key to close...")

if not(log.isEmpty()):                  # displays this session's history only if there is something to show
    log.show()
    if reader.yesNoInput("Save history to file?"):
        log.saveToFile()

print("Goodbye!")
