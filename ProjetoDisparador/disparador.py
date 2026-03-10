import pywhatkit as kit
import pandas as pd
import time
import random

# Lendo a planilha dos jovens
df = pd.read_excel('contatos.xlsx')

# Nossa IA básica: variações de saudação pra não enviar texto igual
saudacoes = ["Fala", "E aí", "Opa", "Tudo bem,"]

print("Iniciando o disparo...")

for index, linha in df.iterrows():
    nome = str(linha['Nome'])
    numero = str(linha['Numero'])
    
    # Sorteia uma saudação diferente pra cada envio
    saudacao = random.choice(saudacoes)
    mensagem = f"{saudacao} {nome}! Aqui é o Douglas. Tenho um recado sobre a vaga de jovem aprendiz na Renapsi."
    
    print(f"Enviando para {nome} ({numero})...")
    
    # Dispara a mensagem instantaneamente
    # wait_time=15 (espera 15 seg pro zap web carregar)
    # tab_close=True (fecha a aba depois de enviar pra não travar o PC)
    kit.sendwhatmsg_instantly(numero, mensagem, wait_time=15, tab_close=True, close_time=3)
    
    # O SEGREDO ANTI-BAN: Pausa aleatória
    # Pausa de 30 a 60 segundos entre um envio e outro
    pausa = random.randint(30, 60)
    print(f"Mensagem enviada! Pausando por {pausa} segundos pra não cair no radar do Zap...\n")
    time.sleep(pausa)

print("Disparo concluído com sucesso, chefe!")