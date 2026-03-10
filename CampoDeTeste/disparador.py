import pywhatkit as kit
import time
import random
import pyautogui

# Leitor dos contatos
with open('contatos.txt', 'r') as arquivo:
    numeros = arquivo.readlines()

# Variações anti-spam hehehe
saudacoes = [
    "Oi, tudo bem?",
    "Olá, tudo bem?",
    "E aí, tudo certo?",
    "Opa, como você tá?",
    "Fala, beleza?"
]

print("Iniciando o disparo... Tira a mão do mouse ou o programador te bate!")

for numero in numeros:
    numero_limpo = numero.strip() 
    
    if not numero_limpo:
        continue # Pula linhas em branco
        
    # Sorteia uma saudação e monta a mensagem
    inicio = random.choice(saudacoes)
    mensagem = f"{inicio} Aqui é o Douglas da Renapsi. Tenho um recado sobre a vaga de Jovem Aprendiz."
    
    print(f"Enviando para {numero_limpo}...")
    
    # Abre o zap, espera 20 seg pra carregar e digita
    kit.sendwhatmsg_instantly(numero_limpo, mensagem, wait_time=20, tab_close=False)
    
    # Força o envio (aperta Enter)
    time.sleep(2)
    pyautogui.press('enter')
    
    # Fecha a aba pra não travar o navegador
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    
    # Pausa anti-ban (30 a 60 segundos)
    pausa = random.randint(30, 60)
    print(f"Mensagem enviada! Pausando por {pausa} segundos...\n")
    time.sleep(pausa)

print("Fim da lista! O robô parou sozinho.")