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
        Colors.sky_blue(" \n Twitter link: https://twitter.com/varkmarker")
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
        Colors.red("")
        os.system("sudo reboot")

    # Session one
    def session_one():
        time.sleep(0.5)
        # Updating
        Colors.light_blue(" \n UPDATE STARTED ")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get update")
        time.sleep(0.5)
        # Upgrading
        Colors.light_blue("\n UPGRADE STARTED ")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get full-upgrade")
        time.sleep(0.5)
        # Installing bc
        Colors.light_blue("\n INSTALLING BC ")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y bc")
        time.sleep(0.5)
        Colors.light_blue("\n INSTALLING REQUIRE TOOLS ")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y aircrack-ng wireless-tools net-tools")
        time.sleep(0.5)
        # Installing bulid-essential
        Colors.light_blue("\n INSTALLING BUILD-ESSENTIAL")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y build-essential")
        time.sleep(0.5)
        # Installing libelf-dev
        Colors.light_blue("\n INSTALLING LIBELF-DEV")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y libelf-dev")
        time.sleep(0.5)
        # Installing linux-headers
        Colors.light_blue("\n INSTALLING LINUX-HEADERS-UNAME-R")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y linux-headers-$(uname -r)")
        time.sleep(0.5)
        # Installing dkms
        Colors.light_blue("\n INSTALLING DKMS")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y dkms")
        time.sleep(0.5)
        # Installing removing r8188eu
        Colors.light_gnome("\n REMOVING R8188EU.KO FILE FROM THE KERNAL")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo rmmod r8188eu.ko")
        # Command execution
        Colors.red("\n COMMAND EXECUTION STARTED")
        Colors.red("")
        os.system('sudo echo "blacklist r8188eu" > "/etc/modprobe.d/realtek.conf" ')
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


