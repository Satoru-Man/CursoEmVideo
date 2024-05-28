# ler um arquivo de audio mp3 e reproduzi-lo
#C:\Users\claud\OneDrive\Documentos\BaselVisa\Schule\NWn_B1_Audios_KB\NWn_B1-1_Audios_KB\NWn_B1_KB_Audio_1-050.mp3
# arquivo = str('C:\Users\claud\OneDrive\Documentos\BaselVisa\Schule\NWn_B1_Audios_KB\NWn_B1-1_Audios_KB\NWn_B1_KB_Audio_1-050.mp3')

import pygame
pygame.init()
pygame.mixer.music.load('house_lo.mp3')
pygame.mixer.music.play()
pygame.event.wait()

# o programa executa sem erro, mas nao toca a musica do arquivo
# voltar aqui quando descobrir como tratar excecoes