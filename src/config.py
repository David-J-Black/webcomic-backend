import argparse


class Config:

    def __init__(self):

        self.environment: str
        self.database_path = 'mysql+mysqlconnector://root:password@localhost/webcomic'