class ModeEnable:
    # Get user wifi drive interface name
    def injection_code():
        time.sleep(0.5)
        Colors.red("\n IWCONFIG RESULT")
        Colors.orange("")
        os.system("\n sudo iwconfig")
        time.sleep(0.5)
        Colors.sky_blue("\n DRIVE INSTALLATION COMPLETED .")
        time.sleep(0.5)
        Colors.light_green("\n IF YOU WANT TO CHECK MONITOR MODE : PRESS = y")
        time.sleep(0.5)
        Colors.light_green("\n IF YOU WANT TO  EXIT FROM THE TOOL : PRESS = n")
        time.sleep(0.5)
        Colors.sky_blue("\n If you want to continue y or n : ")
        choice = input(colr().hex("#fff300", " > ", rgb_mode=True))
        choice = choice.lower()

        def next_code():
            Colors.red("\n Enter you wifi adapter system name ? \n Eg: wlan0")
            time.sleep(0.5)
            interface = input(colr().hex("#fff300", "> ", rgb_mode=True))
            time.sleep(0.5)
            Colors.sky_blue(f" \n INTERFACE NAME : {interface}\n")
            name_upper = interface.upper()
            name_lower = interface.lower()
            time.sleep(0.5)
            Colors.cream("This is your name of the driver y or n")
            choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
            choice = choice.lower()
            # Choice of show and excute command.
            def show_execute(name_upper, name_lower):
                Colors.light_blue("\n [1] SHOW THE COMMAND  [2] Execute   \n [3] Exit")
                px = input(colr().hex("#fff300", "> ", rgb_mode=True))
                # Monitor mode command showing to the user.
                def show_the_command(name_upper, name_lower):
                    time.sleep(0.5)
                    Colors.red("\n COMMANDS FOR MONITOR MODE ENABLING ")
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} DOWN COMMAND")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo ifconfig {name_lower} down")
                    time.sleep(0.5)
                    Colors.light_blue("\n AIRMON-NG KILL ALL PROCESS")
                    time.sleep(0.5)
                    Colors.green("\n $ sudo airmon-ng check kill")
                    time.sleep(0.5)
                    Colors.light_blue("\n ENABLE MONITOR MODE COMMAND")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo iwconfig {name_lower} mode monitor")
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} UP COMMAND")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo ifconfig {name_lower} up")
                    time.sleep(0.5)
                    Colors.light_blue(
                        "\n SHOWING THE IWCONFIG RESULT. \n CHECK MONITOR MODE IS ENABLE"
                    )
                    time.sleep(0.5)
                    Colors.green("\n $ iwconfig")
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} INJECTION COMMAND")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo aireplay-ng --test {name_lower}")
                    time.sleep(0.5)
                    Colors.red(
                        "\n If you want to change the wifi to normal state as well your network manager. Use the below commands."
                    )
                    time.sleep(0.5)
                    Colors.orange(
                        "\n Commands for change the monitor mode to auto mode"
                    )
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} DOWN COMMAND")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo ifconfig {name_lower} down")
                    time.sleep(0.5)
                    Colors.light_blue("\n CHANGE MODE TO AUTO")
                    Colors.green(f"\n $ sudo iwconfig {name_lower} mode auto")
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} UP COMMAND")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo ifconfig {name_lower} up")
                    time.sleep(0.5)
                    Colors.orange("\n Command for restart the network manager.")
                    time.sleep(0.5)
                    Colors.green(f"\n $ sudo systemctl restart NetworkManager")
                    time.sleep(0.5)
                    Colors.red(
                        "\n You can test by entering the following command manually"
                    )
                    Operators.exit_author()

                # Monitor mode execute command
                def execute_the_command(name_upper, name_lower):
                    # Monior mode change to auto [mmca] and restart network manager [rnm]
                    def mmca_rnm():
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} DOWN ")
                        time.sleep(0.5)
                        Colors.red("")
                        os.system(f"sudo ifconfig {name_lower} down")
                        time.sleep(0.5)
                        os.system(f"sudo iwconfig {name_lower} mode auto")
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} UP ")
                        time.sleep(0.5)
                        os.system(f"sudo ifconfig {name_lower} up")
                        time.sleep(0.5)
                        Colors.orange("\n Network Manager Restarted")
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system(f"sudo systemctl restart NetworkManager")
                        time.sleep(0.5)
                        Operators.exit_author()

                    time.sleep(0.5)
                    Colors.red(f"\n {name_upper} DOWN")
                    time.sleep(0.5)
                    Colors.blue("")
                    os.system(f" sudo ifconfig {name_lower} down")
                    time.sleep(0.5)
                    Colors.red("\n AIRMON-NG KILL ALL PROCESS")
                    time.sleep(0.5)
                    Colors.blue("")
                    os.system("sudo airmon-ng check kill")
                    time.sleep(0.5)
                    Colors.red("\n ENABLE MONITOR MODE")
                    time.sleep(0.5)
                    Colors.blue("")
                    os.system(f"sudo iwconfig {name_lower} mode monitor")
                    time.sleep(0.5)
                    Colors.red(f"\n {name_upper} UP")
                    time.sleep(0.5)
                    Colors.blue("")
                    os.system(f"sudo ifconfig {name_lower} up")
                    time.sleep(0.5)
                    Colors.red(
                        "\n SHOWING THE IWCONFIG RESULT. \n CHECK MONITOR MODE IS ENABLE"
                    )
                    time.sleep(0.5)
                    Colors.blue("")
                    os.system(" iwconfig")
                    time.sleep(0.5)
                    Colors.red(f"\n {name_upper} INJECTION STARTED")
                    time.sleep(0.5)
                    Colors.blue("")
                    os.system(f"sudo aireplay-ng --test {name_lower}")
                    time.sleep(0.7)
                    Colors.red(f"\n {name_upper} INJECTION STOPPED")
                    time.sleep(0.5)
                    # choice for change monitor mode to auto and restart network manager
                    Colors.red(
                        " \n If you want to change the wifi to normal state as well your network manager. y or n "
                    )
                    choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
                    choice = choice.lower()
                    try:
                        if choice == "y" or choice == "yes":
                            mmca_rnm()
                        elif choice == "n" or choice == "no":
                            Operators.exit_author()
                        else:
                            Operators.case_default()
                    except ValueError:
                        Operators.case_default()

                try:
                    if px == "1":
                        show_the_command(name_upper, name_lower)
                    elif px == "2":
                        execute_the_command(name_upper, name_lower)
                    elif px == "3":
                        Operators.exit_author()
                    else:
                        Operators.case_default()
                except ValueError:
                    Operators.case_default()

            try:
                if choice == "y" or choice == "yes":
                    show_execute(name_upper, name_lower)
                elif choice == "n" or choice == "no":
                    CodeCreater.injection_code()
                else:
                    Operators.case_default()
            except ValueError:
                Operators.case_default()

        try:
            if choice == "y" or choice == "yes":
                next_code()
            elif choice == "n" or choice == "no":
                Operators.exit_author()
            else:
                Operators.case_default()
        except ValueError:
            Operators.case_default()


