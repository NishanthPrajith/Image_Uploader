import subprocess # Used for running commands in the terminal without user input
import sys # Getting the command line argument
import shutil # Moving files from one location to another

class imageUploader:
    def __init__(self):
        self.folderPath = "NishanthPrajith18.github.io/" # Replace this with the path to the webiste folder
        self.filePath = "NishanthPrajith18.github.io/resume.html" # Replace this with the path to the file that has the marker for adding code
        self.imageFolder = "projectImages/" # Replace with image folder name
        self.imagePath = "/home/nishanth/Desktop/" # Replace with path that holds all the images you will use to move and push to the website a.k.a the current location of the images
        self.imageName = sys.argv[1]
        self.message = sys.argv[2]
        self.marker = "<!--" + sys.argv[3] + "-->" # My marker you can add your own. REMEMBER to have a consistent pattern.
    def moveFile(self):
        print("Moving Image...")
        shutil.move(self.imagePath + self.imageName, (self.folderPath + self.imageFolder))
        print("Image moved")
    def gitCommitAndPush(self):
        print("Beginning git push...")
        subprocess.check_output(["git", "status"], cwd=self.folderPath)
        subprocess.check_output(["git", "add", "."], cwd=self.folderPath)
        subprocess.check_output(["git", "commit", "-m", self.message], cwd=self.folderPath)
        subprocess.check_output(["git", "push"], cwd=self.folderPath)
        print("Git upload complete")
    def readFile(self):
        print("Reading file...")
        with open(self.filePath, 'r') as fileObject:

            self.v = 1
            self.g = fileObject.readlines()
            for i in self.g:
                value = i[0: len(i) - 1]
                if (value.strip() == self.marker):
                    print("Marker found ...")
                    break
                self.v += 1
        print("Reading Finished")
    def writeFile(self):
        print("Writing started...")
        with open(self.filePath, 'w') as fileObject:
            temp = self.g[self.v - 1]
            totalSpaces = len(temp) - len(temp.strip()) - 1
            spacer = " " * totalSpaces # Helps with indentation for new added code
            self.g[self.v - 1] = spacer + "<img src='" + self.imageFolder + self.imageName + "' style='width: 100%;' />\n" # Change this to what you want your code to be
            print("Marker changed")
            self.g.insert(self.v, temp)
            print("New marker added")
            fileObject.writelines(self.g)
            print("Write complete")
    def main(self):
        self.moveFile() # Moves the file from it's current location to it's new one which is in the project images folder
        self.readFile() # Read the 'html' file data to identify at which position the marker is located
        self.writeFile() # Writes back to the 'html' file and saves it with the new change
        self.gitCommitAndPush() # Commits and Pushes to git hub

start = imageUploader()
start.main()
