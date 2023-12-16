import function
import PySimpleGUI as SG

lable = SG.Text("Type in a to do")
input_box=SG.InputText(tooltip="Enter to do",key="todo")
add_button=SG.Button("Add")
edit_button=SG.Button("Edit")
complete_button=SG.Button("Complete")
exit_button=SG.Button("Closed")
window=SG.Window('My To Do App',
                 layout=[[lable],[input_box,add_button],
                         [edit_button],[complete_button],
                         [exit_button]],
                 font=('Helvetica',20))
while True:
    event,values = window.read()
    print(event)
    print(values)

    if event == "Add":

            new_todo=values['todo']

            function.add(new_todo)
    elif event=="Closed":
       break



window.close()