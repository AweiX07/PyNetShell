pms_makedat=(1.0,"Beta","")
def startup():
    if not pms_makedat[1]:
        print("?!\n\"What The HELL MY GOD?!\"\n\nNotice:The MakeData is Wrong.\nPlease make it sure that your PNS is safe.\n")
    else:print("PyNetShell Version:"+str(pms_makedat[0])+"-"+str(pms_makedat[1])+" by AweiXZS")
    if pms_makedat[2]:print("\nMakeNote:"+str(pms_makedat[2])+"\n\n")
    else:print("")
startup()
#Start to load module
import os
import subprocess
import socket
import hashlib
import random
import base64
#import sys
'''
import tkinter
import paramiko
import ftplib
import time
import datetime
import pyshark
import requests
import zipp
import numpy
import math
import select
import psutil
import bz2
import gzip
import shutil
import tarfile
import lzma
import secrets
import shlex
import platform
import smtplib
import xml
import re
import threading
import json
import pathlib
import poplib
import imaplib
import http.server
import traceback
import cycler
import filecmp
'''
def localhandler(com):
    global handlercwd,pns_retext
    from os import getcwd
    #retext=None
    try:retext=exec(com)
    except Exception as e:print("PyError:\n"+str(e))
    finally:
        handlercwd=getcwd()
        return None

def pns_valueedit(name,value):
    globals()[name]=value

def empty(com):return "EMPTY:"+com

pns_retext=None
pns_return_show=1
pns_resize=1024
pns_handler_show=0
#pns_errshowed=0
handlerfunction=localhandler
handler=empty
handleruser=str(os.getlogin())
handlerhost="localhost"
handlercwd=os.getcwd()
key="92043b45887f56d192fa25ba3f292b81ab40af927e42f0cd681847b0b1c9d6c5"


def debug_test():print("test")

def coder(mod,strings):
    from base64 import b64encode as ben
    from base64 import b64dncode as bde
    try:
        if mod == 0:
            return ben(strings.encode())
        elif mod == 1:
            return dbe(strings).decode()
        else:
            print("Coder:ValueError:'"+strings+"',mode="+str(mod))
            return None
    except binascii.Error:
        return None
    except Exception as cer:
        print("Coder:UnknowError >"+str(cer)+"<-('"+strings+"',mode="+str(mod)+")")
        return None

def net_handler(com):
    global handler,handlercwd,pns_resize
    handler.send(coder(0,com))
    return coder(1,handler.recv(pns_resize))
    #if ddbb==None:
        #print()

def pns_connect(ip,port,tkey):
    global handler,handleruser,handlerhost,handercwd
    import socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Trying to connect: "+ip+"&"+port+" ......",end="")
    cnum=s.connect_ex((ip,port))
    if cnum:
        print("Failed\n:(\nErrorCode:"+cnum)
        s.close()
        return 0
    else:
        print("Port Availiable")
    s.send(coder(0,tkey))
    data=s.recv(1024)
    if coder(1,data) == "OK":
        print("Key Pass")
        handlerlist=[]
        for i in ["Get_user","Get_cwd"]:
            db=" ![UNKNOW]! "
            s.send(coder(0,i))
            db=coder(1,s.recv(1024))
            print(i+":"+db)
            handlerlist.append(db)
        handler=s
        handleruser=handlerlist[0]
        handlerhost=s.getsockname()[0]+str(s.getsockname()[1])
        handlercwd=handlerlist[1]
        handlerfunction=net_handler
        print("Connect Succerrful")

def pns_cdto(path):
    from os import chdir,getcwd
    chdir(str(path))
    print(getcwd())

def fcpy(path1,path2):
    p1=open(path1,"rb")
    p2=open(path2,"wb")
    text=b"PNS_COPIED_WITHOUT_ANYTHING"
    dnum=0
    while text:
        text=p1.readline()
        dnum+=len(text)
        p2.write(text)
    del text
    p1.close()
    p2.close()
    print("Finish copying:"+str(dnum))
    return dnum


#startup()
while 1:
    try:
        if pns_handler_show:text=input(handleruser+"@"+handlerhost+"&("+str(os.getcwd())+"):\n"+str(handlerfunction)+"$")
        else:text=input(handleruser+"@"+handlerhost+"&("+str(os.getcwd())+"):\nPNS>")
        if text in "exit":
            break
        elif text == "pns_returnhide":
            pns_return_show=0
            print("Return_Hide")
        elif text == "pns_returnshow":
            pns_return_show=1
            print("Return_Show")
        elif text == "pns_handlerhide":
            pns_handler_show=0
            print("Handler_Hide")
        elif text == "pns_handlershow":
            pns_handler_show=1
            print("Handler_Show")
        elif text == "pns_ml":
            from os import getcwd
            while 1:
                text=input(handleruser+"@"+handlerhost+"&("+str(os.getcwd())+"):\nPNS-MainLoop>")
                if text == "quit":break
                try:exec(text)
                except Exception as e:print("ML-PyError:\n"+str(e))
                finally:handlercwd=getcwd()
            del fetcwd
        else:
            handlerfunction(text)
            if pns_retext != None:
                if pns_return_show:print(str(pns_retext))
    except Exception as ped:
        print("ShellError:\n"+str(ped))
        try:
            os.getcwd()
        except:
            import os
        if input("Advise to reset your handler.Continue using this handler?(N/y)") == "y":
            pass
        else:
            handler=localhandler
#quit()