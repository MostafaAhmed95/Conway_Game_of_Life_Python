from Gui import Vis
from lis import Mop
import time
m=Vis(300,300,20)
ly=Mop(300,300,20)
ly.init_pos(1,1)
ly.init_pos(1,2)
ly.init_pos(1,3)
m.colorize(ly.l)
time.sleep(2)
ly.next_it()
m.colorize(ly.l)
m.top.mainloop()

