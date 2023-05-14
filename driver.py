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


# Operator's
class Operators:
    # Normal exit
    def exit():
        os.system("exit")
        time.sleep(0.5)
        Colors.red("\n You are exited \n")

    # Reboot cancel
    def reboot_exit():
        time.sleep(0.5)
        Colors.sky_blue("\n You cancelled the reboot.")
        Colors.sky_blue("\n Only install the second step after the reboot.")
        Colors.sky_blue(
            "\n If any error come in this installation we are not the reason. "
        )
        time.sleep(0.5)
        os.system("exit")

    # Author information
    def author():
        Colors.sky_blue("\n                     AUTHOR")
        time.sleep(0.5)
        Colors.orange(
            " \n If this script saves you time. You can give a star on GitHub"
        )
        time.sleep(0.5)
        Colors.orange(
            " \n If any error you can post the issue on the GitHub page: https://github.com/varkmarker/Tp-linkWN722NV2/issues"
        )
        time.sleep(0.5)
        Colors.orange(
            f" \n If you have any suggestions about this tool you can contact me on Twitter."
        )
        time.sleep(0.5)
        Colors.orange(" \n Twitter link: https://twitter.com/varkmarker")
        time.sleep(0.5)
        Colors.light_blue(" \n AUTHOR: VARKMARKER \n")
        time.sleep(0.5)

    # Invalid error message
    def case_default():
        print(
            colr().hex(
                "#00ffff",
                """\n                 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~""",
            ),
        )

        Colors.red("    ....Invalid option....")

    def exit_author():
        Operators.author()
        os.system("exit")


# Before the rebooting
class Before:
    def reboot():
        time.sleep(0.5)
        Colors.red("\n REBOOTING")
        time.sleep(0.5)
        os.system("sudo reboot")

    # Session one
    def session_one():
        time.sleep(0.5)
        # Updating
        Colors.light_blue(" \n UPDATE STARTED ")
        time.sleep(0.5)
        os.system("\n sudo apt-get update")
        time.sleep(0.5)
        Colors.light_blue("\n UPDATE FINISHED ")
        time.sleep(0.5)
        # Upgrading
        Colors.light_blue("\n UPGRADE STARTED ")
        time.sleep(0.5)
        os.system("\n sudo apt-get upgrade")
        time.sleep(0.5)
        Colors.light_blue("\n UPGRADE FINISHED ")
        time.sleep(0.5)
        # Installing bc
        Colors.light_green("\n INSTALLING BC ")
        time.sleep(0.5)
        os.system("\n sudo apt-get install bc")
        time.sleep(0.5)
        Colors.light_green("\n INSTALLED BC ")
        time.sleep(0.5)
        # Installing bulid-essential
        Colors.light_green("\n INSTALLING BUILD-ESSENTIAL")
        time.sleep(0.5)
        os.system("\n sudo apt-get install build-essential")
        time.sleep(0.5)
        Colors.light_green("\n INSTALLED BUILD-ESSENTIAL")
        time.sleep(0.5)
        # Installing libelf-dev
        Colors.light_green("\n INSTALLING LIBELF-DEV")
        time.sleep(0.5)
        os.system("\n sudo apt-get install libelf-dev")
        time.sleep(0.5)
        Colors.light_green("\n INSTALLED LIBELF-DEV")
        time.sleep(0.5)
        # Installing linux-headers
        Colors.light_green("\n INSTALLING LINUX-HEADERS-UNAME-R")
        time.sleep(0.5)
        os.system("\n sudo apt-get install linux-headers-$(uname -r)")
        time.sleep(0.5)
        Colors.light_green("\n INSTALLED LINUX-HEADERS-UNAME-R")
        time.sleep(0.5)
        # Installing dkms
        Colors.light_blue("\n INSTALLING DKMS")
        time.sleep(0.5)
        os.system("\n sudo apt-get install dkms")
        time.sleep(0.5)
        Colors.light_blue("\n INSTALLED DKMS")
        time.sleep(0.5)
        # Installing removing r8188eu
        Colors.light_gnome("\n REMOVING R8188EU.KO FILE FROM THE KERNAL")
        time.sleep(0.5)
        os.system("\n sudo rmmod r8188eu.ko")
        Colors.light_gnome("\n REMOVED THE R8188EU.KO FILE FROM THE KERNAL")
        time.sleep(0.5)
        # Command execution
        Colors.red("\n COMMAND EXECUTION STARTED")
        os.system('sudo echo "blacklist r8188eu" > "/etc/modprobe.d/realtek.conf" ')
        time.sleep(0.5)
        Colors.red("\n COMMAND EXECUTION COMPLETED")
        time.sleep(0.5)
        # Reboot
        Colors.red(" \n  TIME TO REBOOT ")
        time.sleep(0.5)
        Colors.violet(
            "\n  AFTER THE REBOOT YOU RUN THIS SCRIPT AGAIN CHOOSE THE SECOND OPTION"
        )
        time.sleep(0.5)
        Colors.red("\n Are you sure to reboot your system y or n")
        time.sleep(0.5)
        choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
        switch = {
            "y": Before.reboot,
            "Y": Before.reboot,
            "yes": Before.reboot,
            "YES": Before.reboot,
            "NO": Operators.reboot_exit,
            "n": Operators.reboot_exit,
            "no": Operators.reboot_exit,
            "N": Operators.reboot_exit,
        }
        try:
            switch_case = switch.get(str(choice), Operators.case_default)
            switch_case()
        except ValueError:
            Operators.case_default()





# Privileges check
# if os.geteuid() != 0:
#     Colors.red(" \n THIS SCRIPT REQUIRES SUDO PRIVILEGES . \n")
#     exit(1)
# else:
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
# Main choice function that call functions
Colors.sky_blue(
    "\n   [1] FIRST STEP      [2] SECOND STEP \n   [3] MAKE ERROR STEP [4] AUTOMATIC CODE GIVER + EXECUTING \n   [5] EXIT"
)
time.sleep(0.5)
choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
switch = {
    1: Before.session_one,
    2: After.session_two,
    4: CodeCreater.injection_code,
    5: Operators.exit,
}
try:
    switch_case = switch.get(int(choice), Operators.case_default)
    switch_case()
except ValueError:
    Operators.case_default()