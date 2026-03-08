import customtkinter as ctk
import os
from datetime import datetime
from PIL import Image

# Configuración visual basada en el Manual de Estilo NeoOS
ctk.set_appearance_mode("dark")
COLOR_BG = "#1a1c31"       # Fondo degradado azul oscuro
COLOR_ACCENT = "#00f2ff"  # Cian Neón para elementos activos

class NeoOS(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- CONFIGURACIÓN DE VENTANA (MODO NO PANTALLA COMPLETA) ---
        self.title("NeoOS Alpha v0.0.1")
        self.geometry("1100x700") # Tamaño inicial equilibrado
        self.resizable(True, True) # Permite al usuario redimensionar
        self.configure(fg_color=COLOR_BG)
        
        # Contenedor para las transiciones de pantalla
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        # Iniciar con la pantalla de Login
        self.show_login_screen()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # --- PANTALLA DE LOGIN ---
    def show_login_screen(self):
        self.clear_screen()
        # Caja de login con efecto Glassmorphism
        frame = ctk.CTkFrame(self.container, fg_color="#12121f", corner_radius=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ctk.CTkLabel(frame, text="NEO OS", font=("Orbitron", 40, "bold"), text_color=COLOR_ACCENT).pack(pady=30, padx=50)
        
        self.user_en = ctk.CTkEntry(frame, placeholder_text="Usuario", width=250)
        self.user_en.pack(pady=10)
        self.pass_en = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*", width=250)
        self.pass_en.pack(pady=10)
        
        ctk.CTkButton(frame, text="ENTRAR", fg_color=COLOR_ACCENT, text_color="black", 
                      font=("Segoe UI", 14, "bold"), command=self.show_loading_screen).pack(pady=30)

    # --- PANTALLA DE CARGA (Captura de la Nube) ---
    def show_loading_screen(self):
        self.clear_screen()
        frame = ctk.CTkFrame(self.container, fg_color="transparent")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Intentar cargar nube.png, si falla usa símbolo Unicode
        try:
            img = ctk.CTkImage(Image.open("nube.png"), size=(120, 80))
            ctk.CTkLabel(frame, image=img, text="").pack(pady=20)
        except:
            ctk.CTkLabel(frame, text="☁", font=("Arial", 80), text_color="white").pack(pady=20)

        ctk.CTkLabel(frame, text="Cada bit es un paso hacia la perfección.", 
                      font=("Segoe UI", 22), text_color="white").pack()
        
        self.bar = ctk.CTkProgressBar(frame, width=350, height=10, progress_color=COLOR_ACCENT)
        self.bar.set(0)
        self.bar.pack(pady=25)
        
        # Texto de estado basado en especificaciones técnicas
        ctk.CTkLabel(frame, text="Iniciando Firewall con IA y Protección Proactiva...", 
                      font=("Segoe UI", 12), text_color="#666").pack()

        self.progress = 0
        self.update_progress()

    def update_progress(self):
        if self.progress < 1:
            self.progress += 0.02
            self.bar.set(self.progress)
            self.after(40, self.update_progress)
        else:
            self.show_desktop()

    # --- ESCRITORIO (Diseño Final) ---
    def show_desktop(self):
        self.clear_screen()
        
        # Panel de Iconos Laterales
        icons_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        icons_frame.place(x=30, y=50)
        
        # Apps principales según Documento de Requisitos
        apps = [("💻", "Terminal"), ("📁", "Archivos"), ("🌐", "Navegador"), ("⚙", "Ajustes")]
        for icon, name in apps:
            btn = ctk.CTkButton(icons_frame, text=f"{icon}\n{name}", fg_color="transparent", 
                                 text_color="#888", font=("Segoe UI", 12),
                                 width=90, height=90, hover_color="#2d2d3d")
            btn.pack(pady=10)

        # Barra de Tareas inferior (Taskbar)
        taskbar = ctk.CTkFrame(self.container, height=60, fg_color="#0d0d12", corner_radius=0)
        taskbar.pack(side="bottom", fill="x")
        
        # Botón de Inicio con branding de NeoOS
        ctk.CTkButton(taskbar, text="NeoOS", width=100, height=40, 
                      fg_color="#1e1e26", font=("Orbitron", 12, "bold")).pack(side="left", padx=15)
        
        # Reloj y fecha
        self.clock = ctk.CTkLabel(taskbar, text="", font=("Consolas", 13), text_color="#555")
        self.clock.pack(side="right", padx=25)
        self.refresh_clock()

    def refresh_clock(self):
        now = datetime.now().strftime("%H:%M:%S | %d/%m/%Y")
        try:
            self.clock.configure(text=now)
            self.after(1000, self.refresh_clock)
        except: pass

if __name__ == "__main__":
    app = NeoOS()
    app.mainloop()