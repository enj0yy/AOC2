# AOC2 - Cache Simulator
Graziele Fagundes e Rafael Freitas - M1

Execução: python cache_simulator.py nsets bsize assoc substituição flag_saida arquivo_de_entrada

Política de substituição suportada: R (random)

Testes:

python cache_simulator.py 256 4 1 R 1 bin_100.bin
        exato: 100 0.9200 0.0800 1.00 0.00 0.00
        
python cache_simulator.py 128 2 4 R 1 bin_1000.bin
        exato: 1000 0.8640 0.1360 1.00 0.00 0.00
        
python cache_simulator.py 16 2 8 R 1 bin_10000.bin
        aproximadamente: 10000 0.9306 0.0694 0.18 0.79 0.03
        
python cache_simulator.py 512 8 2 R 1 vortex.in.sem.persons.bin
        aproximadamente: 186676 0.8785 0.1215 0.05 0.93 0.02
        
python cache_simulator.py 1 4 32 R 1 vortex.in.sem.persons.bin
        aproximadamente: 186676 0.5447 0.4553 0.00 1.00 0.00
