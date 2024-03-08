import subprocess
import optparse
def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac",help="new mac adresss")
    return parse_object.parse_args()


def macchanger(user_interface,user_mac):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])

(get,arguments)=get_user_input()
macchanger(get.interface,get.mac)