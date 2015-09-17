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

from ij import ImageJ
from fiji.scripting import TextEditor
from ij.plugin.frame import RoiManager
from ij.text import TextWindow
from ij.plugin.frame import Recorder




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
	
	SPECS = {
	#	Format:
	#	WINDOW : 	[x,	y,	w,	h]
	#
		ImageJ :		[SCREEN_WIDTH - IJ_WIDTH, 0, None, None],
		TextEditor :	[SCREEN_WIDTH-640, SCREEN_HEIGHT-540, 640, 540],
		RoiManager :	[0, 0, None, None],
		TextWindow :	[0, SCREEN_HEIGHT-320, 480, 320],
		Recorder :		[0, SCREEN_HEIGHT-320-120, 480, 320],
	}
	
	# the window is Fiji JFrame itself
	x,y,w,h = SPECS[ type(IJ_FRAME) ]
	IJ_FRAME.setLocation(x,y)
	#
	
	niws = WM.getNonImageWindows()
	print "%i non-image windows are open" % (len(niws))
	for win in niws:
		print type(win)
		x, y, w, h = SPECS[ type(win) ]
		if w == None:	w = win.getWidth()
		if h == None:	h = win.getHeight()
		win.setSize(w, h)
		win.setLocation(x, y)


if __name__=='__main__':
	arrange()