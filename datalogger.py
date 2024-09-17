import os 
import datetime


class Logger:
    def __init__(self, file_path):
        self.log_file_path = self.file_path
        self.log_file = open(self.log_file_path, 'w')   

    def close(self):
        self.log_file.close()
    
    def create_log(self, log_file_path):
        self.log_file_path = "./log/log.txt"

        if not os.path.exists(self.log_file_path):
            os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
            with open(self.log_file_path, 'w') as f:
                f.write(f"Log file created at {datetime.datetime.now()}\n")
        else:
            with open(self.log_file_path, 'a') as f:
                f.write(f"Log file appended at {datetime.datetime.now()}\n")
        
        self.log_file = open(self.log_file_path, 'a')
        self.log_file.write(f"Log file created at {datetime.datetime.now()}\n")
        self.log_file.flush()
        
        return self.log_file_path
    
    def log(self, message):
        self.log_file.write(message + '\n')
        self.log_file.flush()

    def close(self):
        self.log_file.close()
        
        