class CodeCreater:
    # Get user wifi drive interface name
    def injection_code():
        time.sleep(0.5)
        Colors.blue("")
        os.system("sudo iwconfig")
        time.sleep(0.5)
        Colors.red("\n Enter you wifi adapter system name ? \n Eg: wlan0")
        time.sleep(0.5)
        interface = input(colr().hex("#fff300", "> ", rgb_mode=True))
        time.sleep(0.5)
        Colors.sky_blue(f" \n INTERFACE NAME : {interface}\n")
        name_upper = interface.upper()
        name_lower = interface.lower()
        time.sleep(0.5)
        Colors.cream("This is your name of the driver y or n")
        choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
        choice = choice.lower()
        # Choice of show and excute command.
        def show_execute(name_upper, name_lower):
            Colors.light_blue("\n [1] SHOW THE COMMAND  [2] Execute   \n [3] Exit")
            px = input(colr().hex("#fff300", "> ", rgb_mode=True))
            # Monitor mode command showing to the user.
            def show_the_command(name_upper, name_lower):
                time.sleep(0.5)
                Colors.red("\n COMMANDS FOR MONITOR MODE ENABLING ")
                time.sleep(0.5)
                Colors.light_blue(f"\n {name_upper} DOWN COMMAND")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo ifconfig {name_lower} down")
                time.sleep(0.5)
                Colors.light_blue("\n AIRMON-NG KILL ALL PROCESS")
                time.sleep(0.5)
                Colors.green("\n $ sudo airmon-ng check kill")
                time.sleep(0.5)
                Colors.light_blue("\n ENABLE MONITOR MODE COMMAND")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo iwconfig {name_lower} mode monitor")
                time.sleep(0.5)
                Colors.light_blue(f"\n {name_upper} UP COMMAND")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo ifconfig {name_lower} up")
                time.sleep(0.5)
                Colors.light_blue(
                    "\n SHOWING THE IWCONFIG RESULT. \n CHECK MONITOR MODE IS ENABLE"
                )
                time.sleep(0.5)
                Colors.green("\n $ iwconfig")
                time.sleep(0.5)
                Colors.light_blue(f"\n {name_upper} INJECTION COMMAND")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo aireplay-ng --test {name_lower}")
                time.sleep(0.5)
                Colors.red(
                    "\n If you want to change the wifi to normal state as well your network manager. Use the below commands."
                )
                time.sleep(0.5)
                Colors.orange("\n Commands for change the monitor mode to auto mode")
                time.sleep(0.5)
                Colors.light_blue(f"\n {name_upper} DOWN COMMAND")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo ifconfig {name_lower} down")
                time.sleep(0.5)
                Colors.light_blue("\n CHANGE MODE TO AUTO")
                Colors.green(f"\n $ sudo iwconfig {name_lower} mode auto")
                time.sleep(0.5)
                Colors.light_blue(f"\n {name_upper} UP COMMAND")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo ifconfig {name_lower} up")
                time.sleep(0.5)
                Colors.orange("\n Command for restart the network manager.")
                time.sleep(0.5)
                Colors.green(f"\n $ sudo systemctl restart NetworkManager")
                time.sleep(0.5)
                Colors.red("\n You can test by entering the following command manually")
                Operators.exit_author()

            # Monitor mode execute command
            def execute_the_command(name_upper, name_lower):
                # Monior mode change to auto [mmca] and restart network manager [rnm]
                def mmca_rnm():
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} DOWN ")
                    time.sleep(0.5)
                    Colors.red("")
                    os.system(f"sudo ifconfig {name_lower} down")
                    time.sleep(0.5)
                    Colors.red("")
                    os.system(f"sudo iwconfig {name_lower} mode auto")
                    time.sleep(0.5)
                    Colors.light_blue(f"\n {name_upper} UP ")
                    time.sleep(0.5)
                    Colors.red("")
                    os.system(f"sudo ifconfig {name_lower} up")
                    time.sleep(0.5)
                    Colors.orange("\n Network Manager Restarted")
                    time.sleep(0.5)
                    Colors.red("")
                    os.system(f"sudo systemctl restart NetworkManager")
                    time.sleep(0.5)
                    Operators.exit_author()

                time.sleep(0.5)
                Colors.red(f"\n {name_upper} DOWN")
                time.sleep(0.5)
                Colors.blue("")
                os.system(f" sudo ifconfig {name_lower} down")
                time.sleep(0.5)
                Colors.red("\n AIRMON-NG KILL ALL PROCESS")
                time.sleep(0.5)
                Colors.blue("")
                os.system("sudo airmon-ng check kill")
                time.sleep(0.5)
                Colors.red("\n ENABLE MONITOR MODE")
                time.sleep(0.5)
                Colors.blue("")
                os.system(f"sudo iwconfig {name_lower} mode monitor")
                time.sleep(0.5)
                Colors.red(f"\n {name_upper} UP")
                time.sleep(0.5)
                Colors.blue("")
                os.system(f"sudo ifconfig {name_lower} up")
                time.sleep(0.5)
                Colors.red(
                    "\n SHOWING THE IWCONFIG RESULT. \n CHECK MONITOR MODE IS ENABLE"
                )
                time.sleep(0.5)
                Colors.blue("")
                os.system(" iwconfig")
                time.sleep(0.5)
                Colors.red(f"\n {name_upper} INJECTION STARTED")
                time.sleep(0.5)
                Colors.blue("")
                os.system(f"sudo aireplay-ng --test {name_lower}")
                time.sleep(0.7)
                Colors.red(f"\n {name_upper} INJECTION STOPPED")
                time.sleep(0.5)
                # choice for change monitor mode to auto and restart network manager
                Colors.red(
                    " \n If you want to change the wifi to normal state as well your network manager. y or n "
                )
                choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
                choice = choice.lower()
                try:
                    if choice == "y" or choice == "yes":
                        mmca_rnm()
                    elif choice == "n" or choice == "no":
                        Operators.exit_author()
                    else:
                        Operators.case_default()
                except ValueError:
                    Operators.case_default()

            try:
                if px == "1":
                    show_the_command(name_upper, name_lower)
                elif px == "2":
                    execute_the_command(name_upper, name_lower)
                elif px == "3":
                    Operators.exit_author()
                else:
                    Operators.case_default()
            except ValueError:
                Operators.case_default()

        try:
            if choice == "y" or choice == "yes":
                show_execute(name_upper, name_lower)
            elif choice == "n" or choice == "no":
                CodeCreater.injection_code()
            else:
                Operators.case_default()
        except ValueError:
            Operators.case_default()


