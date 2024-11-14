import cv2
import easyocr

# Carica l'immagine utilizzando OpenCV
img = cv2.imread('etichetta.JPG')

# Converti l'immagine in scala di grigi
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applica un filtro di soglia (threshold)
_, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# Salva l'immagine pre-elaborata (opzionale)
cv2.imwrite('immagine_preprocessata.png', img)

# Crea il lettore EasyOCR per l'italiano
lettore = easyocr.Reader(['it'])

# Leggi il testo dall'immagine preprocessata
risultati = lettore.readtext('etichetta.JPG')

# Stampa i risultati
for (bbox, testo, confidenza) in risultati:
    print(f"Testo: {testo}, Confidenza: {confidenza}")


# Estrai solo i testi riconosciuti in una nuova lista
testi_riconosciuti = [testo for (_, testo, _) in risultati]

# Stampa la lista dei testi
print(testi_riconosciuti)
