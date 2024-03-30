import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')
        self.create_menu()
        self.create_themes()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Light Theme", command=self.light_theme)
        theme_menu.add_command(label="Dark Theme", command=self.dark_theme)
        menubar.add_cascade(label="Themes", menu=theme_menu)

        self.root.config(menu=menubar)

    def create_themes(self):
        self.style = ttk.Style()
        self.style.theme_create("light", parent="clam", settings={
            "TFrame": {"configure": {"background": "#ffffff"}},
            "TLabel": {"configure": {"foreground": "#000000", "background": "#ffffff"}},
            "TButton": {"configure": {"foreground": "#000000", "background": "#ffffff"}},
            "TScrollbar": {"configure": {"background": "#ffffff"}},
            "TEntry": {"configure": {"background": "#ffffff"}},
            "TText": {"configure": {"background": "#ffffff"}},
        })
        self.style.theme_create("dark", parent="clam", settings={
            "TFrame": {"configure": {"background": "#2e2e2e"}},
            "TLabel": {"configure": {"foreground": "#ffffff", "background": "#2e2e2e"}},
            "TButton": {"configure": {"foreground": "#ffffff", "background": "#2e2e2e"}},
            "TScrollbar": {"configure": {"background": "#2e2e2e"}},
            "TEntry": {"configure": {"background": "#2e2e2e", "foreground": "#ffffff"}},
            "TText": {"configure": {"background": "#2e2e2e", "foreground": "#ffffff"}},
        })
        self.style.theme_use("light")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, content)

    def save_file(self):
        content = self.text_area.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Info", "File saved successfully.")

    def light_theme(self):
        self.style.theme_use("light")

    def dark_theme(self):
        self.style.theme_use("dark")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
