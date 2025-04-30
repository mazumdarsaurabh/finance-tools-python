![Screenshot of Jira](Screenshot.png)

Step 1: Capture and Save the Screenshot

Capture: Take a screenshot of your JIRA board.

Save: Save the screenshot as an image file (e.g., jira_board.png, jira_board.jpg).

Step 2: Add the Image to Your Repository

Open a terminal in your project's root directory.

Create an "images" folder (if it doesn't exist):

mkdir -p images

Move the image to the "images" folder:

mv jira_board.png images/  #  Replace "jira_board.png" with your actual filename

If you want to put the image in the root directory, skip the mkdir and mv commands.  Just make sure the image file is in your project's root.

Step 3: Update README.md

Open README.md in a text editor.

Add Markdown to reference the image:

## Project Tracking - JIRA Board

Here's our JIRA board:

![JIRA Board Screenshot](images/jira_board.png)  #  Adjust the path if needed

If the image is in the root directory:

## Project Tracking - JIRA Board

Here's our JIRA board:

![JIRA Board Screenshot](jira_board.png)  #  Adjust the filename if needed

Save the README.md file.

Step 4: Commit and Push

Add the image and README.md to Git:

git add images/jira_board.png  #  If image is in "images"
git add README.md

If the image is in the root directory:

git add jira_board.png
git add README.md
