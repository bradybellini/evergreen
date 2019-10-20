import sqlite3
import asyncio

class Module(object):

    def __init__(self, guild):
        self.guild = guild
        
    def moduleCheck(self, guild):
        return guild