trabalho_terca = False
trabalho_quinta = False

tv_50    = trabalho_terca and trabalho_quinta
sorvete  = trabalho_terca or  trabalho_quinta
tv_32    = trabalho_terca != trabalho_quinta

mais_saudavel = not sorvete

print("tv_50={} tv_32 ={} Sorvete ={} Saudavel ={}"
.format(tv_50, tv_32, sorvete, mais_saudavel) )