# class MakeError:
class MakeError:
    # Comment Repository
    def comment_repo():
        # Comment
        def ct_repo():
            replace = [
                "#deb http://http.kali.org/kali kali-rolling main contrib non-free"
            ]

            with open("/etc/apt/sources.list", "r") as file:
                commentrepo = file.read()

                commentrepo = commentrepo.replace(
                    "deb http://http.kali.org/kali kali-rolling main contrib non-free",
                    replace[0],
                )
            with open("/etc/apt/sources.list", "w") as file:
                file.write("" + commentrepo)

        def no_case():

            print(colr().hex("#ff0000", "Kali Repo Not Comment Yet", rgb_mode=True))

        answer = input(
            colr().hex(
                "#af50a2",
                "If you want to comment [ # ] the repository line of kali linux in \nthe source file that adds by this script y or n : ",
                rgb_mode=True,
            )
        )

        # Comment repo switch
        switch = {
            "y": ct_repo,
            "Y": ct_repo,
            "yes": ct_repo,
            "YES": ct_repo,
            "NO": no_case,
            "n": no_case,
            "no": no_case,
            "N": no_case,
        }

        switch_case = switch.get(str(answer), Operators.case_default)
        switch_case()

    def iferrormake():
        time.sleep(0.5)
        Colors.orange(" \n If you get make error again")
        time.sleep(0.5)
        Colors.orange(" \n Please message me on twitter with the error photo.")
        time.sleep(0.5)
        Colors.orange(" \n Twitter link: https://twitter.com/varkmarker")
        time.sleep(0.5)
        Colors.light_blue(" \n AUTHOR: VARKMARKER \n")
        time.sleep(0.5)

    def aftermake():
        time.sleep(0.5)
        # Make installing
        Colors.light_blue("\n MAKE INSTALLING")
        time.sleep(0.5)
        Colors.red("")
        os.system("sudo apt install -y make")
        time.sleep(0.5)
        # Installing bulid-essential
        Colors.light_blue("\n INSTALLING BUILD-ESSENTIAL")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y build-essential")
        time.sleep(0.5)
        # Installing dkms
        Colors.light_blue("\n INSTALLING DKMS")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get install -y dkms")
        time.sleep(0.5)
        # Make command's
        Colors.light_blue("\n MAKING STARTED")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo make")
        Colors.light_blue(
            " \n If you get any Error messages during the Make command execution y or n:"
        )
        time.sleep(0.5)
        choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
        choice = choice.lower()
        #  If the  make function has no error. This command will execute during the installation.
        def make_after():

            time.sleep(0.5)
            # Make install
            Colors.light_blue("\n RUNNING MAKE INSTALL ")
            time.sleep(0.5)
            Colors.red("")
            os.system("\n sudo make install")
            time.sleep(0.5)
            os.system("\n sudo modprobe 8188eu")
            time.sleep(0.5)
            # Calling the comment repository function
            MakeError.comment_repo()

        try:
            if choice == "y" or choice == "yes":
                MakeError.iferrormake()
            elif choice == "n" or choice == "no":
                make_after()
        except ValueError:
            Operators.case_default()

    def solvemake():
        Colors.red(" \n REMOVING MAKE COMMAND ")
        time.sleep(0.5)
        Colors.blue("")
        os.system("sudo apt-get remove make")
        # Check kali linux repository already exist or not
        # kali linux リポジトリが既に存在するかどうかを確認します
        file_path = "/etc/apt/sources.list"
        one_string = "deb http://http.kali.org/kali kali-rolling main contrib non-free"
        second_string = (
            "#deb http://http.kali.org/kali kali-rolling main contrib non-free"
        )

        with open(file_path, "r") as f:
            file_contents = f.read()

        # Check if the line is found in the file
        if second_string in file_contents:
            # Comment Repository
            def comment_repo():
                replace = [
                    "deb http://http.kali.org/kali kali-rolling main contrib non-free"
                ]

                with open("/etc/apt/sources.list", "r") as file:
                    Commandrepo = file.read()

                    Commandrepo = Commandrepo.replace(
                        "#deb http://http.kali.org/kali kali-rolling main contrib non-free",
                        replace[0],
                    )
                with open("/etc/apt/sources.list", "w") as file:
                    file.write("" + Commandrepo)
                os.system("sudo apt-get update")
                MakeError.aftermake()

            comment_repo()

        elif one_string in file_contents:
            os.system("sudo apt-get update")
            MakeError.aftermake()
        else:
            # Add Repository
            def add_repo():
                with open("/etc/apt/sources.list", "a") as file:
                    file.write(
                        "\n".join(
                            [
                                "#KALI LINUX REPOSITORY ",
                                "deb http://http.kali.org/kali kali-rolling main contrib non-free",
                            ]
                        )
                    )

                os.system(
                    "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ED444FF07D8D0BF6",
                )

                os.system("sudo apt-get update")
                MakeError.aftermake()

            add_repo()


