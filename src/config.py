import argparse


class Config:

    def __init__(self):

        self.environment: str
        self.database_path = 'mysql+mysqlconnector://backend:PeanutButter69!@localhost/webcomic'
