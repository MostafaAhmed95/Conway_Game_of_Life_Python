from Gui import Vis
from lis import Mop
import time
m=Vis(300,300,20)
ly=Mop(300,300,20)

#glider shape
ly.init_pos(2,4)
ly.init_pos(3,5)
ly.init_pos(3,6)
ly.init_pos(4,4)
ly.init_pos(4,5)

m.colorize(ly.l)

def again():
    ly.next_it()
    m.colorize(ly.l)
    m.top.after(1000,again)

m.top.after(1000,again)
m.top.mainloop()


