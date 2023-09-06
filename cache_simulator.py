# Graziele Fagundes e Rafael Freitas - M1

import sys
import math
import random

def main():
	if (len(sys.argv) != 7):
		print("Numero de argumentos incorreto. Utilize:")
		print("python cache_simulator.py <nsets> <bsize> <assoc> <substituição> <flag_saida> arquivo_de_entrada")
		exit(1)
	
	nsets = int(sys.argv[1])			# nsets = numero de conjuntos
	bsize = int(sys.argv[2])			# bsize = tamanho do bloco
	assoc = int(sys.argv[3])			# assoc = grau de associatividade
	subst = sys.argv[4]					# subst = politica de substituicao
	flagOut = int(sys.argv[5])			# flagOut = flag de formataçao de saída
	arquivoEntrada = sys.argv[6]		# arquivoEntrada = arquivo de endereços

	cache_bit_validade = [0] * (nsets * assoc)	
	cache_tag = [0] * (nsets * assoc)			
	blocos_ocupados = 0

	n_bits_indice = int(math.log2(nsets))
	n_bits_offset = int(math.log2(bsize))
	n_bits_tag = 32 - n_bits_offset - n_bits_indice

	acessos = 0
	hit = 0
	miss_compulsorio = 0
	miss_capacidade = 0
	miss_conflito = 0
 
	with open(arquivoEntrada, 'rb') as file:
		endereco = file.read(4)

		while endereco:
			acessos += 1

			endereco_int = int.from_bytes(endereco, byteorder='big')

			tag = endereco_int >> (n_bits_offset + n_bits_indice)
			indice = (endereco_int >> n_bits_offset) & (2**(n_bits_indice) -1)

			# Procurar por hit em todas vias
			deu_hit = 0
			i = indice
			while (deu_hit != 1 and i < (nsets * assoc)):
				if ((cache_bit_validade[i] == 1) and (cache_tag[i] == tag)):
					hit += 1
					deu_hit = 1
				i += nsets

			# Caso não ocorrer hit procurar onde colocar endereço
			if (deu_hit == 0):

				# Procurar por uma posição vazia
				achou_posicao = 0
				i = indice
				while (achou_posicao != 1 and i < (nsets * assoc)):
					if (cache_bit_validade[i] == 0):
						achou_posicao = 1
						miss_compulsorio += 1
						blocos_ocupados += 1
						cache_bit_validade[i] = 1
						cache_tag[i] = tag
					i += nsets

				# Caso não encontrar posição vazia calcular uma posição aleatória para substituir
				if (achou_posicao == 0):
					if (cacheCheia(blocos_ocupados, nsets, assoc)):
						miss_capacidade += 1
					else:
						miss_conflito += 1
					
					r = random.randint(0,assoc-1)
					cache_bit_validade[r*nsets+indice] = 1
					cache_tag[r*nsets+indice] = tag

			endereco = file.read(4)
   
	total_misses = miss_capacidade + miss_conflito + miss_compulsorio
 
	if(flagOut == 0):
		print("---------------------------------------")
		print("Acessos: {:.0f}".format(acessos))
		print("Taxa de hit: {:.4f}".format(hit/acessos))
		print("Taxa de miss: {:.4f}".format(total_misses/acessos))
		print("Taxa de miss compulsório: {:.2f}".format(miss_compulsorio/total_misses))
		print("Taxa de miss capacidade: {:.2f}".format(miss_capacidade/total_misses))
		print("Taxa de miss conflito: {:.2f}".format(miss_conflito/total_misses))
		print("---------------------------------------")

	else:
		print("{:.0f}".format(acessos), end=" ")
		print("{:.4f}".format(hit/acessos), end=" ")
		print("{:.4f}".format(total_misses/acessos), end=" ")
		print("{:.2f}".format(miss_compulsorio/total_misses), end=" ")
		print("{:.2f}".format(miss_capacidade/total_misses), end=" ")
		print("{:.2f}".format(miss_conflito/total_misses))

def cacheCheia(blocos_ocupados, nsets, assoc):
	if blocos_ocupados < (nsets * assoc):
		return 0
	else:
		return 1
	
if __name__ == '__main__':
	main()