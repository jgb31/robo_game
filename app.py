from flask import Flask, render_template, request
import subprocess
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    """ 
    Runs the start menu page of the game by generating the start.html file.   

    """
    return render_template('start.html')
	
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    """  
    Runs and sets up the object selection menu for the game. Once an object is
    chosen, it will run the object detection algorithm as a subprocess to
    determine if the object you are looking for is found by the robot.

    """

    #Check if the user request was added to the server
    if request.method == 'POST':
        target_object = None
        cmd = "python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model"
       
        #Keyboard detection
        if request.form["btn_identifier"] == 'keyboard':
            target_object = 'keyboard'

            detectObject(cmd, target_object)

        #Mouse detection
        if request.form["btn_identifier"] == 'mouse':
            target_object = 'mouse'

            detectObject(cmd, target_object)

        #Banana detection
        if request.form["btn_identifier"] == 'banana':
            target_object = 'banana'

            detectObject(cmd, target_object)
        
        return render_template('menu.html')
            
    return render_template('menu.html')
	
@app.route('/found')
def found():
    """  
    Runs and sets up the "Item Found" page by generating the found.html file.

    """

    return render_template('found.html')
	
@app.route('/fail')
def fail():
    """  
    Runs and sets up the "Item Not Found" page by generating the fail.html file.

    """
    return render_template('fail.html')

def detectObject(cmd: str, target_object: str) -> None:
    """ Runs the object detection algorithm as a subprocess, and retreives the objects 
    that are detected in bytes. It then converts the bytes into a utf-8 string to 
    determine if the objects detected matches the item that the user selected on the
    website. 
    
    Args:
        cmd: A string that represents the command to run the object detection algorithm
        target_object: A string of object to be identified
    
    """
    #Run the subprocess for the object detection algorithm
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #Retrieve output from subprocess
    chunk = proc.stdout

    #Convert from bytes to utf-8 to process as string
    chunk = chunk.decode("utf-8")
    
    #Manipulate output string  
    newString = chunk.replace('[','').replace(']','').replace('\'','').replace('\"','')
    newString = newString.rstrip()
    tokens = newString.split(',')
    
    #Loop through detected objects
    for i in range(0, len(tokens), 2):
        confidence = tokens[i + 1]

        #Check if the computer vision detected the object correctly
        if tokens[i] == target_object and float(confidence) > 0.6:
            print("Found!!!!")
            print(tokens[i] + tokens[i + 1])
            webbrowser.open('http://172.20.10.5:5000/found')
            break

        #Check if the correct object is NOT detected
        if i == (len(tokens) - 2):
            #Check if last object is not the target
            if tokens[i] != target_object:
                webbrowser.open('http://172.20.10.5:5000/fail')
                break
            
            #Check if object is target object, but below confidence threshold
            elif tokens[i] == target_object and float(confidence) <= 0.6:
                webbrowser.open('http://172.20.10.5:5000/fail')
                break
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