class After:
    # Session two
    def session_two():
        # Updating
        time.sleep(0.5)
        Colors.light_blue(" \n UPDATE STARTED ")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo apt-get update")
        time.sleep(0.5)
        # Make command's
        Colors.light_blue("\n MAKING STARTED")
        time.sleep(0.5)
        Colors.red("")
        os.system("\n sudo make")
        time.sleep(0.5)
        Colors.light_blue(
            " \n If you get any Error messages during the Make command execution y or n:"
        )
        time.sleep(0.5)
        choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
        choice = choice.lower()
        #  If the  make function has no error. This command will execute during the installation.
        def make_after():

            time.sleep(0.5)
            # Make install
            Colors.light_blue("\n RUNNING MAKE INSTALL ")
            time.sleep(0.5)
            Colors.red("")
            os.system("\n sudo make install")
            time.sleep(0.5)
            Colors.light_blue("\n MAKE INSTALL FINISHED")
            time.sleep(0.5)
            Colors.red("")
            os.system("\n sudo modprobe 8188eu")
            time.sleep(0.5)
            # Calling the function for enabling monitor mode
            ModeEnable.injection_code()

        try:
            if choice == "y" or choice == "yes":
                MakeError.solvemake()
            elif choice == "n" or choice == "no":
                make_after()
        except ValueError:
            Operators.case_default()


