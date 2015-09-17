'''
Name:
	ij_ocd.py : Tiling Window Plugin for the Fiji Perfectionist.
Brief:
	Auto-arrange all the non-image windows.
 Author:
 	Pushkar Paranjpe
	 C-CAMP, India
	 pushkarparanjpe@gmail.com
	 http://mezzoderm.webfactional.com/ 
Version:
	0.1
Since:
	Aug, 17, 2015
 '''

from ij import IJ
from ij import WindowManager as WM

import fiji.scripting.TextEditor as FSTE
import ij.plugin.frame.RoiManager as ROIM
import ij.text.TextWindow as TW
import ij.plugin.frame.Recorder as REC



def arrange():
	
	# Fiji JFrame Instance and Measurements
	IJ_FRAME = IJ.getInstance()
	IJ_WIDTH = IJ_FRAME.getWidth()
	IJ_HEIGHT = IJ_FRAME.getHeight()
	#
	
	# Display Screen Measurements
	SCREEN_DIMS = IJ_FRAME.getGraphicsConfiguration().getBounds()
	SCREEN_WIDTH = int(SCREEN_DIMS.getWidth())
	SCREEN_HEIGHT = int(SCREEN_DIMS.getHeight())
	print SCREEN_WIDTH, SCREEN_HEIGHT
	#
	
	# the window is Fiji JFrame itself
	IJ_FRAME.setLocation(SCREEN_WIDTH - IJ_WIDTH, 0)
	#
	
	niws = WM.getNonImageWindows()
	print "%i non-image windows are open" % (len(niws))
	for win in niws:
		w = win.getWidth()
		h = win.getHeight()
		x = win.getX()
		y = win.getY()
		print w,h, x,y
		print type(win)
	
		#IF the window is Fiji Scripting TextEditor
		if type(win) == FSTE:
			w, h = 640, 540
			win.setSize(w, h)
			win.setLocation(SCREEN_WIDTH - w, SCREEN_HEIGHT-h)
	
		#IF the window is ROI Manager
		elif type(win) == ROIM:
			win.setLocation(0, 0)
	
		#IF the window is Results Window
		elif type(win) == TW and win.getTitle() == "Results":
			w, h = 480, 320
			win.setSize(w, h)
			win.setLocation(0, SCREEN_HEIGHT-h)
	
		#IF the window is Recorder Window
		elif type(win) == REC:
			w, h = 480, 320
			win.setSize(w, h)
			win.setLocation(0, SCREEN_HEIGHT-h-120)
	
	
if __name__=='__main__':
	arrange()