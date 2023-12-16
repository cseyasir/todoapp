import function
import PySimpleGUI as SG

lable = SG.Text("Type in a to do")
input_box=SG.InputText(tooltip="Enter to do",key="todo")
add_button=SG.Button("Add")
list_box=SG.Listbox(values=function.get_todos(),key="todos",
                    enable_events=True,
                    size=[45,10])
edit_button=SG.Button("Edit")
complete_button=SG.Button("Complete")
exit_button=SG.Button("Exit")
window=SG.Window('My To Do App',
                 layout=[[lable],[input_box,add_button],
                         [list_box,edit_button,complete_button],
                         [exit_button]],
                 font=('Helvetica',10))
while True:
    event,values = window.read()
    print(event)
    print(values)


    if event == "Add":

            new_todo=values['todo']

            function.add(new_todo)
            todos=function.get_todos()
            window['todos'].update(values=todos)
    elif event=="Edit":
        todo_to_edit = values["todos"][0]
        new_todo=values['todo']
        todos=function.get_todos()
        index=todos.index(todo_to_edit)
        todos[index]=new_todo
        function.write_todos(todos)
        window["todos"].update(values=todos)
    elif event =="Complete":
        item_to_remve=(values["todos"][0])
        todos = function.get_todos()
        index=todos.index(item_to_remve)


        todos.pop(index)
        window["todos"].update(values=todos)
        todos = function.write_todos(todos)

    elif event =="todos":
        window['todo'].update(value=values['todos'][0])
    elif event=="Exit":
       break



window.close()