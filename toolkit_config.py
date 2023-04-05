""" toolkit_config.py

Project configuration file
"""
import os

PRJDIR = '. ./'   #'\\Users\\Lyle2\\PycharmProjects\\toolkit'
ROOTDIR = os.path.join(PRJDIR, 'project1')
DATDIR = os.path.join(ROOTDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'TICKERS.txt')

print(TICPATH)