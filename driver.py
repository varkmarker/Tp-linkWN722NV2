from colr import Colr as colr
import os
import time



# Color's functions
class Colors:
    def red(data):
        print(colr().hex("#ff0000", data, rgb_mode=True))

    def rose(data):
        print(colr().hex("#ff0066", data, rgb_mode=True))

    def green(data):
        print(colr().hex("#00ff8d", data, rgb_mode=True))

    def gnome_green(data):
        print(colr().hex("#2ed1b4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#a8c836", data, rgb_mode=True))

    def dark_orange(data):
        print(colr().hex("#cf301b", data, rgb_mode=True))

    def light_gnome(data):
        print(colr().hex("#00ffc4", data, rgb_mode=True))

    def yellow_green(data):
        print(colr().hex("#7ed666", data, rgb_mode=True))

    def violet(data):
        print(colr().hex("#cc33ff", data, rgb_mode=True))

    def light_green(data):
        print(colr().hex("#21ff00", data, rgb_mode=True))

    def orange(data):
        print(colr().hex("#ff8e35", data, rgb_mode=True))

    def yellow(data):
        print(colr().hex("#fff300", data, rgb_mode=True))

    def sky_blue(data):
        print(colr().hex("#00ccff", data, rgb_mode=True))

    def blue(data):
        print(colr().hex("#0000ff", data, rgb_mode=True))

    def cream(data):
        print(colr().hex("#ff9999", data, rgb_mode=True))

    def dark_rose(data):
        print(colr().hex("#cc0066", data, rgb_mode=True))

    def dark_red(data):
        print(colr().hex("#cc0000", data, rgb_mode=True))

    def dark_green(data):
        print(colr().hex("#009933", data, rgb_mode=True))

    def light_blue(data):
        print(colr().hex("#6666ff", data, rgb_mode=True))














# Welcome Banner
time.sleep(0.5)
Colors.red(
    """\n  
                ********** *******         **        **  ****     **  **   **
                /////**/// /**////**       /**      /** /**/**   /** /**  ** 
                    /**    /**   /**       /**      /** /**//**  /** /** **  
                    /**    /*******  ***** /**      /** /** //** /** /****   
                    /**    /**////  /////  /**      /** /**  //**/** /**/**  
                    /**    /**             /**      /** /**   //**** /**//** 
                    /**    /**             /********/** /**    //*** /** //**
                    //     //              //////// //  //      ///  //   // """
)
Colors.blue(
    "\n                                                                WN722NV2"
)
time.sleep(0.5)
Colors.orange(
    "\n IT IS A TOOL TO INSTALL THE TP-LINK VERSION 2 WIFI ADAPTER DRIVE THAT SUPPORTS MONITOR MODE "
)