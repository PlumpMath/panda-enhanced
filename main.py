from pandac.PandaModules import loadPrcFileData
loadPrcFileData("", """sync-video 0
fullscreen 1
#win-size 1920 1080
win-size 1366 768
yield-timeslice 0 
client-sleep 0 
multi-sleep 0
basic-shaders-only #t

audio-library-name null""")

from direct.directbase import DirectStart
#from system.map import *

from direct.gui.DirectGui import DirectFrame
from direct.gui.OnscreenText import OnscreenText
import sys, gc

from console.panda3d_console import panda3dIOClass

render.setShaderAuto()
#base.toggleWireframe()
base.setFrameRateMeter(True)

"""
Good practice for the time of development
"""
gc.enable()
gc.set_debug(gc.DEBUG_LEAK)

class main(object):
    def __init__(self):
        base.setBackgroundColor(.2, .2, .2)
        base.camLens.setFov(75)
        base.camLens.setNear(0.01)
        base.disableMouse()
        
        base.setFrameRateMeter(True)
        render.setShaderAuto()
        self.console = panda3dIOClass(self)
        
    
    def doExit(self):
        self.map_sql.destroy()
        
        print "\n\n\nGARBAGE COLLECTED:\n"
        gc.collect()
        for g in gc.garbage:
            print g
        
        sys.exit()

m = main()
#m.startGame()

base.accept("escape", m.doExit)

run()
