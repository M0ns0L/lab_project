
#pip install flask flask-sqlalchemy flask-wtf flask-bcrypt flask-login flask-admin
#pip install pandas

commands = [
    'pip install pandas',
    'pip install flask flask-sqlalchemy flask-wtf flask-bcrypt flask-login flask-admin'
]
import subprocess
def run_commands(commands):
    for command in commands:
        
        # Run each command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Get the output and error (if any)
        output, error = process.communicate()
        
        # Decode and print the output
        print("Output:\n", output.decode())
        
        # Print errors, if any
        if error:
            print("Error:\n", error.decode())
run_commands(commands)
