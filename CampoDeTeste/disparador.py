import pywhatkit as kit
import time
import random
import pyautogui

# Leitor dos contatos
with open('contatos.txt', 'r') as arquivo:
    numeros = arquivo.readlines()

# Aumentei a lista para o sorteio ser mais variado
saudacoes = [
    "Oi, tudo bem?", "Olá, tudo bem?", "E aí, tudo certo?", "Opa, como você tá?", 
    "Fala, beleza?", "Bom dia, tudo bem?", "Opa, Douglas aqui!", "Oi, como vai?"
]

print("Iniciando o disparo TURBO... Tira a mão do mouse!")

contador = 0    
for numero in numeros:
    numero_limpo = numero.strip() 
    if not numero_limpo:
        continue 
    
    contador += 1 
    inicio = random.choice(saudacoes)
    mensagem = f"{inicio} Aqui é o Douglas da Renapsi. Tenho um recado sobre a vaga de Jovem Aprendiz."
    
    print(f"[{contador}] Enviando para {numero_limpo}...")
    
    # Reduzi o wait_time para 20 (se sua internet for boa, carrega tranquilo)
    kit.sendwhatmsg_instantly(numero_limpo, mensagem, wait_time=20, tab_close=False)
    
    time.sleep(2)
    pyautogui.press('enter')
    
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    
    # Reduzi a pausa entre mensagens para 20 a 40 segundos
    # Isso acelera muito o processo final de 600 nomes
    pausa = random.randint(20, 40)
    print(f"Sucesso! Próximo em {pausa} segundos...\n")
    time.sleep(pausa)

    # Mantive o descanso de 10 min a cada 50, isso é vital para 600 envios!
    if contador % 50 == 0:
        print(f"☕ {contador} enviados. Pausa de 10 min para não ser banido.")
        time.sleep(600)

print("Fim! Robô está cansado, mas missão cumprida! 🚀")