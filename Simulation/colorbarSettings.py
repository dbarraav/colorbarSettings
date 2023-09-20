
from cc3d import CompuCellSetup
        

from colorbarSettingsSteppables import colorbarSettingsSteppable

CompuCellSetup.register_steppable(steppable=colorbarSettingsSteppable(frequency=1))


CompuCellSetup.run()
