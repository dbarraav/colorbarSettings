
from cc3d.core.PySteppables import *

class colorbarSettingsSteppable(SteppableBasePy):

    def __init__(self,frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        any code in the start function runs before MCS=0
        """
        self.create_scalar_field_cell_level_py("field1")
        
    def step(self,mcs):
        """
        type here the code that will run every frequency MCS
        :param mcs: current Monte Carlo step
        """
        field1 = self.field.field1
        field1.clear()
        
        for cell in self.cell_list:  
            field1[cell] = cell.id

    def finish(self):
        """
        Finish Function is called after the last MCS
        """

    def on_stop(self):
        # this gets called each time user stops simulation
        return


        