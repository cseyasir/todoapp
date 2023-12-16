import function
import PySimpleGUI as SG

lable = SG.Text("Type in a to do")
input_box=SG.InputText(tooltip="Enter to do")
add_button=SG.Button("Add")
edit_button=SG.Button("Edit")
complete_button=SG.Button("Complete")

window=SG.Window('My To Do App',layout=[[lable],[input_box,add_button],[edit_button],[complete_button]])
window.read()
window.close()