# Kali linux or parrotos
class Os:
    def parrot_kali():
        time.sleep(0.5)
        Colors.sky_blue("\n Updating")
        Colors.red("")
        os.system("sudo apt-get update")
        time.sleep(0.)
        Colors.sky_blue("\nInstalling driver")
        Colors.red("")
        os.system("sudo apt-get install realtek-rtl8188eus-dkms")
        time.sleep(0.5)
        Colors.sky_blue("\n Enabling Monitor Mode")

        def injection_code():
            time.sleep(0.5)
            Colors.red("\n IWCONFIG RESULT")
            Colors.orange("")
            os.system("\n sudo iwconfig")
            time.sleep(0.5)
            Colors.sky_blue("\n DRIVE INSTALLATION COMPLETED .")
            time.sleep(0.5)
            Colors.light_green("\n IF YOU WANT TO CHECK MONITOR MODE : PRESS = y")
            time.sleep(0.5)
            Colors.light_green("\n IF YOU WANT TO  EXIT FROM THE TOOL : PRESS = n")
            time.sleep(0.5)
            Colors.sky_blue("\n If you want to continue y or n : ")
            choice = input(colr().hex("#fff300", " > ", rgb_mode=True))
            choice = choice.lower()

            def next_code():
                Colors.red("\n Enter you wifi adapter system name ? \n Eg: wlan0")
                time.sleep(0.5)
                interface = input(colr().hex("#fff300", "> ", rgb_mode=True))
                time.sleep(0.5)
                Colors.sky_blue(f" \n INTERFACE NAME : {interface}\n")
                name_upper = interface.upper()
                name_lower = interface.lower()
                time.sleep(0.5)
                Colors.cream("This is your name of the driver y or n")
                choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
                choice = choice.lower()
                # Choice of show and excute command.
                def show_execute(name_upper, name_lower):
                    Colors.light_blue(
                        "\n [1] SHOW THE COMMAND  [2] Execute   \n [3] Exit"
                    )
                    px = input(colr().hex("#fff300", "> ", rgb_mode=True))
                    # Monitor mode command showing to the user.
                    def show_the_command(name_upper, name_lower):
                        time.sleep(0.5)
                        Colors.red("\n COMMANDS FOR MONITOR MODE ENABLING ")
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} DOWN COMMAND")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo ifconfig {name_lower} down")
                        time.sleep(0.5)
                        Colors.light_blue("\n AIRMON-NG KILL ALL PROCESS")
                        time.sleep(0.5)
                        Colors.green("\n $ sudo airmon-ng check kill")
                        time.sleep(0.5)
                        Colors.light_blue("\n ENABLE MONITOR MODE COMMAND")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo iwconfig {name_lower} mode monitor")
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} UP COMMAND")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo ifconfig {name_lower} up")
                        time.sleep(0.5)
                        Colors.light_blue(
                            "\n SHOWING THE IWCONFIG RESULT. \n CHECK MONITOR MODE IS ENABLE"
                        )
                        time.sleep(0.5)
                        Colors.green("\n $ iwconfig")
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} INJECTION COMMAND")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo aireplay-ng --test {name_lower}")
                        time.sleep(0.5)
                        Colors.red(
                            "\n If you want to change the wifi to normal state as well your network manager. Use the below commands."
                        )
                        time.sleep(0.5)
                        Colors.orange(
                            "\n Commands for change the monitor mode to auto mode"
                        )
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} DOWN COMMAND")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo ifconfig {name_lower} down")
                        time.sleep(0.5)
                        Colors.light_blue("\n CHANGE MODE TO AUTO")
                        Colors.green(f"\n $ sudo iwconfig {name_lower} mode auto")
                        time.sleep(0.5)
                        Colors.light_blue(f"\n {name_upper} UP COMMAND")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo ifconfig {name_lower} up")
                        time.sleep(0.5)
                        Colors.orange("\n Command for restart the network manager.")
                        time.sleep(0.5)
                        Colors.green(f"\n $ sudo systemctl restart NetworkManager")
                        time.sleep(0.5)
                        Colors.red(
                            "\n You can test by entering the following command manually"
                        )
                        Operators.exit_author()

                    # Monitor mode execute command
                    def execute_the_command(name_upper, name_lower):
                        # Monior mode change to auto [mmca] and restart network manager [rnm]
                        def mmca_rnm():
                            time.sleep(0.5)
                            Colors.light_blue(f"\n {name_upper} DOWN ")
                            time.sleep(0.5)
                            Colors.red("")
                            os.system(f"sudo ifconfig {name_lower} down")
                            time.sleep(0.5)
                            os.system(f"sudo iwconfig {name_lower} mode auto")
                            time.sleep(0.5)
                            Colors.light_blue(f"\n {name_upper} UP ")
                            time.sleep(0.5)
                            os.system(f"sudo ifconfig {name_lower} up")
                            time.sleep(0.5)
                            Colors.orange("\n Network Manager Restarted")
                            time.sleep(0.5)
                            Colors.blue("")
                            os.system(f"sudo systemctl restart NetworkManager")
                            time.sleep(0.5)
                            Operators.exit_author()

                        time.sleep(0.5)
                        Colors.red(f"\n {name_upper} DOWN")
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system(f" sudo ifconfig {name_lower} down")
                        time.sleep(0.5)
                        Colors.red("\n AIRMON-NG KILL ALL PROCESS")
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system("sudo airmon-ng check kill")
                        time.sleep(0.5)
                        Colors.red("\n ENABLE MONITOR MODE")
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system(f"sudo iwconfig {name_lower} mode monitor")
                        time.sleep(0.5)
                        Colors.red(f"\n {name_upper} UP")
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system(f"sudo ifconfig {name_lower} up")
                        time.sleep(0.5)
                        Colors.red(
                            "\n SHOWING THE IWCONFIG RESULT. \n CHECK MONITOR MODE IS ENABLE"
                        )
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system(" iwconfig")
                        time.sleep(0.5)
                        Colors.red(f"\n {name_upper} INJECTION STARTED")
                        time.sleep(0.5)
                        Colors.blue("")
                        os.system(f"sudo aireplay-ng --test {name_lower}")
                        time.sleep(0.7)
                        Colors.red(f"\n {name_upper} INJECTION STOPPED")
                        time.sleep(0.5)
                        Colors.orange("\n IF INJECTION IS NOT WORKING TRY USING THE FIRST STEP AND SECOND STEP INSTALLATION")
                        # choice for change monitor mode to auto and restart network manager
                        Colors.red(
                            " \n If you want to change the wifi to normal state as well your network manager. y or n "
                        )
                        choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
                        choice = choice.lower()
                        try:
                            if choice == "y" or choice == "yes":
                                mmca_rnm()
                            elif choice == "n" or choice == "no":
                                Operators.exit_author()
                            else:
                                Operators.case_default()
                        except ValueError:
                            Operators.case_default()

                    try:
                        if px == "1":
                            show_the_command(name_upper, name_lower)
                        elif px == "2":
                            execute_the_command(name_upper, name_lower)
                        elif px == "3":
                            Operators.exit_author()
                        else:
                            Operators.case_default()
                    except ValueError:
                        Operators.case_default()

                try:
                    if choice == "y" or choice == "yes":
                        show_execute(name_upper, name_lower)
                    elif choice == "n" or choice == "no":
                        injection_code()
                    else:
                        Operators.case_default()
                except ValueError:
                    Operators.case_default()

            try:
                if choice == "y" or choice == "yes":
                    next_code()
                elif choice == "n" or choice == "no":
                    Operators.exit_author()
                else:
                    Operators.case_default()
            except ValueError:
                Operators.case_default()

        injection_code()


# Privileges check
if os.geteuid() != 0:
    Colors.red(" \n THIS SCRIPT REQUIRES SUDO PRIVILEGES . \n")
    exit(1)
else:
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
        "\n   [1] FIRST STEP               [2] SECOND STEP \n   [3] PARROT OR KALI           [4] AUTOMATIC CODE GIVER \n   [5] EXIT"
    )
    time.sleep(0.5)
    choice = input(colr().hex("#fff300", "> ", rgb_mode=True))
    switch = {
        1: Before.session_one,
        2: After.session_two,
        3: Os.parrot_kali,
        4: CodeCreater.injection_code,
        5: Operators.exit_author,
    }
    try:
        switch_case = switch.get(int(choice), Operators.case_default)
        switch_case()
    except ValueError:
        Operators.case_default()
