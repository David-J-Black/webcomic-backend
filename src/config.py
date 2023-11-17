class Config:

    def __init__(self):

        self.environment: str
        self.database_path = 'mysql+mysqlconnector://root:password@localhost/webcomic'
        self.log_location = '../log/log.log'

        self.admin_pass_hashed: str = '$2a$12$7Jx7sVsbP/2eGQ5K3mdasuKbAahPhalxhKf8JVAtVVwkbHHZFQH2K'