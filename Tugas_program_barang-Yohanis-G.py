brg = []
perintah = 0

while perintah !=7 :
	print('''1. Menambah
	2. Menghapus
	3. Mengedit
	4. Menampilkan
	5. Memeriksa barang
	6. Mencari index
	7. Keluar''')
	perintah = int(input("Masukkan perintah :"))
	if perintah == 1 :
		while True :
			elem = input("Masukkan barang :")
			brg.append(elem)
			
			stop = input("Ketik Y untuk berhenti, selain itu lanjut :").lower()
			if stop == 'y' :
				break
				
	elif perintah == 2 :
		while True :
			hps = int(input("Masukkan index yang akan dihapus :"))
			print(brg.pop(hps), "dihapus!")
			
			if hps > (len(brg) -1) :
				print("index tidak ditemukan")
				
			stop = input("Ketik Y untuk berhenti, selain itu lanjut :").lower()
			if stop == 'y' :
				break
				
	elif perintah == 3 :
		while True :
			edit = int(input("Masukkan index yang akan diedit :"))
			
			if edit > (len(brg) -1) :
				print("index tidak di temukan")
			else :
				brg [edit] = input("Masukkan barang yang baru :")
				
			stop = input("Ketik Y untuk berhenti selain itu lanjut :").lower()
			if stop == 'y' :
				break
				
	elif perintah == 4 :
		for i in range (len(brg)) :
			print(brg[i])
			
	elif perintah == 5 :
		cari = input("masukkan barang dicetak :")
		for i in range(len(brg)) :
			if brg [i] == cari :
				print("barang ada dalam list")
	elif perintah == 6 :
		cari3 = input("Masukkan barang yang dicari :")
		if cari3 in brg :
			print(f"{cari3} ada pada index ke-{brg.index(cari3)}")
		else :
			print("index tidak ditemukan")