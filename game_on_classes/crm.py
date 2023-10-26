from tkinter import*


def creat_task(event):
    task=entry.get()
    if task:
        todu_list.insert(END, task)
        entry.delete(0, END)
def move_task(event, source_list, target_list):
    source_list.get(source_list.curselection())

root=Tk()
root.title('KanBan')

todu_list=Listbox(root, height=15, width=30)
in_progress_list=Listbox(root, height=15, width=30)
win_progress=Listbox(root, height=15, width=30)

todu_list.grid(row=1, column=0, padx=10, pady=10)
in_progress_list.grid(row=1, column=1, padx=10, pady=10)
win_progress.grid(row=1, column=2, padx=10, pady=10)

entry=Entry(root, width=30)
entry.grid(row=0,column=0)

ad_buton=Button(root, text='add', width=15)
ad_buton.grid(row=0, column=1, pady=5)
ad_buton.bind('<Button-1>', creat_task)

todu_list.bind('<Double-Button-1>', lambda e: move_task(e, todu_list, in_progress_list))
in_progress_list.bind('<Double-Button-1>', lambda e: move_task(e, in_progress_list, done_list))

root.mainloop()