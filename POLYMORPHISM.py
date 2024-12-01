import tkinter as tk 

class Animal:
    def make_sound(self):
        return "Some Sound"
    
class Bird(Animal): 
    def make_sound(self):
            return "Tweet tweet"
        
class Dog(Animal):
    def make_sound(self):
        return "Woof woof"
    
class Snake(Animal):
    def make_sound(self):
        return "Sss Sss"

class Sheep(Animal):
    def make_sound(self):
        return "Mbek mbek"
    
#fungsi untuk menampilkan suara berdasarkan jenis hewan yang dipilih 
def show_sound(animal):
    label_result.config(text=animal.make_sound())

#MEMBANGUN JENDELA UTAMA MENGGUNAKAN TKINTER
root = tk.Tk()
root.title('Polimorfisme di Tkinter')

#LABEL UNTUK MENAMPILKAN HASIL SUARA
label_result = tk.Label(root, text="Klik salah satu tombol untuk mendengar suara hewan", font=('Arial', 14))
label_result.pack(pady=20)

#TOMBOL UNTUK MEMILIH 
button_bird = tk.Button(root, text='Burung', font=('Arial', 12), command=lambda: show_sound(Bird()))
button_bird.pack(pady=10)

button_dog = tk.Button(root, text='Anjing', font=('Arial', 12), command=lambda: show_sound(Dog()))
button_dog.pack(pady=10)

button_snake = tk.Button(root, text='Ular', font=('Arial', 12), command=lambda: show_sound(Snake()))
button_snake.pack(pady=10)

button_sheep = tk.Button(root, text='Kambing', font=('Arial', 12), command=lambda: show_sound(Sheep()))
button_sheep.pack(pady=10)

button_animal = tk.Button(root, text='General', font=('Arial', 12), command=lambda: show_sound(Animal()))
button_animal.pack(pady=10)

root.mainloop()
