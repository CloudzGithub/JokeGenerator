import os
import requests
import tkinter as tk



root = tk.Tk()
root.title("Joke Generator")

root.geometry("1000x500")

def generate_joke():
    global jgrrj
    global jgrra
    jgre = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart")
    jgrrj = jgre.json()['setup']
    jgrra = jgre.json()['delivery']
    print(jgrrj)
    print(jgrra)
    return

generate_joke()

label1 = tk.Label(root, text=jgrrj)
label1.pack(pady=10)
label2 = tk.Label(root, text=jgrra)
label2.pack(pady=10)

def on_button_click():
    generate_joke()
    label1.config(text=jgrrj)
    label2.config(text=jgrra)
    return

button = tk.Button(root, text="Generate new joke", command=on_button_click)
button.pack(pady=10)

root.mainloop()