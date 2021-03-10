"""
===========
Slider Demo
===========
by +N
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def example_1st():
    ############################################################################
    # 1st Example start
    ############################################################################
    fig = plt.figure()
    #用t和s定義2D線段
    #===============================
    t = np.arange(0, 10, 1)
    print("t =", t)
    s = 0 * t
    print("s =", s)
    #-------------------------
    l, = plt.plot( t, s )
    print("l = ", l)
    l2, = plt.plot( s, t )
    print("l2 = ", l2)
    #===============================

    #定義slider的位置（大小）
    #===========================================
    location_of_slider_1 = plt.axes([
        0.2,  # slider box x-coordinate start
        0,    # slider box y-coordinate start
        0.7,  # slider box x-coordinate end
        0.05, # slider box y-coordinate end
        ])
    #===========================================

    #產生一個Slider的物件叫做slider_1 
    #==========================================================
    slider_1 = Slider(
            location_of_slider_1, # 採用定上面定義的slider位置
            'slider_name',        # 顯示的名字
            0,                    # slider_1的最小值
            9,                    # slider_1的最大值
            valinit=5,            # slider_1的初始值
            valstep=1,            # 滑動時每一步的步長
            )
    #==========================================================

    #定義一個 『函式』,這個函式的內容是slider的值被更新時所對應要做的事情
    #=========================================================================
    def update_slider_1(val):
        l.set_ydata( slider_1.val ) # slider_1.val 就是目前slider_1被滑到的值
        plt.draw() #根據調正過後的值重新畫圖
    #=========================================================================

    #定義當slider_1的值被改變時要做哪個『函式』所定義的事
    slider_1.on_changed( update_slider_1 )

    #將以上所定義的規則套用在的那個『圖』顯示在螢幕上(從記憶體內被讀取出來)
    plt.show()
    ############################################################################
    # 1st Example end
    ############################################################################

def example_2nd():
    #################################################################
    # 2nd Example start
    #################################################################
    fig = plt.figure()
    _3d_fig = fig.gca(projection='3d') # gca = Get Current Axis !!!
    _3d_fig.set_xlim( xmin= 0, xmax=1)
    _3d_fig.set_ylim( ymin= 0, ymax=1)
    _3d_fig.set_zlim( zmin= 0, zmax=1)
    # plot the slider
    initial_xx = 0.25
    initial_zz = 0.25
    #               x_start, y_start, x_end, y_end
    axamp_xx = plt.axes([.25, .01, .55, .06])
    axamp_zz = plt.axes([.06, .25, .07, .55])
    # Slider defined
    samp_xx = Slider(axamp_xx, 'X', 0, 0.5, valinit=initial_xx, \
            orientation='horizontal', valstep=0.01)
    samp_zz = Slider(axamp_zz, 'Z', 0, 0.5, valinit=initial_zz, \
            orientation='vertical',   valstep=0.01)
    # plot black ab_line
    a_xyz =( 0,    0,  0 ) 
    b_xyz =( initial_xx, 0.5, initial_zz ) 
    _3d_fig.plot(
            [a_xyz[0], b_xyz[0]], # x-direction
            [a_xyz[1], b_xyz[1]], # y-direction
            [a_xyz[2], b_xyz[2]], # z-direction
            color="black")
    def update(val):
        #--------------------------------------------
        # xx is the current value of the slider
        xx = samp_xx.val # paper's x
        zz = samp_zz.val # paper's y
        _3d_fig.clear()
        _3d_fig.set_xlim( xmin= 0, xmax=1)
        _3d_fig.set_ylim( ymin= 0, ymax=1)
        _3d_fig.set_zlim( zmin= 0, zmax=1)
        # plot black ab_line
        a_xyz =( 0,    0,  0 ) 
        b_xyz =( xx, 0.5, zz ) 
        _3d_fig.plot(
                [a_xyz[0], b_xyz[0]], # x-direction
                [a_xyz[1], b_xyz[1]], # y-direction
                [a_xyz[2], b_xyz[2]], # z-direction
                color="black")
        plt.draw() # redraw 
        #--------------------------------------------
    samp_xx.on_changed(update)
    samp_zz.on_changed(update)
    plt.show()
    #################################################################
    # 2nd Example end
    #################################################################


def input_collecting():
    input_number = input( \
          "================================================\n" \
          "\n" \
          "Please choose one example to begin with or quit.\n" \
          "\n" \
          "================================================\n" \
          "1st Example (1)\n" \
          "2nd Example (2)\n" \
          "Quit        (q)\n" \
          "================================================\n" \
          "\n" \
          "Please enter your choice at here : ")
    return input_number

# Start to run the main program from here!
#============================================
input_number = input_collecting()

#--------------------------------------
while not input_number == "q":
    #------------------------
    if input_number=="1":
        example_1st()
    elif input_number=="2":
        example_2nd()
    #------------------------
    for i in range(100):
        print("")
    input_number = input_collecting()
#--------------------------------------

print("Goodbye !!")
#============================================


